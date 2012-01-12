//
// Macro to handle 1D histograms:
// - smoothen and store histogram;
// - interpolate with TGraph and store it;
// - later retrieve the TGraph and get mass with errors
//

#include <vector>
#include <iostream>
#include <TH1.h>
#include <TString.h>
#include <TGraph.h>

//________________________________________________________________________________________
// Routines to define name conventions
TString graphName( int& var ) { TString name("graph1d"); TString
retS=name; retS+=var; return retS; }
TString histName( int& var ) { TString name("hist1d"); TString retS=name;
retS+=var; return retS; }

struct ItemLocation
{
    double x1,y1,x2,y2;
    ItemLocation( double x1_, double y1_, double x2_, double y2_ ) :
        x1(x1_), y1(y1_), x2(x2_), y2(y2_) {}
};

void drawLabel(TString& text, ItemLocation* loc, int color = 1, double size = 0.05, int align = 12)
{
    TString ltext = "#color["; ltext+=color; ltext+="]{"; 
        ltext+=text; ltext+="}";
    TLatex Tl;
    Tl.SetNDC(true);
    Tl.SetTextSize(size);
    Tl.DrawLatex(loc->x1, loc->y1, ltext);
    return;
}

//________________________________________________________________________________________
// Zero-suppress histogram (put minimum at 0.05)
void zeroSuppress( TH1* hist, double forced_minimum = 0, double xmin = 0, 
    double xmax = 0, bool supprange = false ) {

   if( !supprange ) { // suppress whole graph
     xmin = hist->GetBinLowEdge(1); 
     int nbins = hist->GetNbinsX();
     xmax = hist->GetBinLowEdge(nbins)+hist->GetBinWidth(nbins); 
   }

   double minimum=0.05;

   // Find minimum
   double ymin = 1e9;
   for ( int i=1; i<=hist->GetNbinsX(); ++i ) // bins 0 and N+1 are under/overflow bins
   {
     double yval = hist->GetBinContent(i);
    if( hist->GetBinLowEdge(i)>xmin && 
        (hist->GetBinLowEdge(i)+hist->GetBinWidth(i))<xmax ) {
        if( yval < ymin ) ymin = yval; 
    }
   }  
   std::cout << "Found minimum: " << ymin << std::endl;

   // Zero-suppress
   for ( int i=1; i<=hist->GetNbinsX(); ++i ) {
     if( hist->GetBinLowEdge(i)>xmin && 
         (hist->GetBinLowEdge(i)+hist->GetBinWidth(i))<xmax ) {
      hist->SetBinContent(i,hist->GetBinContent(i)-ymin+minimum+forced_minimum);
     }
   }

}

//________________________________________________________________________________________
// Smoothened 1D histogram and create a TGraph
TGraph* getSpline( TH1* hist, int& nSmooth, double xmin=0., double xmax=0. , double f_min = 0, bool supprange = false) {

  // Set an axis range, if required (i.e., xmin != xmax)
  bool doRange = false;
  if ( fabs(xmin)>1e-100 && (fabs(xmin-xmax)/fabs(xmin) > 1e-10) ) {
    hist->GetXaxis()->SetRangeUser(xmin,xmax);
    doRange = true;
  }

  // Smoothen and zero suppress histogram before drawing spline
  hist->Smooth(nSmooth,"R");
  zeroSuppress(hist,f_min,xmin,xmax, supprange);

  if ( doRange ) hist->GetXaxis()->SetRange(0,0);

  // Get graph
  int nbins = hist->GetNbinsX();
  TGraph* graph = new TGraph(nbins);
  // Loop over histogram contents (NB: bin 0 is underflow bin...)
  for ( int ibin=1; ibin<=nbins; ++ibin ) {
    graph->SetPoint(ibin-1,hist->GetBinCenter(ibin),hist->GetBinContent(ibin));
  }
  
  return graph;

}


