#include <utility>
#include <vector>
#include <iomanip>
// Global variables
//
int kMinPoints = 35;  // Min. number of points for a graph to get displayed:
                      //def=35

struct ItemLocation
{
    double x1,y1,x2,y2;
    ItemLocation( double x1_, double y1_, double x2_, double y2_ ) :
        x1(x1_), y1(y1_), x2(x2_), y2(y2_) {}
};

//________________________________________________________________________________
// Colorful palette
void colorPalette(int colorful = 0) {
    //gStyle->SetPalette(1,0);
    if ( colorful ) 
    { 
        const Int_t NRGBs = 5;
        const Int_t NCont = 255;

        Double_t stops[NRGBs] = { 0.00, 0.34, 0.61, 0.84, 1.00 };

        if( colorful == 1 )
        {
            Double_t red[NRGBs] = {0.00, 0.40, 0.75, 0.90, 1.00};
            Double_t green[NRGBs] = {0.00, 0.40, 0.75, 0.90, 1.00};
            Double_t blue[NRGBs] = {0.00, 0.40, 0.75, 0.90, 1.00};
            TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue,
                    NCont);
        }
        else if( colorful == 2 || colorful == 4 || 
            colorful == 5 )
        {
            Double_t red[NRGBs]   = { 0.00, 0.00, 0.87, 1.00, 0.51 };
            Double_t green[NRGBs] = { 0.00, 0.81, 1.00, 0.20, 0.00 };
            Double_t blue[NRGBs]  = { 0.51, 1.00, 0.12, 0.00, 0.00 };        
            TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue,
                    NCont);
        }
        else if( colorful == 3 )
        {
            Double_t red[NRGBs]   = { 0.00, 0.00, 0.87, 1.00, 0.51 };
            Double_t green[NRGBs] = { 0.00, 0.81, 1.00, 0.20, 0.00 };
            Double_t blue[NRGBs]  = { 0.51, 1.00, 0.12, 0.00, 0.00 };        
            TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue,
                    NCont);
        }
        else 
        {
            Double_t red[NRGBs] = {0.00, 0.40, 0.75, 0.90, 1.00};
            Double_t green[NRGBs] = {0.00, 0.40, 0.75, 0.90, 1.00};
            Double_t blue[NRGBs] = {0.00, 0.40, 0.75, 0.90, 1.00};
            TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue,
                    NCont);
        }
        gStyle->SetNumberContours(NCont);
    } 
    else 
    {
        // Set gray-scale gradient
        const Int_t NRGBs = 2;
        Double_t Stops[NRGBs] = { 0., 0.9 };
        Double_t Gray[NRGBs] = { 0.9, 0.0 };
        int gIndex = TColor::CreateGradientColorTable(NRGBs, Stops, Gray, Gray,
            Gray, 40);
    }
} 

void drawPoint( double X, double Y, int style = 29, int size = 2.0, 
    int color = 8 )
{
    TGraph* point = new TGraph(1);
    point->SetPoint(0,X,Y);
    point->SetMarkerStyle(style);
    point->SetMarkerColor(color);
    point->SetMarkerSize(size);
    point->Draw("P");
}

//________________________________________________________________________________
// Draw contours "by hand"
void contoursByHand( TString filename, TString var1, TString var2,
                     double xmin = 0., double xmax = 5000.,
                     double ymin = 0., double ymax = 5000., 
                     double minChi2 = -1., TString outputFile = "" )
{
  TCanvas* myCanvas = new TCanvas("myCanvas","Pseudo-exps contour",600,10,700,600);
  myCanvas->SetFillColor(0);
  myCanvas->SetBorderMode(0);
  myCanvas->SetRightMargin(0.15);
  myCanvas->SetLeftMargin(0.15);
  myCanvas->Draw();

  gStyle->SetMarkerStyle(1);

  // Branches
  TFile* f = new TFile(filename);
  TTree* tree = (TTree*)f->Get("chi2tree");
  Double_t vars[50];
//  int varSize = tree->GetLeaf("vars")->GetLenType();
//  vars = new Double_t[varSize];
  tree->SetBranchAddress( "vars", &vars[0] );

  // Get best chi2
  int entry = 0;
  if ( minChi2 < 0. ) 
  {
    double minChi2 = 1e9;
    while ( tree->GetEntry(entry++) )
       if ( vars[0]<minChi2 ) minChi2 = vars[0];
  }
  std::cout << "Minimum chi^2: " << minChi2 << std::endl;

  double chi2cuts[3] = { 9.2, 6.0, 2.27 };
  char cut[256];
  int colors[] = { kGreen, kRed, kBlue };

  // First run with loose cut
  tree->SetMarkerColor( kBlack );
  sprintf(cut,"%4s > %7.3g && %4s < %7.3g &&  %4s > %7.3g && %4s < %7.3g",
          var1.Data(),xmin,var1.Data(),xmax,var2.Data(),ymin,var2.Data(),ymax);
  TString toPlot = var1 + ":" + var2;
  std::cout << cut << ": " << tree->Draw(toPlot,cut) << std::endl;

  // Apply cuts
  for ( int i=0; i<3; ++i ) {
     tree->SetMarkerColor(colors[i]); 
     sprintf(cut,"vars[0]-%6.4g < %6.4g",minChi2,chi2cuts[i]);
     std::cout << cut << ": " << tree->Draw(toPlot,cut,"same") << std::endl;
  }

  if ( outputFile.Length()>0 ) myCanvas->SaveAs(outputFile);
} 




