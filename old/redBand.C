#ifndef __CINT__
#include <iostream>
#include <cmath>

#include "TTree.h"
#include "TH2F.h"
#include "TLatex.h"
#include "TString.h"
#include "TCanvas.h"
#include "TGraph.h"
#include "TStyle.h"
#endif


double findMh( TGraph* graph, double chi2, double mHstart );
TTree* chi2tree;
bool doSmooth = false;
bool doPub = false;
bool doBands = true;
// 20000
static const int MAXPOINTS = 20000000;
double LEPLIMIT = 114.4;


//____________________________________________________________________________________
// Find value of Mh corresponding to chi2, starting from mHstart
double findMh( TGraph* graph, double chi2, double mHstart )
{

  double step = 0.01;
  double mH = mHstart;
  double curry = -1;
  while ( mH<graph->GetX()[graph->GetN()-1] ) {
    double y = graph->Eval( mH, 0, "S" );
    if ( curry>0 && fabs( curry-chi2) < fabs( y-chi2 ) ) {
      // Last y was the one      
      mH -= step;
      std::cout << " mH value for Dchi2 = " << chi2 << ": " << mH << std::endl;
      return mH;
    } else
      curry = y;
    
    mH += step;
  }
  std::cout << "Couldn't find a value for chi2=" << chi2 << "(mHstart = " << mHstart << ")" << std::endl;
  return 0.0;
}


//________________________________________________________________________________________
// Zero-suppress graph (put minimum at 0)
void zeroSuppress( TGraph* graph ) {

  double* x = graph->GetX();
  double* y = graph->GetY();

  // Find minimum
  double ymin = 1e9;
  for ( int i=0; i<graph->GetN(); ++i ) 
    if ( y[i] < ymin ) ymin = y[i];

  std::cout << "Found minimum: " << ymin << std::endl;

  // Zero-suppress
  for ( int i=0; i<graph->GetN(); ++i ) 
    graph->SetPoint(i,x[i],y[i]-ymin);

  

}

//____________________________________________________________________________________
// Plot red band. NEW: with large number of sampling points
TGraph* redBand2( TGraph* graph, double error, double xmin, double step = 0.05 )
{

  int norig = graph->GetN();
  int npoints = static_cast<int>((graph->GetX()[norig-1]-graph->GetX()[0])/step);
  std::cout << "npoints = " << npoints << std::endl;
  
  if ( npoints > MAXPOINTS ) {
    std::cerr << "FATAL: npoints = " << npoints << " is greater than MAXPOINTS" << std::endl;
    exit(-1);
  }
  double x1[2*MAXPOINTS+1], y1[2*MAXPOINTS+1];
  double x2[MAXPOINTS], y2[MAXPOINTS];
  
  // Find mH at minimum
  int i1=0; // iterator for upper curve
  int i2=0; // iterator for lower curve
  double ix = graph->GetX()[0];
  while ( ix<=graph->GetX()[norig-1] )
    {
      double iy = graph->Eval( ix, 0, "S" );
      
      if ( ix<=xmin-error ) {//- 
        x1[i1] = ix+error; y1[i1]=iy; ++i1; 
        x2[i2] = ix-error; y2[i2]=iy; ++i2;
      }
      else if ( ix>=xmin+error) { //+
        x1[i1] = ix-error; y1[i1]=iy; ++i1; 
        x2[i2] = ix+error; y2[i2]=iy; ++i2;
      } else if ( iy>=0. ) {
        x2[i2] = (ix<=xmin)?ix-error:ix+error; 
        y2[i2]=iy; 
        ++i2;
      }
      
      ix += step;
    }
  // Merge arrays
  for ( int i=0; i<i2; ++i ) {
    x1[i+i1] = x2[i2-i-1];
    y1[i+i1] = y2[i2-i-1];
  }
  TGraph* redband = new TGraph( i1+i2, x1, y1 );
  
  redband->SetFillColor(46);
  redband->SetLineColor(46);
  redband->SetLineWidth(3);
// redband->Draw("LF");

  return redband;
//  TGraph* lowband = new TGraph( i2, x2, y2 );
//  std::cout << "Value of (low) redband at limit: " << lowband->Eval( LEPLIMIT, 0, "S" )
//            << std::endl;
                                                                     
}