//________________________________________________________________________________________
// Draw overlay of histogram and TGraph
void drawOverlay( TH1F* hist, TGraph* graph, int col=2) {

  // Set range
  hist->SetMinimum(0.);
  hist->SetMaximum(9.);

  // Draw histogram and graph
  hist->Draw();
  graph->SetLineColor(col);
  graph->Draw("C");

  // Draw line at 0
  TLine* zeroline = new TLine(hist->GetXaxis()->GetXmin(),0,hist->GetXaxis()->GetXmax(),0);
  zeroline->Draw("same");

}

//________________________________________________________________________________________
// Main routine to get and draw the interpolated graph
int spline( TString& fileName, int& var1, int& var2, 
            bool& store = false, int& nSmooth = 0, int& col = 2,
            double& xmin1 = 0, double& xmax1 = 0,
            double& xmin2 = 0, double& xmax2 = 0, 
            double f_min1 = 0., double& f_min2 = 0., bool supprange = false) 
{

  // Check if file already opened
  TFile* f = gROOT->GetListOfFiles()->FindObject(fileName);
  if ( f==NULL ) f = TFile::Open(fileName,"UPDATE");

  TString directory("plots_");
  directory += var1; directory += "_"; directory += var2;
  directory += "_1s";
  if ( !f->GetDirectory( directory ) ) {
    std::cerr << "Failed to open directory " << directory << std::endl;
    return -1;
  }

  // Retrieve histograms
  TH1F* hist1 = f->Get(directory+"/h1");
  if ( !hist1 ) {
    std::cerr << "Couldn't retrieve " << directory+"/h1" << std::endl;
    return -1;
  }
  TH1F* hist2 = f->Get(directory+"/h2");
  if ( !hist1 ) {
    std::cerr << "Couldn't retrieve " << directory+"/h2" << std::endl;
    return -1;
  } 

  TGraph* g1 = getSpline( hist1, nSmooth, xmin1, xmax1 , f_min1, supprange );
  TGraph* g2 = getSpline( hist2, nSmooth, xmin2, xmax2 , f_min2, supprange );

  // Plot result
  TCanvas* mycanvas = new TCanvas("mycanvas","Smoothing",10,10,800,400);
  mycanvas->Divide(2,1);
  mycanvas->Draw();

  mycanvas->cd(1);
  drawOverlay(hist1,g1,col);

  mycanvas->cd(2);
  drawOverlay(hist2,g2,col);

  // Store graphs and histograms to file, at root level
  if ( store ) {
    g1->Write(graphName(var1),TObject::kOverwrite);
    g2->Write(graphName(var2),TObject::kOverwrite);
    hist1->Write(histName(var1),TObject::kOverwrite);
    hist2->Write(histName(var2),TObject::kOverwrite);    
  }

  return 0;

}


