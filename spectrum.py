#!/usr/bin/python
#
#  Plot SUSY mass spectrum from SLHA file
#
#  $Id: spectrum.py,v 1.4 2009/06/25 14:40:25 fronga Exp $

import re, array, sys
from ROOT import *
from optparse import OptionParser

# Define PDG mass names
names = {    # Higgs sector
          25 : 'h^{0}',
          35 : 'H^{0}',
          36 : 'A^{0}',
          37 : 'H^{#pm}',
          # Squark sector
          1000001 : '#tilde{d}_{L}',
          1000002 : '#tilde{u}_{L}',
          1000003 : '#tilde{s}_{L}',
          1000004 : '#tilde{c}_{L}',
          1000005 : '#tilde{b}_{1}',
          1000006 : '#tilde{t}_{1}',
          2000001 : '#tilde{d}_{R}',
          2000002 : '#tilde{u}_{R}',
          2000003 : '#tilde{s}_{R}',
          2000004 : '#tilde{c}_{R}',
          2000005 : '#tilde{b}_{2}',
          2000006 : '#tilde{t}_{2}',
          # Slepton sector
          1000011 : '#tilde{l}_{L}',    # Take e for slepton
          1000012 : '#tilde{#nu}_{l}',
          1000015 : '#tilde{#tau}_{1}',
          2000011 : '#tilde{l}_{R}',    # Take e for slepton
          2000012 : '#tilde{#nu}_{R}',
          2000015 : '#tilde{#tau}_{2}',
          # Gluino
          1000021 : '#tilde{g}',
          # neutralino/chargino sector
          1000022 : '#tilde{#chi}_{1}^{0}',
          1000023 : '#tilde{#chi}_{2}^{0}',
          1000024 : '#tilde{#chi}_{1}^{#pm}',
          1000025 : '#tilde{#chi}_{3}^{0}',
          1000035 : '#tilde{#chi}_{4}^{0}',
          1000037 : '#tilde{#chi}_{2}^{#pm}',
          }

#_______________________________________________________________
def usage():
   print "Usage: ",sys.argv[0]," [-h|v] [-o output] <SLHA file>"

#_______________________________________________________________
def scanFile( file, vars, masses ):

   """ Scan SLHA file and retrieve (s)particle masses
       from spectrum """

   # Regexp for spectrum entry in SLHA
   pattern = re.compile("(\d+)\s+([\-\+\.eE\d]+)\s+\#\s+(\S+)",re.I)

   # Regexp for any variable
   varPat = re.compile("^\s*\d+\s+(.*)\#\s+(\S+)")

   print "Scanning ", file

   # Check input file
   try:
       f = open(file)
   except IOError:
       print "File",file,"does not seem to exist"
       usage()
       sys.exit(3)
   
   start = 0
   for line in f.readlines():
      vm = re.search(varPat,line)
      if (vm and vars):
        if vars.count( vm.group(2) ):
           print vm.group(2),'=',vm.group(1)
      if re.compile("^block\s+mass",re.I).match( line ):
         start += 1
         if verbose: print "Found spectrum start:", line
         continue
      # Start has been found
      if start>0:
         if re.compile("^block",re.I).match( line ):
            start=0 # End of spectrum block
         else:
            # In spectrum: search for particle
            m = re.search( pattern, line )
            if m:
               masses[int(m.group(1))] = float(m.group(2))
            else:
               if verbose: print 'Line does not match:',line
   

#_______________________________________________________________
def legend_from_group( pdgId, groups, display_names ):
   """ Check if PDG ID is part of a group
       Returns legend to plot """

   ingroup = False
   first = False
   clegend = ''

   # Search and check if in group, and first
   group = 0
   if groups:
      for curGroup in groups:
         ipos = 0
         for curId in curGroup.split(","):
            ipos = ipos+1
            if pdgId==int(curId):
               ingroup = True
               if ipos==1:
                  first = True
         if ingroup: break
         group = group+1

#   print pdgId, ingroup, first,group
            
   if not ingroup:
      clegend = names[pdgId]
   else:
      if ingroup and not first:
         clegend = None
      else:
         if groups:
            if display_names and len(display_names)>group:
               clegend = display_names[group]
            else:
               for curId in groups[group].split(","):
                  clegend = clegend+names[int(curId)]+","
               clegend = clegend.rstrip(',')

   return clegend
   
#_______________________________________________________________
def align_from_list( pdgId, align):
    """ Check if a special alignment has been set for PDG ID """

    for curId in align:
        if pdgId == int(curId[1:]):
            if curId[0] == '-': return -1
            else: return +1
    return 0