//________________________________________________________________________________
// Print-out graph content to be used later on
void dumpGraph( TGraph* graph ) {

  std::cout << std::endl << "  double x[" << graph->GetN() << "] = { ";
  for ( int i=0; i<graph->GetN(); ++i ) {
    std::cout << graph->GetX()[i];
    if ( i < graph->GetN()-1) std::cout << ",";
  }
  std::cout << " };" << std::endl;
  std::cout << "  double y[" << graph->GetN() << "] = { ";
  for ( int i=0; i<graph->GetN(); ++i ) {
    std::cout << graph->GetY()[i];
    if ( i < graph->GetN()-1) std::cout << ",";
  }
  std::cout << " };" << std::endl;

}

//________________________________________________________________________________________
TGraph* plotGraphs( TString& graphName, int color, int style, 
                    double distmin, double xnorm, double ynorm, 
                    double minPoints = kMinPoints) 
{
  TKey* key;
  Long_t igraph = 0;
  TGraph* graph;
  TGraph* returnGraph;
  while ( key = gDirectory->FindKey( graphName+igraph ) ){
    graph = (TGraph*)key->ReadObj();
    graph->SetLineWidth(3);

    Double_t tmpx, tmpy, tmpx1, tmpy1, tmpx2, tmpy2;
    Double_t xsmooth[2000], ysmooth[2000];

    Double_t dist = 0.;
    Int_t j =0;
    
    if ( graph->GetN()>minPoints ){
       graph->GetPoint(0,tmpx,tmpy);
       xsmooth[j]=tmpx;
       ysmooth[j]=tmpy;
       for (Int_t i=1;i<graph->GetN();i++){
          graph->GetPoint(i,tmpx,tmpy);
          dist = sqrt(pow((tmpx-xsmooth[j])/xnorm,2)+pow((tmpy-ysmooth[j])/ynorm,2));
          if (dist < distmin) continue;
          j++;
          xsmooth[j]=tmpx;
          ysmooth[j]=tmpy;
       }
       j++;
       graph->GetPoint(graph->GetN()-1,tmpx,tmpy);
       xsmooth[j]=tmpx;
       ysmooth[j]=tmpy;     
       j++;

       double xshort[2000], yshort[2000];
       double dist1 = 0;
       double dist2 = 1;
       Int_t pp =0;
       xshort[pp] = xsmooth[0];
       yshort[pp] = ysmooth[0];
       pp++;
       xshort[pp] = xsmooth[1];
       yshort[pp] = ysmooth[1];
       pp++;
       for (Int_t k=2;k<j-1;k++){ 
          dist1 = sqrt(pow((xsmooth[k]-xsmooth[k-1])/xnorm,2)+pow((ysmooth[k]-ysmooth[k-1])/ynorm,2));
          dist2 = sqrt(pow((xsmooth[k]-xsmooth[k-2])/xnorm,2)+pow((ysmooth[k]-ysmooth[k-2])/ynorm,2));
          if ( !(dist2<dist1) ) {
             xshort[pp] = xsmooth[k];
             yshort[pp] = ysmooth[k];
             pp++;
          } else {
             cout << "Skipping point " << k << " as too close to " << k-2 
                  << " , dist1 = " << dist1 << " dist2 = " << dist2 <<endl;
          }
       }
       xshort[pp] = xsmooth[j-1];
       yshort[pp] = ysmooth[j-1];
       pp++;

       std::cout<<graphName<<std::endl;
       double xmax(1e9),ymax(1e9);
       if( graphName.Contains("95") ) {
        xmax = 200;
        ymax = 450;
       } else if( graphName.Contains("68") ) {
        xmax = 200;
        ymax = 320;
       }

       double xsam[2000], ysam[2000];
       Int_t psam = 0;
       for( int H = 0; H<pp; ++H) {
         if(hack) {
           if( xshort[H] < xmax && yshort[H] < ymax ) {
              xsam[psam]=xshort[H];
              ysam[psam]=yshort[H];
              psam++;
           }
         } else {
            xsam[H]=xshort[H];
            ysam[H]=yshort[H];
         }
       }
       if(!hack) psam = pp; 
       
       //TGraph *smoothGraph = new TGraph(pp,xshort,yshort);
       TGraph *smoothGraph = new TGraph(psam,xsam,ysam);
       std::cout << "*** Smoothed graph has " << smoothGraph->GetN() << " points ***" << std::endl;

       graph->SetMarkerStyle(23);
       graph->SetMarkerSize(1.); 

       smoothGraph->SetLineColor(color);
       smoothGraph->SetLineWidth(3);
       smoothGraph->SetLineStyle(style);


       smoothGraph->Draw("C");
       returnGraph = smoothGraph;

       std::cout << "*** Drawing, Graph has " << graph->GetN() << " points ***" << std::endl;
    } else if ( graph->GetN() > 10 ) {
       std::cout << "Skipping, Graph has only " << graph->GetN() << " points " << std::endl;
    }

    ++igraph;
  }

  return returnGraph;
}