//________________________________________________________________________________________
// Get mass and errors for given particle
// - step gives the precision of the output (in GeV)
int getMass( TString& fileName, int& var, 
             double& massOut, double* error68, double* error95,
             double step=1.0, bool verbose=false ) {

  // Check if file already opened
  TFile* f = gROOT->GetListOfFiles()->FindObject(fileName);
  if ( f==NULL ) f = TFile::Open(fileName);

  TGraph* graph = (TGraph*)f->Get(graphName(var));

  if ( !graph ) {
    std::cerr << "*** Couldn't find graph " << graphName(var) << std::endl;
    return -1;
  }

  // Scan graph and find all values
  double massMin = graph->GetX()[0];
  double massMax = graph->GetX()[graph->GetN()-1];

  double curMass = massMin;
  double curChi2 = graph->Eval(curMass);

  double mass = massMin;

  // Get central value
  while ( curMass<=massMax ) {
    double chi2 = graph->Eval(curMass);
    if ( chi2<curChi2 ) {
      mass = curMass;
      curChi2=chi2;
    }
    curMass += step;
  }

  // Get negative error
  double low95=massMin,low68=massMin;
  curMass = massMin;
  double curChi2 = graph->Eval(curMass);
  while ( curMass<=mass ) {
    double chi2 = graph->Eval(curMass);
    // 95 CL <=> Dchi2 = 4
    if ( fabs(chi2-4) < fabs( graph->Eval(low95)-4 ) ) {
      low95 = curMass;
    }
    // 68 CL <=> Dchi2 = 1
    if ( fabs(chi2-1) < fabs( graph->Eval(low68)-1 ) ) {
      low68 = curMass;
    }
    curMass += step;
  }

  // Get positive error
  double high95=massMax,high68=massMax;
  curMass = massMax;
  double curChi2 = graph->Eval(curMass);
  while ( curMass>=mass ) {
    double chi2 = graph->Eval(curMass);
    // 95 CL <=> Dchi2 = 4
    if ( fabs(chi2-4) < fabs( graph->Eval(high95)-4 ) ) {
      high95 = curMass;
    }
    // 68 CL <=> Dchi2 = 1
    if ( fabs(chi2-1) < fabs( graph->Eval(high68)-1 ) ) {
      high68 = curMass;
    }
    curMass -= step;
  }

  // Convert range to error
  low95 = mass-low95;
  low68 = mass-low68;
  high95 = high95-mass;
  high68 = high68-mass;

  // Return values
  massOut = mass;
  error68[0] = low68;
  error95[0] = low95;
  error68[1] = high68;
  error95[1] = high95;

  // Turn on for verbosity
  if ( verbose ) {
    graph->Draw("AC");
    std::cout << "Mass(" << var << ") = " << mass;
    std::cout << "+" << high68 << "(" << high95 << ")";
    std::cout << "-" << low68 << "(" << low95 << ")" << std::endl;
  }

  return 0;

}


//________________________________________________________________________________________
// Plot one spline
TGraph* plotSpline( TString& var, TString& title , bool drawAxis = true) {

  TString strHist = "hist1d";
  strHist+=var;
  std::cout<<strHist<< " <- looking" << std::endl;
  TH1F* hist = gDirectory->Get(strHist);
  hist->GetXaxis()->SetTitle(title);
  hist->GetXaxis()->SetTitleOffset(1.05);
  hist->GetYaxis()->SetTitleOffset(1);
  if(drawAxis) hist->Draw("AXIS");
  else hist->Draw("same");

  TGraph* graph = gDirectory->Get("graph1d"+var);

  gDirectory->Get("graph1d"+var)->Draw("C");

  // Draw line at 0
  TLine* zeroline = new TLine(hist->GetXaxis()->GetXmin(),0,hist->GetXaxis()->GetXmax(),0);
  zeroline->Draw("same");

  return graph; // Just in case we need it

}

void DrawMCLogo()
{

    TImage *img = TImage::Open("/vols/cms01/samr/mastercode/plotting/mastercode.eps");
    img->SetImageQuality(100);

    if (!img) {
        printf("Could not create the Logo... exit\n");
        return;
    }
    TPad *l = new TPad("l","l",0.5,0.5,0.789444,0.65);
    //l->SetFixedAspectRatio();
    l->Draw();
    l->cd();
    img->Draw();

}

TImage * findImage(const char * imageName) 
{ 
  // looks for the image in macropath
  TString macroPath(gROOT->GetMacroPath()); // look for the image in here
  Ssiz_t curIndex(0);
  TImage *img(0);
  while(1) {
     Ssiz_t pathStart = curIndex;
     curIndex = macroPath.Index(":",curIndex);
     Ssiz_t pathEnd = (curIndex==-1)?macroPath.Length():curIndex;
     TString path(macroPath(pathStart,pathEnd-pathStart));
     
     gSystem->ExpandPathName(path);
     const char* fullName = Form("%s/%s", path.Data(), imageName);
     std::cout << fullName << std::endl;

     Bool_t fileFound = ! gSystem->AccessPathName(fullName);

     if(fileFound) {
        img = TImage::Open(fullName);
        break;
     }
     if(curIndex==-1) break;
     curIndex++;
  }
  return img;
}