void sRedBand( TGraph* graph, double error, double xmin)
{
  int nGraph = graph->GetN();
  std::cout<< "Graph has " << nGraph << " points" << std::endl;
  std::cout<< "xmin = " << xmin << std::endl;
  int minP(1);
  while( graph->GetX()[minP++] ) {
    std::cout<< graph->GetX()[minP] << std::endl;
  }
  std::cout << " Min at: " << minP << " with value " << graph->GetX()[minP];

  double* xl1,xl2,xu1,xu2;
  
/*  for( int i =1; i < nGraph; ++i)
  {
    
  }
*/
}


//____________________________________________________________________________________
// Plot blue band (SM Higgs curve)
void blueBand( )
{

  double zerror = 4;
  double xmin = 76;

  int npoints = 31;
  double x[] = { 10.000000, 11.392849, 12.979700, 14.787576, 16.847262, 19.193831, 21.867241, 
                 24.913018, 28.383024, 32.336350, 36.840315, 41.971614, 47.817625, 54.477897,
                 62.065844, 70.710678, 76, 80.559606, 91.780341, 104.563955, 119.128133, 135.720881,
                 154.624747, 176.161637, 200.698289, 228.652526, 260.500365, 296.784127, 
                 338.121669, 385.216905, 438.871795, 500.000000 };

  double y[] = { 20.929260, 18.757168, 16.647426, 14.611732, 12.661571, 10.808107, 9.062193,
                 7.434501, 5.935701, 4.576664, 3.368675, 2.323612, 1.454084, 0.776111,
                 0.300018, 0.042673, 0.0001, 0.020469, 0.251087, 0.750519, 1.538231, 2.633789,
                 4.056692, 5.826546, 7.962673, 10.483595, 13.406320, 16.745357, 20.511276,
                 24.717583, 29.345917, 34.380810 };


  TGraph* smGraph = new TGraph( npoints, x, y );

  if ( npoints > MAXPOINTS ) {
    std::cerr << "FATAL: npoints = " << npoints << " is greater than MAXPOINTS" << std::endl;
    exit(-1);
  }
  double x1[2*MAXPOINTS], y1[2*MAXPOINTS];
  double x2[MAXPOINTS], y2[MAXPOINTS];

  // Find mH at minimum
  int i1=0; // iterator for upper curve
  int i2=0; // iterator for lower curve
  double x0,y0;
  double step = 5;
  smGraph->GetPoint( 0, x0, y0 );
  for ( int i=0; i<100; ++i )
    {
      double ix = x0+i*step;
      double iy = smGraph->Eval( ix, 0, "S" );
      double error = TMath::Log( ix/12. )*3.;
      if ( ix<=xmin-error ) { 
        x1[i1] = ix+error; y1[i1]=iy; ++i1; 
        x2[i2] = ix-error; y2[i2]=iy; ++i2;
      }
      else if ( ix>=xmin+error) { 
        x1[i1] = ix-error; y1[i1]=iy; ++i1; 
        x2[i2] = ix+error; y2[i2]=iy; ++i2;
      } else {//if ( iy>0. ) {
        x2[i2] = (ix<=xmin)?ix-error:ix+error; 
        y2[i2]=iy; 
        ++i2;
      }
      
    }
  // Merge arrays
  for ( int i=0; i<i2; ++i ) {
    x1[i+i1] = x2[i2-i-1];
    y1[i+i1] = y2[i2-i-1];
  }
  if ( doBands ) {
    TGraph* blueBand = new TGraph( i1+i2, x1, y1 );
    blueBand->SetFillColor(7);
    blueBand->SetLineColor(7);
    blueBand->Draw("LF");
    blueBand->Draw("C");
  } else {
    smGraph->SetLineWidth(5);
  }

  smGraph->SetLineColor(4);
  smGraph->Draw("C");
  double chi2limit = smGraph->Eval( LEPLIMIT, 0, "S" );
  std::cout << "Value at limit (" << LEPLIMIT << "): " << chi2limit << std::endl;

  TGraph* lowband = new TGraph( i2, x2, y2 );
  std::cout << "Value of (low) blueband at limit: " << lowband->Eval( LEPLIMIT, 0, "S" )
            << std::endl;

}



