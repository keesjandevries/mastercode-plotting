#! /usr/bin/env python
import ROOT
import sys
from optparse import OptionParser

import mcfunctions as mc

# you should definitely change this stuff :) it's what's going ot be plotted
# can just dump this out as a class that takes a dictionary as a contructor
# - then just loop over some list of dictionaries to allow different contour
# modes in a single run
def configuration():
    out = {  
             "ContourType":     ["RawChi2", "DeltaChi2", "PValue", "FTestSM", \
                                 "ObsContribution" ][1],
             "Zmax":            None,
             "Zmin":            0.0,
             "Zsteps":          25,
             "Xvar":            [1,4],
             "Yvar":            [2,2],
             "XvarName":        ["m_{0}","tan(#beta)"],
             "YvarName":        ["m_{1/2}","m_{1/2}"],
             "OutfilePrefix":   "~/mc7",
             "OutfileType":     "png",
             "ContourList":     ["graph68", "graph95", "graph99"][:-1],
             "ContourColors":   [ROOT.kBlue, ROOT.kRed, ROOT.kGreen][:-1],
             "Label":           "CMSSM preLHC",
             "LabelColor":      8,
             "LabelLocation":   [0.2,0.8],
             "LabelTextSize":   0.05,
             "ContribVar":      None,
             "MinPointsToDraw": 35, 
          }
    assert len(out["Xvar"]) == len(out["Yvar"]) and \
           len(out["Xvar"]) == len(out["XvarName"]) and \
           len(out["Xvar"]) == len(out["YvarName"]) , \
           "Size of array of variables to plot and their names do not match"
    assert len(out["ContourList"]) == len(out["ContourColors"]), \
        "Size of ContourList and ContourColors do not match"
           
    return out

############################################
def opts():
    parser = OptionParser("usage: %prog [options]")
    parser.add_option( "-s", "--short", action="store_true", dest="short",
        default=False, 
        help = "short tree mode was used to generate the graphs" )
    parser.add_option( "--no-histogram", action="store_true", dest="no_histo",
        default=False, 
        help = "turn on to prevent drawing of histogram (i.e. for contour only \
        mode" )
    parser.add_option( "--no-contours", action="store_true", dest="no_contours",
        default=False, 
        help = "turn on to prevent drawing of contours (i.e. for histo only" )
    options,args = parser.parse_args()
    assert len(args) > 0,"File must be specified"
    return options, args
############################################


def drawHistogram(f,directory,conf,i,empty):
    contour = f.Get(directory + "/hCont")

    contour.SetMaximum(conf["Zmax"])
    contour.SetMinimum(conf["Zmin"])
    contour.SetContour(conf["Zsteps"]);

    draw_options = "colz"
    if empty:
        draw_options = ""
    contour.Draw(draw_options)

    if empty:
        contour.Reset("ICE")

    contour.GetXaxis().SetTitle(conf["XvarName"][i]);
    contour.GetYaxis().SetTitle(conf["YvarName"][i]);
    contour.GetYaxis().SetTitleOffset(1.1);
    ztitle = mc.getHistoZAxisTitle( conf["ContourType"] )
    contour.GetZaxis().SetTitle(ztitle)

def drawContours(f,directory,conf,i):
    for contourPrefix, color in zip(conf["ContourList"], conf["ContourColors"]):
        igraph = 0;
        more_graphs = True
        while more_graphs:
            graphName = ( "%s/%s_%d" ) % ( directory, contourPrefix, igraph )
            graph = f.Get(graphName)
            if graph:
                graph.SetLineColor(color);
                graph.SetLineWidth(3);
                graph.SetLineStyle(1);
                if ( graph.GetN() > conf["MinPointsToDraw"] ):
                    graph.Draw("L")
                igraph+=1;
            else:
                more_graphs = False
    return

def main(argv=None):
    ROOT.gROOT.SetBatch(0)
    # import out configuration and command line options
    conf = configuration()
    options, files = opts()
    assert len(files) > 0, "Must specify files as command line arguments"

    # set up root to look pretty 
    mc.rootStyle(conf)
    mc.histoColorPalette(conf["ContourType"])

    if not conf["Zmax"]:
        conf["Zmax"] = mc.getHistoZMax(conf["ContourType"])

    blank_histogram = len(files) > 1 or options.no_histo
    if blank_histogram:
            print "Printing blank histograms"

    for i, (x, y) in enumerate( zip( conf["Xvar"], conf["Yvar"] ) ):
        canvas_title = "MCcontour_%d" % i
        canvas_name = "MC_%d" % i
        canvas = ROOT.TCanvas(canvas_name,canvas_title,1)
        directory = mc.getPlotDirectory( x, y, conf["ContourType"], \
            options.short, conf["ContribVar"] )
        for filename in files:
            f = ROOT.TFile(filename)
            drawHistogram( f, directory, conf, i, blank_histogram )
            if not options.no_contours:
                drawContours( f, directory, conf, i)
            # if you do f.close() here then it removes teh histogram from the
            # pad (apparently it's owned by hte file.  Need to make sure we
            # clean this up at the end.  i.e. iterate over gDirectory

        mc.drawLabel(conf)
        outfile = "%s_%s_%d_%d.%s" % (conf["OutfilePrefix"], conf["ContourType"], \
            conf["Xvar"][i], conf["Yvar"][i], conf["OutfileType"] )
        canvas.SaveAs(outfile)
        canvas.Close()

if __name__ == "__main__":
    main()