//________________________________________________________________________________________
// Plot all graphs corresponding to graphName, with given color
TGraph* plotGraphsOld( TString& graphName, int& color , int linestyle = 1 ) {
  
  TKey* key;
  Long_t igraph = 0;
  TGraph* graph;

  while ( key = gDirectory->FindKey( graphName+igraph ) ){
     graph = (TGraph*)key->ReadObj();
     graph->SetLineColor(color);
     graph->SetLineWidth(3);
     graph->SetLineStyle(linestyle);
     if ( graph->GetN()>kMinPoints ){
        graph->Draw("L");
     }
     ++igraph;
  }

  return graph;

}

void drawLabel(TString& text, ItemLocation& loc, int color = 1, double size = 0.05, int align = 12)
{
    TString ltext = "#color["; ltext+=color; ltext+="]{"; 
        ltext+=text; ltext+="}";
    TLatex Tl;
    Tl.SetNDC(true);
    Tl.SetTextSize(size);
    Tl.DrawLatex(loc.x1, loc.y1, ltext);
    return;
}


//________________________________________________________________________________________
// Plot an MCMC result in the form of 2D contours
int plotMCMC( TString& fileName,    // input file name, 
              TString& var1name,    // variable1 name
              TString& var2name,    // variable2 name
              TString& plotName,    // ending for plot file name
              int& var1, int& var2, // variables to plot
              double distance = 0.05, // Smoothing parameter
              bool rawGraphs = false, // Turn off smoothing?
              bool logx = false,
              bool logy = false,
              int colorful = 0, // use colorful palette
              double min = 0.,
              double max = 25.,    //set maximum for dchi2 plot
              int steps = 0.,
              int var_contrib = 0,
              TString label = "",
              TString zaxis = "",
              TString dir_e = "",
              int lcolor = 0,
              double lx = 0.17,
              double ly = 0.8
              )  
{
    gROOT->SetStyle("Pub");
    gStyle->SetCanvasColor(0);
    gStyle->SetPadRightMargin(0.18);
    colorPalette(colorful);

    TFile* f = new TFile(fileName);

    TString directory("plots_");
    directory += var1; directory += "_"; directory += var2;
    directory += "_"; directory += colorful;
    if( var_contrib > 0 )
    {
        directory += "-";
        directory += var_contrib;
    }
    directory += dir_e;
    if ( !f->cd( directory ) ) 
    {
        std::cerr << "Failed to open directory " << directory << std::endl;
        return -1;
    }

    // Draw histogram (range only)
    TH2F* hCont = gDirectory->Get("hCont");
    hCont->SetMinimum(min);
    if( max != 0. )
    {
        hCont->SetMaximum(max);
    }
    else
    {
        hCont->SetMaximum(hCont->GetMaximum());
    }

    if( steps )
    {
        hCont->SetContour(steps);
    }

    hCont->Draw("colz");

    TCanvas* gCanvas = TVirtualPad::Pad();
    //gCanvas->SetGrayscale();

    if (logx) gCanvas->SetLogx(1);
    else gCanvas->SetLogx(0);
    if (logy) gCanvas->SetLogy(1);
    else  gCanvas->SetLogy(0);

    // Set axis titles
    hCont->GetXaxis()->SetTitle(var1name);
    hCont->GetYaxis()->SetTitle(var2name);
    hCont->GetYaxis()->SetTitleOffset(1.1);
    if( zaxis == "" )
    {
        if (colorful == 1) 
        {
            hCont->GetZaxis()->SetTitle("#Delta#chi^{2}");
        }
        else if( colorful == 2 )
        {
            hCont->GetZaxis()->SetTitle("p(#chi^{2},N_{DoF})");
        }
        else if( colorful == 3 )
        {
            hCont->GetZaxis()->SetTitle("#chi^{2}_{obs}");
        } 
        else if( colorful == 4 )
        {
            hCont->GetZaxis()->SetTitle("F");
        } 
        else hCont->GetZaxis()->SetTitle("1-CL");
    }
    else
    {
        hCont->GetZaxis()->SetTitle(zaxis);
    }
    hCont->GetZaxis()->SetTitleOffset(1.2);


    // Plot graphs
    double xrange = hCont->GetXaxis()->GetXmax() - hCont->GetXaxis()->GetXmin();
    double yrange = hCont->GetYaxis()->GetXmax() - hCont->GetYaxis()->GetXmin();

    if (rawGraphs) 
    {
        Int_t col68 = (colorful)?kBlue-1:kRed-1;
        Int_t col95 = (colorful)?kRed-1:kBlue-1;
        if(colorful<=1) 
        {
            plotGraphsOld( "graph68_", col68 );
            plotGraphsOld( "graph95_", col95 );
        }
    } 
    else 
    {
        plotGraphs( "graph68_", kBlue-1, 1, distance, xrange, yrange );
        plotGraphs( "graph95_", kRed-1, 1, distance, xrange, yrange );
    }

    ItemLocation loc(lx,ly,1.,1.);
    drawLabel( label, loc, lcolor );


    if (plotName.Length()>0) 
    { 
        gCanvas->SaveAs("~/public_html/"+plotName+".eps");
    }
    // Reset canvas
    gCanvas->SetLogx(0);
    gCanvas->SetLogy(0);
}