//____________________________________________________________________________________
// Plot mH scan: main entry point
int plotScan( TString* filenames,int* styles, double* mins, bool* bands, int nfiles=1, int index = 68,
              TString drawOpt = "C", double mHmin = 85, double mHmax = 140 )
{

  // Styles
  gROOT->SetStyle("Pub");
  gStyle->SetCanvasColor(0);
  gStyle->SetCanvasDefH( 500 );
  gStyle->SetCanvasDefW( 600 );
  

  double chi2min = -0., chi2max = 4;  // Delta-chi2 range
  double threshold = 1e-4;

  for(int i = 0; i<nfiles; i++ )
  {
    std::cout << "Opening " << filenames[i]; 
    TFile* file = new TFile(filenames[i]);
      if ( !(file->IsOpen()) ) {
      std::cerr << "*** Couldn't open " << filenames[i] << std::endl;
      return -1;
    }
    // Retrieve and correct graph
    TString gName("graph1d");
    gName += index;
    TGraph *gChi2[4];
    gChi2[i] = (TGraph*)file->Get( gName );
    if ( !gChi2 ) {
      std::cerr << "*** Couldn't find graph \"" << gName << "\"" << std::endl;
      return -1;
    }
    if(i==0) zeroSuppress( gChi2[i] );
  }

  // Set plot range
  TH2F* range = new TH2F("range","#chi^{2} fit of lightest Higgs mass",
                         2,mHmin,mHmax,2,chi2min,chi2max);
  range->GetXaxis()->SetTitle("M_{h} [GeV]");
  range->GetYaxis()->SetTitle("#Delta#chi^{2}");
  range->Draw();


  // Find preferred value
//  double mHfavour = findMh( gChi2, 0., mHmin );
//  double negError = mHfavour-findMh( gChi2, 1., mHmin );
//  double posError = findMh( gChi2, 1., mHfavour )-mHfavour;
//  std::cout << "Favoured value: " << mHfavour << "+" << posError << "-" << negError << std::endl;

  // Include LEP limit
  TBox* bLepLimit = new TBox( mHmin, chi2min+0.01, LEPLIMIT, chi2max-0.01 );
  bLepLimit->SetFillColor( 5 );
  bLepLimit->Draw();

  // Find value at lep limit
//  double chi2limit = gChi2->Eval( LEPLIMIT, 0, "S" );
//  std::cout << "Value at limit (" << LEPLIMIT << "): " << chi2limit << std::endl;

  // Include upper theoretical limit
  double theoLimit = 130;
  TBox* bTheoLimit = new TBox( theoLimit, chi2min+0.01, mHmax, chi2max-0.01 );
  bTheoLimit->SetFillColor( 42 );
  bTheoLimit->Draw();

  TGraph* rB[4];
  for (int i=0; i<nfiles; i++)
  { 
    if ( bands[i] ) {
      rB[i]=redBand2( gChi2[i], 1.5, mins[i],0.05);
    }
    gChi2[i]->SetLineWidth(3);
    gChi2[i]->SetMarkerStyle(2);
    gChi2[i]->SetLineColor(4);
    gChi2[i]->SetLineStyle(styles[i]);
  }

  for( int i = 0; i<nfiles; ++i){
    if(bands[i]) rB[i]->Draw("LF");
  }
  for( int i = 0; i<nfiles; ++i) gChi2[i]->Draw(drawOpt);

  // Forbidden regions
  TLatex tt;
  tt.SetTextSize(0.7*gStyle->GetTextSize());
  tt.SetTextAlign(12);
  tt.DrawLatex( mHmin+4, chi2min+0.4, "#splitline{LEP}{excluded}" );
  tt.SetTextAlign(22);
  tt.DrawLatex( (theoLimit+mHmax)/2.01, chi2min+0.4, "#splitline{Theoretically}{inaccessible}" );


  
  return 0;
  
}

