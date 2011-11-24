#!/usr/bin/perl

use strict;
use Getopt::Long;

# Declare options
my $help;
my $model     = 0;
my $fullname  = '';
my $makefiles = '';
my $result = GetOptions( 'h|?|help'  => \$help,
                         'm|model=i' => \$model,
                         'full|f'    => \$fullname,
                         'makefiles' => \$makefiles );

# Check arguments
if ( !@ARGV || $help || !$result ) {
    die "Usage: ".$0." [-full|f] [-makefiles] -m <model> <files>\n";
}

# Order of output
my @order = ( 'chi2', 'm0', 'm12', 'a0', 'tanb', 'sgnmu', 'mtop', 'mz', 'gammaz', 'dahad', 'mh' );
my @precision = ( '%6.2f','%10.4f','%10.4f','%10.3f','%8.3f', '%6.0f', '%10.4f', '%10.5f', '%8.4f', '%10.6f', '%7.1f', '%12.0f', '%12.0f' );
my @format;
foreach my $prec ( @precision ) { 
  $prec =~ /%(\d+)\./; # extract number of fields for string format
  push @format, "%$1s";
}

# Global variables
my $modelDir = "models";
my @files = @ARGV;
my $ifile = 0;
my %results;  # Names of files and fit results


# Loop on all files
foreach my $file ( @files ) {
    my $fieldString="";
    my $chi2 = 1e9;
    
# Parse file and get relevant lines
    open( IN, $file ) or die "Couldn't open $file: $!";
    while( <IN> ) {
        chomp();
        if ( /^\s*115\.0*\s+[0-9\.]+\s+([0-9\.e\+\-]+)/i ) { #WARNING: this could be fragile!
            my $tmpChi2 = $1;
            if ( $tmpChi2<$chi2) {
                $fieldString = $_;    # Retrieve three lines
                    $fieldString .= <IN>;
                $fieldString .= <IN>;
                $chi2 = $tmpChi2;
            }
        }
    }
    close( IN );
    
    my $fileName = $file;
# Display dir name or full name
    if ( !$fullname ) { $fileName =~ s/.*?\/?(.*)\/.*$/$1/; }
    
# Retrieve fields and store results (if file was processed)
    if ( length($fieldString)>0 ) {
      $results{$fileName} = &parseFields($fieldString); # Store chi2 to write out models
    } else {
      print "Failed to parse $file\n";
    }
}

my $ifile = 0;
foreach my $file ( keys %results ) {
    if ( !$ifile ) { # Print header
        printf "%15s",'scenario';
        for (my $i=0;$i<@order;++$i) { printf $format[$i],$order[$i]; }
        if ( $model==2 ) { printf $format[@order].$format[@order+1],'mhu2','mhd2'; }
        print "\n";
    }
    # File label is either file name or directory name
    if ($fullname) { printf "%s\n%15s",$file," "; }
    else           { printf "%15s",$file; }
    # Print results (model-dependent)
    for (my $i=0;$i<@order;++$i) { printf $precision[$i], $results{$file}->{$order[$i]}; }
    if ( $model==2 ) {
        printf $precision[@order].$precision[@order+1], $results{$file}->{'mhu2'}, $results{$file}->{'mhd2'};
    }
    print "\n";
    ++$ifile;
}

# Create models if requested (but only if not full name: one model per scenario!)
if ( $makefiles && !$fullname ) {
    foreach my $dir ( keys %results ) {
        if ( !$results{$dir} ) {
            print "  *** No chi2 for ".$dir.": skipping\n";
            next;
        }
        my $constraints = $dir."/constraints.txt";
        my $masses      = $dir."/spectrum_constraints.txt";
        my $steering    =
        $dir."/steer_npfitter_".($model==0?"msugra":($model==2?"nuhm":($model==4?"rsugra":($model=5?"vcmssm":"msugra")))).".txt";
        my $output = $modelDir."/".$dir.".txt";
        &makeModel( $constraints, $masses, $steering, $output, $results{$dir} );
    }
}

#___________________________________________________________________________
sub parseFields {
    my $string = shift;
    $string =~ s/^\s*//;
        
my @fields = split(/\s+/,$string);
my $i = 5;

my $results = { 'mh'    => $fields[1],    # 1
    'chi2'  => $fields[2],    # 2
    'm0'    => $fields[$i],   # 5
    'm12'   => $fields[++$i], # 6
    'a0'    => $fields[++$i], # 7
    'tanb'  => $fields[++$i], # 8
    'sgnmu' => $fields[++$i] }; # 9
if ( $model == 2 ) {
    $results->{'mhu2'} = $fields[++$i];
    $results->{'mhd2'} = $fields[++$i];
}
$results->{'mtop'}   = $fields[++$i];
$results->{'mz'}     = $fields[++$i];
$results->{'gammaz'} = $fields[++$i];
$results->{'dahad'}  = $fields[++$i];

return $results;
}