//________________________________________________________________________________________
int overLay( TString* f, TString* vars, TString* legends, int nfiles, 
             int* var1, int* var2, double distance,
             bool rawGraphs = false, TString contour = "95" ) {

  gROOT->SetStyle("Pub");
  gStyle->SetCanvasColor(0);
  gStyle->SetPadRightMargin(0.18);
  TLegend* legend = new TLegend(0.17,0.7,0.5,0.89,"","brNDC");
  legend->SetBorderSize(0);
  legend->SetFillColor(0);

  TString graphName("graph");
  graphName += contour;
  graphName += "_";
  
  for ( int i=0; i<nfiles; ++i ) {
    TFile* file = new TFile(f[i]);
    TString directory("plots_");
    directory += var1; directory += "_"; directory += var2;
    file->cd( directory );
    if (!i) {
      TH2F* hCont = gDirectory->Get("hCont");
      hCont->Reset("ICE");
      hCont->GetYaxis()->SetTitleOffset(1.5);
      hCont->GetYaxis()->SetTitle("");
      hCont->GetXaxis()->SetTitle("");

      // Resize M0
      if ( var2 == 1 ) {
        hCont->GetYaxis()->SetRangeUser(-100.,1200.);
      } else if ( var1 == 1 ) {
        hCont->GetXaxis()->SetRangeUser(-100.,1200.);
      }

      hCont->Draw();
    }
    double xrange = hCont->GetXaxis()->GetXmax() - hCont->GetXaxis()->GetXmin();
    double yrange = hCont->GetYaxis()->GetXmax() - hCont->GetYaxis()->GetXmin();

    TGraph *graph;
    if (rawGraphs) graph = plotGraphsOld( graphName, kRed-6+3*i);
    else graph = plotGraphs( graphName, kRed, i+1, distance, xrange, yrange );
    legend->AddEntry(graph,legends[i],"l");
  }

  //CHF
  legend->SetTextSize(0.03);
  legend->Draw();

}