//____________________________________________________________________________________
// Plot overlay mH scan (SM + mSugra)
int plotOverlay( TString fileName = "output/msugra-noMH-cut20-v5.root", int index = 68, TString drawOpt = "C" )
{

  // Styles
  gROOT->SetStyle("Pub");
  gStyle->SetCanvasColor(0);
  gStyle->SetCanvasDefH( 500 );
  gStyle->SetCanvasDefW( 600 );
  

  double chi2min = -0., chi2max = 4;  // Delta-chi2 range
  double mHmin   = 30, mHmax = 200;
  double threshold = 1e-4;

  TCanvas* myCanvas = new TCanvas("myCanvas","Pseudo-exps contour",10,10,600,600);
  myCanvas->SetTopMargin(0.02);
  myCanvas->SetLogx(1);
  
  // Retrieve and correct graph
  TFile* file = new TFile(fileName);
  if ( !file->IsOpen() ) {
    std::cerr << "*** Couldn't open " << fileName << std::endl;
    return -1;
  }
  TString gName("graph1d");
  gName += index;
  TGraph* gChi2 = file->Get( gName );
  if ( !gChi2 ) {
    std::cerr << "*** Couldn't find graph \"" << gName << "\"" << std::endl;
    return -1;
  }
  zeroSuppress( gChi2 );

  // Set plot range
  TH2F* range = new TH2F("range","#chi^{2} fit of lightest Higgs mass",
                         2,mHmin,mHmax,2,chi2min,chi2max);
  if ( !doPub ) {
    range->GetXaxis()->SetTitle("M_{h} [GeV/c^{2}]");
    range->GetYaxis()->SetTitle("#Delta#chi^{2}");
    range->GetYaxis()->SetTitleOffset(1.1);
  }
  range->GetXaxis()->SetNoExponent();
  range->GetXaxis()->SetMoreLogLabels(1);
  range->Draw();

  // Find preferred value
  double mHfavour = findMh( gChi2, 0., 100. );
  double negError = mHfavour-findMh( gChi2, 1., 100. );
  double posError = findMh( gChi2, 1., mHfavour )-mHfavour;
  std::cout << "Favoured value: " << mHfavour << "+" << posError << "-" << negError << std::endl;

  
  // Include LEP limit
  int LepColor = 5;
  TBox* bLepLimit = new TBox( mHmin, chi2min+0.01, LEPLIMIT, chi2max-0.01 );
  bLepLimit->SetFillColor( LepColor );
  bLepLimit->Draw();

  TLatex tt;
  if (doPub) tt.SetTextFont(133);
  tt.SetTextSize(14);

  // Blue band
  blueBand();

  // Plot red band (1.5 GeV)
  if ( doBands ) {
    redBand2( gChi2, 1.5, mHfavour, 0.005 );
    gChi2->SetLineColor(4);
    gChi2->SetLineWidth(3);
  } else {
    gChi2->SetLineColor(kMagenta);
    gChi2->SetLineWidth(5);
  }


  // Plot scan
  gChi2->SetMarkerStyle(2);
  gChi2->Draw(drawOpt);
  TMultiGraph* mg = new TMultiGraph();

  // Forbidden regions
  tt.SetTextSize(18);
  tt.SetTextAlign(12);
  tt.DrawLatex( mHmin+4, chi2min+0.4, "#splitline{LEP}{excluded}" );
  tt.SetTextAngle(0);


  // Printout
  // hep-ph number
  TLatex tt;
  tt.SetTextFont(83);
  tt.SetTextSize(18);
  tt.SetTextAlign(32);
  //  tt.DrawTextNDC( 0.89, 0.88, "arXiv:0707.3447" );

//   TString name = "mh-scan-overlay";
//   if ( !doPub ) name += "_label";
//   myCanvas->Print(name+".eps");

  
  return 0;
  
}


//________________________________________________________________________________________
// Specific functions for ease of use
plotOverlayCMSSM(TString name="output/msugra-noMH-cut20-v5.root",TString output="plots/redBandOverlayCMSSM.eps") {

  plotOverlay(name,68);

  // Printout
  myCanvas = TVirtualPad::Pad();
  myCanvas->RedrawAxis();
  myCanvas->SaveAs(output);
  
}

plotOverlayNUHM1( TString name="output/msugra-noMH-cut20-v5.root",TString output="plots/redBandOverlayNUHM1.eps") {

  plotOverlay(name,70);

  // Printout
  myCanvas = TVirtualPad::Pad();
  myCanvas->RedrawAxis();
  myCanvas->SaveAs(output);
  
}

plotScanMC4_nuhm1() {
  TString files[] = {"/vols/cms02/samr/MC4/nuhm1-noMH.root"};
  int styles[] = {1};
  double mins[] = {119.5513};
  bool bands[] ={true};

  plotScan(&files,styles,mins,bands,1,71);

  myCanvas = TVirtualPad::Pad();
  myCanvas->RedrawAxis();
  myCanvas->SaveAs("~/public_html/mc4/mh_nuhm1.png");
  myCanvas->SaveAs("/vols/cms02/samr/plots/MC4/mh_nuhm1.png");
}