void plotNSplines( TString* files, TString* vars, int* style, int nfiles, TString& label,
                   int* color, TString& fileout, double xmin, double xmax, 
                   bool logx=false, bool logy=false, double chi2max=9.,
                   bool drawLegend=false, TString* legendEntry, double lx1=0.65,
                   double ly1=0.18, double lx2=0.85, double ly2=0.33) {
  int* width = new int[nfiles];
  for(int i=0; i<nfiles; ++i) {
    width[i] = 3;
  }
  plotNSplines(files,vars,style,width,nfiles,label,color,fileout,xmin,xmax,logx,
    logy,chi2max,drawLegend,legendEntry,lx1,ly1,lx2,ly2);
}

void plotNSplines( TString* files, TString* vars, int* style, int* width, int nfiles, TString& label,
                   int* color, TString& fileout, double xmin, double xmax, 
                   bool logx=false, bool logy=false, double chi2max=9.,
                   bool drawLegend=false, TString* legendEntry, double lx1=0.65,
                   double ly1=0.18, double lx2=0.85, double ly2=0.33, bool logo = false, ItemLocation *loc = NULL, TString label_m = "") 
{
  TCanvas *c1 = new TCanvas("c1", "#Delta#chi^{2}",1);
  gROOT->SetStyle("Pub");
  gStyle->SetCanvasColor(0);


  TMultiGraph* mg = new TMultiGraph();
  TLegend* lg = new TLegend(lx1,ly1,lx2,ly2);
  lg->SetBorderSize(0);
  lg->SetFillStyle(0);
  for(int f = 0; f<nfiles ; ++f )// for each model
  {
      TFile* f1 = new TFile(files[f]);
      
      TGraph* graphTemp = plotSpline(vars[f],label);

      graphTemp->SetLineWidth(width[f]);
      graphTemp->SetLineColor(color[f]);
      graphTemp->SetLineStyle(style[f]);
      mg->Add(graphTemp,"c");
      if( drawLegend ) lg->AddEntry(graphTemp,legendEntry[f],"L");

      f1->Close();
      f1 = NULL;
      graphTemp = NULL;
  }


  mg->Draw("a");
  if( loc ) drawLabel(label_m,loc);
  gPad->SetLogx(logx);
  if( drawLegend ) lg->Draw();
  if( logo ) DrawMCLogo();
  mg->GetXaxis()->SetRangeUser(xmin,xmax);
  mg->GetXaxis()->SetTitle(label);
  mg->GetYaxis()->SetRangeUser(0,chi2max);
  mg->GetYaxis()->SetTitle("#Delta#chi^{2}");

  c1->Print(fileout);
  c1->Close();
}

//________________________________________________________________________________________
// Plot all masses (CMSSM or NUHM1). See allMasses***() methods above
void plotMasses( TString filename, size_t nindex, int* indices, 
                 TString* labels, int* colors, double xmax,
                 TString plotName = "CMSSM" ) {

  gROOT->SetStyle("Pub");
  gStyle->SetCanvasColor(0);

  // Canvas for masses
  TCanvas* canvas = new TCanvas("canvas","Mass spectrum",200,10,700,60*nindex);
  double xmin=150;// xmax= 1500;
  double ymin=2.5,  ymax = nindex+1;
  canvas->Range(-xmin,-ymin,xmax+xmin,ymax+ymin);
  canvas->Draw();

  // Frame
  TFrame* frame = new TFrame(0.,0.,xmax,ymax);
  frame->SetBorderMode(0);
  frame->SetFillColor(0);
  frame->Draw();
  
  // Axes
  TGaxis* ax = new TGaxis( 0., 0., xmax, 0., 0., xmax );
  ax->SetTitleOffset(1.);
  TGaxis* axTop = ax->Clone();
  axTop->SetY1(ymax);
  axTop->SetY2(ymax);
  axTop->SetOption("-");
  axTop->Draw();
  ax->SetTitle("mass [GeV/c^{2}]");
  ax->Draw();

  // Draw masses
  TLatex* t = new TLatex();
  t->SetTextAlign(22);
  t->SetTextSize(0.7*gStyle->GetTextSize());
  t->SetNDC(0);
  double xerr = 0.2;
  for ( size_t i=0; i<nindex; ++i ) {
    double mass,error95[2],error68[2];
    getMass(filename,indices[i],mass,error68,error95);
    // 68% CL
    TGraphAsymmErrors* graph68 = new TGraphAsymmErrors(1);
    graph68->SetPoint(0,mass,nindex-i);
    graph68->SetPointError(0,error68[0],error68[1],xerr,xerr);
    graph68->SetLineColor(colors[i]);
    graph68->SetLineWidth(2);
    // 95% CL
    TGraphAsymmErrors* graph95 = graph68->Clone();
    graph95->SetPointError(0,error95[0],error95[1],xerr,xerr);
    graph95->SetLineStyle(3);

    graph95->Draw();
    graph68->Draw();

    t->SetTextColor(colors[i]);
    t->DrawLatex( -xmin/2.0, nindex-i, labels[i] );
  }

  // Add plot label
  t->SetTextAlign(33);
  t->SetTextColor(1);
  t->SetTextSize( t->GetTextSize()*1.3 );
  t->DrawLatex(xmax*0.9,nindex,plotName);
 
  // Save it
  if (plotName.Length()>0) {
    canvas->SaveAs("plots/masses"+plotName+".eps");
    canvas->SaveAs("~/public_html/splines/masses"+plotName+".png");
  }
}