void overLays( TString* f, TString* vars, int* style, int nfiles, 
             int var1, int var2, double distance,
             bool rawGraphs = false, TString* contour, 
             int* color, int ncont, bool hack=false, 
             double minPoints = kMinPoints ) {

  gROOT->SetStyle("Pub");
  gStyle->SetCanvasColor(0);
  gStyle->SetPadRightMargin(0.18);

  for ( int i=0; i<nfiles; ++i ) {
    TFile* file = new TFile(f[i]);
    TString directory("plots_");
    directory += var1; directory += "_"; directory += var2;
    file->cd( directory );

    for (int j = 0; j<ncont; ++j)
    {
      TString graphName("graph");
      graphName += contour[j];
      graphName += "_";
      if (!i && !j) { //on first run
        TH2F* hCont = gDirectory->Get("hCont");
        hCont->Reset("ICE");
        hCont->GetYaxis()->SetTitleOffset(1.5);
        hCont->GetYaxis()->SetTitle(vars[1]);
        hCont->GetXaxis()->SetTitle(vars[0]);

        // Resize M0
        if ( var2 == 1 ) {
          hCont->GetYaxis()->SetRangeUser(-100.,1200.);
        } else if ( var1 == 1 ) {
          hCont->GetXaxis()->SetRangeUser(-100.,1200.);
        }

        hCont->Draw();
      }
      double xrange = hCont->GetXaxis()->GetXmax() - hCont->GetXaxis()->GetXmin();
      double yrange = hCont->GetYaxis()->GetXmax() - hCont->GetYaxis()->GetXmin();

      TGraph *graph;
      bool hack2 = false;
      if(hack && i<1) {
        hack2 = true;
        std::cout << "Attempting to fix smoothing for " << f[i] <<"(" 
                  << contour[j] << ")" << std::endl;
      }
      // Below line is a hack for the MC5 stuff.  Generally it can be ignored,
      int color_shift;
      if(nfiles==2) { 
        color_shift=6-3*i;
      } else if( nfiles == 1 ) { 
        color_shift = 0;
      } else color_shift =6-3*(int)(i>1);
      // it goes along with a similar line involving ``distmin`` in plotGraphs()
//      if( i==1 && graphName.Contains("68") ) distance +=0.01;
      if (rawGraphs) graph = plotGraphsOld( graphName, color[j]-color_shift, style[i]);
      else 
        graph = plotGraphs( graphName, color[j]-color_shift, style[i],
                            distance, xrange, yrange, minPoints );
    }
  }
}

int overLays_nvar( TString* f, TString* vars, int** style, int nfiles, 
             std::vector<std::pair<int,int> > varlist , double distance,
             bool rawGraphs = false, TString* contour, 
             int** color, int ncont, TString dir_ext ="", 
             double minPoints = kMinPoints ) 
{

    gROOT->SetStyle("Pub");
    gStyle->SetCanvasColor(0);
    gStyle->SetPadRightMargin(0.18);

    for ( int i=0; i<nfiles; ++i ) {
        TFile* file = new TFile(f[i]);
        TString directory("plots_");
        directory += varlist[i].first; directory += "_"; 
        directory += varlist[i].second;
        directory += dir_ext;
        file->cd( directory );

        for (int j = 0; j<ncont; ++j)
        {
            TString graphName("graph");
            graphName += contour[j];
            graphName += "_";
            if (!i && !j) { //on first run
                TH2F* hCont = gDirectory->Get("hCont");
                hCont->Reset("ICE");
                hCont->GetYaxis()->SetTitleOffset(1.5);
                hCont->GetYaxis()->SetTitle(vars[1]);
                hCont->GetXaxis()->SetTitle(vars[0]);

                hCont->Draw();
            }
            double xrange = hCont->GetXaxis()->GetXmax() - 
                hCont->GetXaxis()->GetXmin();
            double yrange = hCont->GetYaxis()->GetXmax() - 
                hCont->GetYaxis()->GetXmin();

            TGraph *graph;
            if (rawGraphs) graph = plotGraphsOld( graphName, color[i][j], style[i][j]);
            else 
                graph = plotGraphs( graphName, color[i][j], style[i][j],
                        distance, xrange, yrange, minPoints );
        }
    }
}