plotScanMC4_cmssm() {
  TString files[] = {"/vols/cms02/samr/MC4/cmssm-noMH.root"};
  int styles[] = {1};
  double mins[] = {109.59};
  bool bands[] ={true};

  plotScan(&files,styles,mins,bands,1,69);

  myCanvas = TVirtualPad::Pad();
  myCanvas->RedrawAxis();
  myCanvas->SaveAs("~/public_html/mc4/mh_cmssm.png");
  myCanvas->SaveAs("/vols/cms02/samr/plots/MC4/mh_cmssm.png");
}

plotScanMC4_vcmssm() {
  TString files[] = {"/vols/cms02/samr/MC4/vcmssm-noMH.root"};
  int styles[] = {1};
  double mins[] = {110.05};
  bool bands[] ={true};

  plotScan(&files,styles,mins,bands,1,69);

  myCanvas = TVirtualPad::Pad();
  myCanvas->RedrawAxis();
  myCanvas->SaveAs("~/public_html/mc4/mh_vcmssm.png");
  myCanvas->SaveAs("/vols/cms02/samr/plots/MC4/mh_vcmssm.eps");
}

plotScanMC4_msugra() {
  TString files[] = {"/vols/cms02/samr/MC4/msugra-noMH-coann.root"};
  int styles[] = {1};
  double mins[] = {107.9};
  bool bands[] ={true};

  plotScan(&files,styles,mins,bands,1,69);

  myCanvas = TVirtualPad::Pad();
  myCanvas->RedrawAxis();
  myCanvas->SaveAs("~/public_html/mc4/mh_msugra.png");
  myCanvas->SaveAs("/vols/cms02/samr/plots/MC4/mh_msugra.eps");
}

plotScanMC5_msugra() {
  TString files[] = { 
                      "/vols/cms02/samr/MC5/atlas-scaled/msugra-noMH-coann.root"
                     ,"/vols/cms02/samr/MC5/atlas-scaled/msugra-noMH-funnel.root"
                     ,"/vols/cms02/samr/MC5/cms/msugra-noMH-coann.root"
                     ,"/vols/cms02/samr/MC5/cms/msugra-noMH-funnel.root"
                     ,"/vols/cms02/samr/MC5/norm/msugra-noMH-coann.root"
                    };
  int styles[] = { 1,1,2,2,3 };
  double mins[] = { 121.2, 116.8 ,121.2, 110.4, 107.7 };
  bool bands[] = { true, true, false, false, false};
  
  plotScan(&files,styles,mins,bands,5,69);

  // Printout
  myCanvas = TVirtualPad::Pad();
  myCanvas->RedrawAxis();
  myCanvas->SaveAs("~/public_html/mh_msugra.eps");
  myCanvas->SaveAs("/vols/cms02/samr/plots/MC5/mh_msugra.eps");
  
}

plotScanMC5_nuhm1() {
  TString files[] = { 
                      "/vols/cms02/samr/MC5/norm/nuhm1-noMH.root"
                     ,"/vols/cms02/samr/MC5/cms/nuhm1-noMH.root"
                     ,"/vols/cms02/samr/MC5/atlas-scaled/nuhm1-noMH.root"
                    };
  int styles[] = { 3,2,1 };
  double mins[] = {119.5,113.5,116.5};
  bool bands[] = {false,false,true};

  plotScan(&files,styles,mins,bands,3,71);

  // Printout
  myCanvas = TVirtualPad::Pad();
  myCanvas->RedrawAxis();
  myCanvas->SaveAs("~/public_html/mc5/mh_nuhm1.eps");
  myCanvas->SaveAs("/vols/cms02/samr/plots/MC5/mh_nuhm1.eps");
  
}


plotScanMC5_vcmssm() {
TString file[] = { 
                   "/vols/cms02/samr/MC5/atlas-scaled/vcmssm-noMH.root" 
                 , "/vols/cms02/samr/MC5/cms/vcmssm-noMH.root" 
                 , "/vols/cms02/samr/MC5/norm/vcmssm-noMH.root" 
                 };
  int styles[] = { 1,2,3 };
  double mins[] = {115.76,115.76,116.9};
  bool bands[] = {true,false,false};
  plotScan(&file,styles,mins,bands,3,69);

  myCanvas = TVirtualPad::Pad();
  myCanvas->RedrawAxis();
  myCanvas->SaveAs("~/public_html/mc5/mh_vcmssm.eps");
  myCanvas->SaveAs("/vols/cms02/samr/plots/MC5/mh_vcmssm.eps");
}