#___________________________________________________________________________
# Make output model file
sub makeModel {
    
    my $constraints = shift;
    my $masses = shift;
    my $steering = shift;
    my $output = shift;
    my $result = shift;
    
    open(OUT,">$output") or die "Couldn't open $output: $!";
    
    my $nvars = ($model==0)?76:78;
    my $chi2 = $result->{chi2};

    my @parameters;
    my @errors;
    
    # Retrieve steering information
    open(IN,$steering) or die "Couldn't open $steering: $!";
    my $lines = 0;
    while (<IN>) {
        $lines++;
        if ( $lines==4 ) { # Retrieve information on input parameters
            @parameters = split(/\s+/);
        }
        elsif ( $lines == 6 ) { # Information on errors
            @errors = split(/\s+/);
        }
    }
    close(IN);


    # Print header
    print OUT <<HEAD
C- Number of constraints - minimum chi^2
$nvars $chi2
C- CONSTRAINT: 1=use, value, exp. error, theo. error
HEAD
        ;
    
    # Print chi2 and model parameters
    print OUT '0  '.sprintf("%-9.4f%-11i%-8i",$result->{chi2},0,0).'! 0 #chi^{2}'."\n";
    print OUT '0  '.sprintf("%-9.2f%-11i%-8i",$result->{m0},0,0).'! 1 M_{0} [GeV/c^{2}]  '."\n";
    print OUT '0  '.sprintf("%-9.2f%-11i%-8i",$result->{m12},0,0).'! 2 M_{1/2} [GeV/c^{2}]'."\n";
    print OUT '0  '.sprintf("%-9.2f%-11i%-8i",$result->{a0},0,0).'! 3 A_{0} [GeV/c^{2}]  '."\n";
    print OUT '0  '.sprintf("%-9.4f%-11i%-8i",$result->{tanb},0,0).'! 4 tan#beta  '."\n";
    print OUT '0  '.sprintf("%-9.0f%-11i%-8i",$result->{sgnmu},0,0).'! 5 sgnmu  '."\n";
    my $i=5;
    if ( $model == 2 ) {
        print OUT '0  '.sprintf("%-9.0f%-11i%-8i",$result->{mhu2},0,0).'! '.++$i.' m(H_{u}^{2})'."\n";
        print OUT '0  '.sprintf("%-9.0f%-11i%-8i",$result->{mhd2},0,0).'! '.++$i.' m(H_{d}^{2})'."\n";
    }
    # Standard model parameters might be free (error<0), in which case we print the result
    if ( $errors[$i]<0 ) { print OUT '0  '.sprintf("%-9.2f%-11i%-8i",$result->{mtop},0,0).'! '.++$i."  m_{top}\n"; } 
    else { print OUT '1  '.sprintf("%-9.2f%-11.2f%-8i",$parameters[$i],$errors[$i],0).'! '.++$i."  m_{top}\n"; }
    if ( $errors[$i]<0 ) { print OUT '0  '.sprintf("%-9.4f%-11i%-8i",$result->{mz},0,0).'! '.++$i."  m_{Z}\n"; }
    else { print OUT '1  '.sprintf("%-9.4f%-11.4f%-8i",$parameters[$i],$errors[$i],0).'! '.++$i."  m_{Z}\n"; }
    if ( $errors[$i]<0 ) { print OUT '0  '.sprintf("%-9.4f%-11i%-8i",$result->{gammaz},0,0).'! '.++$i."  #Gamma_{Z}\n"; }
    else { print OUT '1  '.sprintf("%-9.4f%-11.4f%-8i",$parameters[$i],$errors[$i],0).'! '.++$i."  #Gamma_{Z}\n"; }
    if ( $errors[$i]<0 ) { print OUT '0  '.sprintf("%-9.6f%-11i%-8i",$result->{dahad},0,0).'! '.++$i."  #Delta#alpha_{had}\n"; }
    else { print OUT '1  '.sprintf("%-9.6f%-11.6f%-8i",$parameters[$i],$errors[$i],0).'! '.++$i."  #Delta#alpha_{had}\n"; }
       
# #  print OUT '0  '.sprintf("%-9.4f%-11i%-8i",$result->{gammaz},0,0).'! '.++$i.' gammaz  '."\n";
# #  print OUT '0  '.sprintf("%-9.6f%-11i%-8i",$result->{dahad},0,0).'! '.++$i.' dahad  '."\n";
# # THESE ARE ACTUALLY SM CONSTRAINTS: FIX THEN TO INPUT VALUE!
#     print OUT '1  172.4    1.2        0       ! '.++$i.'  Model mtop [GeV/c^2]'."\n";
#     print OUT '1  91.1875  0.0021     0       ! '.++$i.'  Model mZ [GeV/c^2]'."\n";
#     print OUT '0  0        0          0       ! '.++$i.' Model dummy (Gz)'."\n";
#     print OUT '1  0.02758  0.00035    0       ! '.++$i.' Model dahad'."\n";
    
#  Dump constraints
    open(IN,$constraints) or die "Couldn't open $constraints: $!";
    my $begin = 0;
    while (<IN>) {
        if ( /CONSTRAINT/ ) { # Marker: start from here
            $begin++;
            next;
        }
        if ( $begin ) {
            ++$i;
            my $line = $_;
            $line =~ s/(\!\s+)\d+/$1$i/;
            print OUT $line;
        }
    }
    close(IN);

# Dump masses
    open(IN,$masses) or die "Couldn't open $masses: $!";
    my $begin = 0;
    while (<IN>) {
        if ( /CONSTRAINT/ ) { # Marker: start from here
            $begin++;
            next;
        }
        if ( $begin ) {
            ++$i;
            my $line = $_;
            $line =~ s/(\!\s+)\d+/$1$i/;
            print OUT $line;
        }
    }
    close(IN);
    
    close(OUT);
    print "  -> $output written\n";
}