#_______________________________________________________________
def plotMasses( masses, options ):
   """ Plot masses through ROOT
   """

   # Initialise canvas
   c = TCanvas( 'c', 'SUSY spectrum', 10, 10, 860, 860 )
   c.SetLeftMargin(0.15)
   c.SetBorderMode(0)
   c.SetFillColor(0) 
   
   # Canvas style
   gStyle.SetOptTitle(0)
   gStyle.SetOptStat(0)   

   # Define parameters
   xmax = 10.
   ymax = options.ymax
   xstart = 1.4
   ystart = 20.

   c.Range( -xstart, -ystart, xmax+xstart, ymax+ystart )

   lwidth = 0.5
   tspace = 0.
   cols = [ 1., 3.25, 5.5, 7.8 ]
   fsize  = 24

   # Draw frame
   frame = TFrame( 0., 0., xmax, ymax )
   frame.SetBorderMode(0)
   frame.SetFillColor(0)
   frame.Draw()

   # Draw axis
   ax = TGaxis( 0., 0., 0., ymax, 0., ymax )
   ax.SetLabelFont(63)
   ax.SetLabelSize(1.2*fsize)
   ax.SetTitleFont(63)
   ax.SetTitleSize(1.2*fsize)
   if options.dotitle: ax.SetTitle( "m [GeV/c^{2}]" )
   ax.SetTitleOffset(1.5)
   ax.Draw()
   axRight = ax.Clone()
   axRight.SetX1(xmax)
   axRight.SetX2(xmax)
   axRight.SetOption("+L")
   axRight.Draw()

   # Lines and text
   l = TLine()
   l.SetLineWidth(2)
   t = TLatex()
   t.SetTextAlign(32)
   t.SetTextFont(63)
   t.SetTextSize(fsize)
   
   icol = 0 # For the column placement
   colindex = 0 # coloring
   # Color depends on ROOT version
   m = re.compile("^(\d+)\.(\d+)\/").match(gROOT.GetVersion())
   newCol = true
   if int(m.group(2))<16:
      newCol = false
      print "Using old coloring scheme"
   
   alternate = 1
   smear = 1
   for pdgId in masses.keys():
      if pdgId in names.keys():
         if masses[pdgId]<0: masses[pdgId] = -masses[pdgId]
         if masses[pdgId]>ymax:
            print "Warning: mass of ",names[pdgId]," is out of range:"
            print masses[pdgId],">",ymax
                   
         if ( pdgId<100 ): # Higgs sector
            icol = 0
            if newCol:
               colindex = kRed-2
            else:
               colindex = 2
         elif ( pdgId%10000<10 ): # Squark sector
            icol = 3
            if newCol:
               colindex = kGreen+2
            else:
               colindex = 3
         elif ( pdgId%10000>20 ): # -ino sector
            icol = 2
            if newCol:
               colindex = kBlue-2
            else:
               colindex = 4
         else:
            icol = 1
            if newCol:
               colindex = kMagenta+2
            else:
               colindex = 6
         # Check if it should be grouped
         legend = legend_from_group( pdgId, options.groups, options.display_names )
         align = 0
         if options.align: align = align_from_list( pdgId, options.align)
         if legend:
            if align == 0: alternate = (-1)**(pdgId%2)
            else: alternate = align
            smear = (pdgId%10)/10.
            l.SetLineColor( colindex )
            l.DrawLine( smear+cols[icol]-lwidth/2., masses[pdgId],
                        smear+cols[icol]+lwidth/2., masses[pdgId] )
            t.SetTextColor( colindex )
            t.SetTextAlign(22-10*alternate)
            t.DrawLatex( smear+cols[icol]+alternate*(lwidth+tspace), masses[pdgId]+3,
                         legend )

   c.SaveAs( options.output )

#_______________________________________________________________
#### run fill function if invoked on CLI
if __name__ == '__main__':

   parser = OptionParser()
   parser.add_option("-v", "--verbose",action="store_true", dest="verbose", 
                      default=False, help="turn on verbosity")
   # Input/Output
   parser.add_option("-f","--file", dest="input", metavar="FILE",
                    help="[mandatory] input file in SLHA format")
   parser.add_option("-o", "--output", dest="output", metavar="FILE",
                    help="write spectrum to FILE (extension determines format)")
   # SLHA Parameter options
   parser.add_option("--vars",action="append",dest="vars",type="string",
                    help="retrieve additional variables from SLHA.\n"
                         "Use multiple times to add multiple variables")
   # Plotting
   parser.add_option("--group",action="append",dest="groups",type="string",
                     help="group some particles (comma-separated list of PDG IDs).\n"
                     "Use multiple times to make multiple groups.")
   parser.add_option("--display",action="append",dest="display_names",type="string",
                     help="attach name to group of particles."
                     "Use in same order as --group.")
   parser.add_option("--align",action="append",dest="align",type="string",
                    help="define alignment explicitly: +/-[PDG ID].")
   parser.add_option("--ymax",dest="ymax",type="float",metavar="NUM",default=1000.,
                     help="y maximum [default: %default]")
   parser.add_option("--no-title",dest="dotitle",action="store_false",
                     default=True,
                     help="do not draw axis title")
   parser.add_option("--no-display",dest="doplot",action="store_false",
                     default=True,
                     help="do not actually draw")
   
   (options, args) = parser.parse_args()

   # Check arguments
   if options.input == None:
      parser.error('Input file is missing\n'+parser.format_option_help())

   # Set some global variables
   verbose = options.verbose
   masses = dict()

   # Set input/output file names
   if options.output==None:
      options.output = re.sub(r'\..*$','.eps',options.input)
      if options.output.find('.eps') == -1:
         options.output += '.eps'

   
   print "Will store result in ", options.output
   scanFile(options.input,options.vars,masses)
   if verbose:
      for pdgId in masses.keys():
          if pdgId in names.keys():
              print pdgId,names[pdgId],": ",masses[pdgId]
   if options.doplot: plotMasses(masses,options)
