#! /usr/bin/env python
import ROOT
import sys
from optparse import OptionParser
from array import array

import mcfunctions as mcf
import mcconsts as mcc

# several modes: same graph per file (i.e. gluino plotted of several files)
# several combination of lines from different files (i.e. thresholds)
# so need a function that retruns the TH1/TGraph for the line "getSpline",
# append this into a list and send to the drwaing tool :)

############################################
def opts():
    parser = OptionParser("usage: %prog [options]")
    parser.add_option( "-s", "--short", action="store_true", dest="short",
        default=True,
        help = "short tree mode was used to generate the graphs" )
    options,args = parser.parse_args()
    assert len(args) > 0,"File must be specified"
    return options, args
############################################

class splineInfo( object ) :
    def __init__( self, d ) :
        self.xmax_list    = d["Xmax"]
        self.xmin_list    = d["Xmin"]
        self.yoffset_list = d["Yoffset"]
        self.smooth_list  = d["Smoothing"]

        self.filename     = d["Filename"]
        self.plotvar      = d["PlotVar"]
        self.label        = d["Label"]

        self.color        = d["Color"]

        self.directory    = mcf.getPlotDirectory( d["Var1"], d["Var2"], d["CalcMode"], d["Short"] )

    def addSmooth( xmin, xmax, yoffset, smoothing ) :
        self.xmax_list.append(xmax)
        self.xmin_list.append(xmin)
        self.yoffset_list.append(yoffset)
        self.smooth.append(smoothing)
    def setLabel( label ) :
        self.label = label

class plotInfo( object ) :
    def __init__( self, d ) :
        self.xmax = d["Xmax"]
        self.xmin = d["Xmin"]
        self.ymax = d["Ymax"]
        self.xaxis_label = d["XAxisLabel"]
        self.yaxis_label = d["YAxisLabel"]

def makeSplineObject( filename, x, y, plotVar, calcMode, short = False, label = "", Color = ROOT.kRed ) :
    mode = mcc.calcModes[calcMode]
    d = { "Filename":  filename,
          "Var1":      x,
          "Var2":      y,
          "PlotVar":   plotVar,
          "Label":     label,
          "Short":     short,
          "CalcMode":  mode,
          "Xmax":      [],
          "Xmin":      [],
          "Yoffset":   [],
          "Smoothing": [],
          "Color":     Color
         }
    splineObj = splineInfo( d )
    return splineObj

def zeroSuppressHist( hist, xmin, xmax, yoffset = 0. ) :
    ymin = 1e9
    minimum = 0.05
    if yoffset == 0.:
        xmin = hist.GetBinLowEdge(1)
        nbins = hist.GetNbinsX()
        xmax = hist.GetBinLowEdge(nbins) + hist.GetBinWidth(nbins)
    for i in range(1,hist.GetNbinsX()+1) :
        yval = hist.GetBinContent(i)
        if( hist.GetBinLowEdge(i) > xmin ) and ( hist.GetBinLowEdge(i) + hist.GetBinWidth(i) < xmax ) :
            if( yval < ymin ) :
                ymin = yval
    for i in range( 1, hist.GetNbinsX()+1 ):
        if( hist.GetBinLowEdge(i) > xmin ) and ( hist.GetBinLowEdge(i) + hist.GetBinWidth(i) < xmax ) :
            content = hist.GetBinContent(i) - ymin + minimum + yoffset
            hist.SetBinContent( i, content )

def getGraphs( splinelist ) :
    graphlist = []
    for s in splinelist :
        f = ROOT.TFile.Open(s.filename,"UPDATE")
        assert f.GetDirectory( s.directory ), \
            "Failed to open directory %s" % ( s.directory )
        if s.plotvar == 1:
            hist = f.Get( s.directory+"/h1" )
        else :
            hist = f.Get( s.directory+"/h2" )
        graphList = []
        for ( smoothing, xmin, xmax, yoffset ) in zip( s.smooth_list, s.xmin_list, s.xmax_list, s.yoffset_list ) :
            hist.GetXaxis().SetRangeUser( xmin, xmax )
            hist.Smooth( smoothing,"R" )
            zeroSuppressHist( hist, xmin, xmax, yoffset )
        nbins = hist.GetNbinsX()
        graph = ROOT.TGraph(nbins)
        for i in range( 1, nbins+1 ) :
            graph.SetPoint( i-1, hist.GetBinCenter(i), hist.GetBinContent(i) )
        graph.SetLineColor(s.color)
        graphlist.append(graph)
    return graphlist

def drawGraphs( graphs, p ) :
    canvas = ROOT.TCanvas( "splines", "Smoothing", 10, 10, 800, 400 )
    canvas.Draw("A")
    canvas.cd()
    test1 = ROOT.Double(0)
    test2 = ROOT.Double(0)
    first = True
    options = "C"
    for graph in graphs :
        if first:
            options = "AC"
        else :
            options = "C"
        graph.Draw(options)
        if first:
            first = False
            graph.GetXaxis().SetRangeUser( p.xmin, p.xmax )
            graph.GetYaxis().SetRangeUser( 0, p.ymax )
    canvas.SaveAs("test.png")


def main(argv=None):
    mcf.rootStyle()
    d = { "Filename":  "/home/hyper/Documents/mastercode_data/cmssm-bsgOrig-g2Orig.root",
          "Var1":      138,
          "Var2":      0,
          "PlotVar":   1,
          "Label":     "TEST",
          "Short":     True,
          "CalcMode":  "DeltaChi2",
          "Xmax":      [3000,4400],
          "Xmin":      [0,3600],
          "Yoffset":   [0,0],
          "Smoothing": [10,50],
          "Color":     ROOT.kRed
         }
    e = { "Filename":  "/home/hyper/Documents/mastercode_data/cmssm-bsgOrig-g2Orig.root",
          "Var1":      119,
          "Var2":      0,
          "PlotVar":   1,
          "Label":     "TEST",
          "Short":     True,
          "CalcMode":  "DeltaChi2",
          "Xmax":      [1000],
          "Xmin":      [0],
          "Yoffset":   [5],
          "Smoothing": [10],
          "Color":     ROOT.kGreen
         }
    p = { "Xmax":       5000.0,
          "Xmin":       0.0,
          "Ymax":       9.0,
          "XAxisLabel": "TESTER LOL",
          "YAxisLabel": "#Delta#Chi^{2}"
        }
    plotter = plotInfo( p )
    spline1 = splineInfo( d )
    spline2 = splineInfo( e )
    slist = [spline1,spline2]
    graphs = getGraphs ( slist )
    drawGraphs( graphs, plotter )


if __name__ == "__main__":
    main()