void plotMassesLandscape( TString filename, size_t nindex, int* indices, 
                 TString* labels, int* colors, double ymax,
                 TString plotName = "CMSSM", double LatexAdjust=2.0 ) {

  gROOT->SetStyle("Pub");
  gStyle->SetCanvasColor(0);

  // Canvas for masses
  TCanvas* canvas = new TCanvas("canvas","Mass spectrum",10,220,60*nindex,740);
  double xmin=2.5, xmax = nindex+1;
  double ymin=150;
  canvas->Range(-xmin,-ymin,xmax+xmin,ymax+ymin);
  canvas->Draw();

  // Frame
  TFrame* frame = new TFrame(0.,9.,xmax,ymax);
  frame->SetBorderMode(0);
  frame->SetFillColor(0);
  frame->Draw();
  
  // Axes
  TGaxis* ax = new TGaxis( 0., 9., 0., ymax, 0., ymax );
  ax->SetTitleOffset(1.);
  TGaxis* axTop = ax->Clone();
  axTop->SetX1(xmax);
  axTop->SetX2(xmax);
  axTop->SetOption("+L");
  axTop->Draw();
  ax->SetTitle("mass [GeV/c^{2}]");
  ax->Draw();

  // Draw masses
  TLatex* t = new TLatex();
  t->SetTextAlign(22);
  t->SetTextSize(0.7*gStyle->GetTextSize());
  t->SetNDC(0);
  double xerr = 0.2;
  for ( size_t i=0; i<nindex; ++i ) {
    double mass,error95[2],error68[2];
    getMass(filename,indices[i],mass,error68,error95);
    // 68% CL
    TGraphAsymmErrors* graph68 = new TGraphAsymmErrors(1);
    graph68->SetPoint(0,i+1,mass);
    graph68->SetPointError(0,xerr,xerr,error68[0],error68[1]);
    graph68->SetLineColor(colors[i]);
    graph68->SetLineWidth(2);
    // 95% CL
    TGraphAsymmErrors* graph95 = graph68->Clone();
    graph95->SetPointError(0,xerr,xerr,error95[0],error95[1]);
    graph95->SetLineStyle(3);

    graph95->Draw();
    graph68->Draw();

    t->SetTextColor(colors[i]);
    t->DrawLatex( i+1, -ymin/LatexAdjust,  labels[i] );
  }

  // Add plot label
  t->SetTextAlign(11);
  t->SetTextColor(1);
  t->SetTextSize( t->GetTextSize()*1.3 );
  t->DrawLatex(1,ymax*0.9,plotName);
 
  // Save it
  if (plotName.Length()>0) {
    canvas->SaveAs("plots/masses"+plotName+"_landscape.eps");
    canvas->SaveAs("~/public_html/masses"+plotName+"_landscape.png");
  }
}