int drawspline(TH1F* hist)
{
    int nbins = hist->GetNbinsX();
    double yval[101], xval[101];
    for (int i=0; i < nbins;i++){
        yval[i] = hist->GetBinContent(i+1);  //whoever came up with this should be shot
        xval[i] = hist->GetBinCenter(i+1);
        cout << i << " " << xval[i] << "  " << yval[i] << endl;
    }

    double y1[10], x1[10], binpos[10];
    int start = 0, end = 1000;  
    int minbin = hist->GetMinimumBin();  
    //  hist->GetBinWithContent(9., start, 1, minbin,10.);
    for (int i=0;i<nbins;i++){
        if (yval[i]<10 && yval[i+1]<10 ) {
            start = i;
            break;
        }
    }

    hist->GetBinWithContent(9., end, minbin, nbins,10.);

    cout << "start= "<< start << " minbin= " << minbin << " end= " << end << endl;

    binpos[0]=start;
    binpos[9]=end;

    int dist=4;
    if ( (minbin - start) < 6 ) dist=1;
    int range1 = minbin-dist - start;
    int range2 = end - minbin+dist;


    int nstep1 = 3, nstep2 =4;
    if (range1 > range2) {
        nstep1 =4;
        nstep2 =3;
    } 
    int step1 = int(range1/nstep1);
    int step2 = int(range2/nstep2);

    for (int i=1;i<nstep1;i++){
        binpos[i]=start+i*step1;
    }
    binpos[nstep1]=minbin-dist;
    binpos[nstep1+1]=minbin;
    binpos[nstep1+2]=minbin+dist;
    for (int i=1;i<nstep2;i++){
        binpos[nstep1+2+i]=minbin+dist+i*step2;
    }

    for (int i=0;i<10;i++){
        y1[i] = hist->GetBinContent(binpos[i]);
        x1[i] = hist->GetBinCenter(binpos[i]);
    }

    //   //chf temp hack to work around spikes. Note: last point could be away from end...
    //   int range = end - start;
    //   int step = int(range/7);
    //   cout << "step= " << step << endl;
    //   for (int i=0;i<8;i++){
    //      y1[i]= hist->GetBinContent(start+i*step);
    //      x1[i]= hist->GetBinCenter(start+i*step); 
    //   }
    //   //end of hack


    for (int i=0;i<10;i++){
        cout << i << " bin = " << binpos[i] << "  xval = " << x1[i] << "  yval = " << y1[i] << endl;
    }


    gr1 = new TGraph(10,x1,y1);
    gr1->SetMarkerColor(kBlue);
    gr1->SetMarkerStyle(21);
    gr1->SetLineColor(kRed);
    gr1->SetLineWidth(2);
    gr1->Draw("CP");


    //   TSpline3 *s = new TSpline3("grs",gr1);
    //   s->SetLineWidth(3);  
    //   s->SetLineColor(kRed);
    //   s->Draw("same");
    //   TSpline5 *s5 = new TSpline5("grs",gr1);
    //   s5->SetLineWidth(3);  
    //   s5->SetLineColor(kGreen);
    //   s5->Draw("same");

}

void printMaxMin(TString graphName, TString fileName, int var1 =1 , int var2=2,
    TString ex = "", TString var1name = "", TString var2name = "") 
{
    using namespace std;
    //cout << graphName << " in " << fileName << endl;
    TFile* f = new TFile(fileName);
    TString dir = "plots_"; dir+=var1; dir+="_"; dir+=var2; dir+=ex;
    f->cd(dir);
    double xmax,xmin,ymax,ymin;
    Long_t igraph = 0;
    TGraph* graph;
    double xmax(-1.),xmin(1e9),ymax(-1.),ymin(1e9);
    while ( key = gDirectory->FindKey( graphName+igraph ) ){
        graph = (TGraph*)key->ReadObj();
        double x,y;
        double entries = graph->GetN();
        for (int i = 0; i<entries; ++i)
        {
            graph->GetPoint(i,x,y);
            if(x>xmax) xmax=x;
            if(x<xmin) xmin=x;
            if(y>ymax) ymax=y;
            if(y<ymin) ymin=y;
        }
        ++igraph;
    }
    cout << setw(8) << var1name << " = [" << xmin << "," << xmax << "]" << endl;
    cout << setw(8) << var2name << " = [" << ymin << "," << ymax << "]" << endl;
}