plotScanMC5_cmssm() {
  
  TString files[] = { "/vols/cms02/samr/MC5/norm/cmssm-noMH.root"
                    , "/vols/cms02/samr/MC5/cms/cmssm-noMH.root" 
                    , "/vols/cms02/samr/MC5/atlas-scaled/cmssm-noMH.root" 
                    };
  int styles[] = { 3,2,1 };
  double mins[] = {109.59,112.63,112};
  bool bands[] = {false,false,true};
  plotScan(&files,styles,mins,bands,3,69);
  myCanvas = TVirtualPad::Pad();
  myCanvas->RedrawAxis();
  
  myCanvas->SaveAs("~/public_html/mc5/mh_cmssm.eps");
  myCanvas->SaveAs("/vols/cms02/samr/plots/MC5/mh_cmssm.eps");
  
}

plotScanJE_cmssm() {
  
  TString files[] = { "/vols/cms02/samr/MC5/JE/cmssm-noMH.root" };
  int styles[] = { 1 };
  double mins[] = {112};
  bool bands[] = {true};
  plotScan(&files,styles,mins,bands,1,69);
  myCanvas = TVirtualPad::Pad();
  myCanvas->RedrawAxis();
  myCanvas->SaveAs("~/public_html/JE/mh_cmssm.eps");
}

plotScanJE_vcmssm() {
TString file[] = { "/vols/cms02/samr/MC5/JE/vcmssm-noMH.root" };
  int styles[] = { 1 };
  double mins[] = {115.76};
  bool bands[] = {true};
  plotScan(&file,styles,mins,bands,1,69);
  myCanvas = TVirtualPad::Pad();
  myCanvas->RedrawAxis();
  myCanvas->SaveAs("~/public_html/JE/mh_vcmssm.eps");
}

plotScanMC6_msugra() {
  TString files[] = { 
                      "/vols/cms03/samr/MC6/Plain/msugra-noMH_funnel.root"
                     ,"/vols/cms03/samr/MC6/Xenon/msugra-noMH_coann.root"
                     ,"/vols/cms03/samr/MC6/Xenon/msugra-noMH_funnel.root"
                    };
  int styles[] = { 3,1,1 };
  double mins[] = { 107.8, 122.4, 116.8 };
  bool bands[] = { false, true, true};
  plotScan(&files,styles,mins,bands,3,139);
  myCanvas = TVirtualPad::Pad();
  myCanvas->RedrawAxis();
  myCanvas->SaveAs("~/public_html/mc6/mh_msugra.eps");
  
}

plotScanMC6_nuhm1() {
  TString files[] = { 
                      "/vols/cms03/samr/MC6/Plain/nuhm1-noMH.root"
                     ,"/vols/cms03/samr/MC6/Xenon/nuhm1-noMH.root"
                    };
  int styles[] = { 3,1 };
  double mins[] = {119.3,117.8};
  bool bands[] = {false,true};
  plotScan(&files,styles,mins,bands,2,141);
  myCanvas = TVirtualPad::Pad();
  myCanvas->RedrawAxis();
  myCanvas->SaveAs("~/public_html/mc6/mh_nuhm1.eps");
  
}


plotScanMC6_vcmssm() {
TString file[] = { 
                   "/vols/cms03/samr/MC6/Plain/vcmssm-noMH.root" 
                 , "/vols/cms03/samr/MC6/Xenon/vcmssm-noMH.root" 
                 };
  int styles[] = { 3,1 };
  double mins[] = {115.76,114.0};
  bool bands[] = {false,true};
  plotScan(&file,styles,mins,bands,2,139);
  myCanvas = TVirtualPad::Pad();
  myCanvas->RedrawAxis();
  myCanvas->SaveAs("~/public_html/mc6/mh_vcmssm.eps");
}

plotScanMC6_cmssm() {
  
  TString files[] = { "/vols/cms03/samr/MC6/Plain/cmssm-noMH.root"
                    , "/vols/cms03/samr/MC6/Xenon/cmssm-noMH.root" 
                    };
  int styles[] = { 3,1 };
  double mins[] = {109.59,115.6};
  bool bands[] = {false,true};
  plotScan(&files,styles,mins,bands,2,139);
  myCanvas = TVirtualPad::Pad();
  myCanvas->RedrawAxis();
  myCanvas->SaveAs("~/public_html/mc6/mh_cmssm.eps");
}
