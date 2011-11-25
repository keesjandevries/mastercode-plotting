#! /usr/bin/env python
import ROOT
from optparse import OptionParser
from array import array

############################################
def opts():
    parser = OptionParser("usage: %prog [options]")
    parser.add_option("-f", "--file", action="store", type="string", 
        dest="filename", default=None, metavar="F",
        help="file name to retrieve graphs from")
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
    assert options.filename!=None,"File must be specified"
    return options
############################################

# you should definitely change this stuff :) it's what's going ot be plotted
# can just dump this out as a class that takes a dictionary as a contructor
# - then just loop over some list of dictionaries to allow different contour
# modes in a single run
def configuration():
    out = { "MinPointsToDraw": 35, 
             "ContourType":     ["RawChi2", "DeltaChi2", "PValue", "FTestSM", \
                                 "ObsContribution" ][1],
             "Zmax":            25.0,
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
             "ContribVar":      None
          }
    assert len(out["Xvar"]) == len(out["Yvar"]) and \
           len(out["Xvar"]) == len(out["XvarName"]) and \
           len(out["Xvar"]) == len(out["YvarName"]) , \
           "Size of array of variables to plot and their names do not match"
    assert len(out["ContourList"]) == len(out["ContourColors"]), \
        "Size of ContourList and ContourColors do not match"
           
    return out

def getDirIndexFromMode(mode):
    out = -1
    if mode == "RawChi2":
        out = 0
    if mode == "DeltaChi2":
        out = 1
    if mode == "PValue":
        out = 2
    if mode == "ObsContribution":
        out = 3 
    if mode == "FTestSM":
        out = 4
    return out

def getZAxisTitle(mode):
    out = ""
    if mode == "RawChi2":
        out = "#chi2^{2}"
    if mode == "DeltaChi2":
        out = "#Delta#chi^{2}"
    if mode == "PValue":
        out = "P(#chi^{2},N_{dof})"
    if mode == "ObsContribution":
        out = "#chi^{2}(Obs)"
    if mode == "FTestSM":
        out = "p_{F}"
    return out

def getZMax(mode):
    out = 0.0
    if mode == "RawChi2":
        out = 60.0
    if mode == "DeltaChi2":
        out = 25.0
    if mode == "PValue":
        out = 1.0
    if mode == "ObsContribution":
        out = 9.0 
    if mode == "FTestSM":
        out = 1.0
    return out

def colorPalette(d):
    stops = array('d', [ 0.00, 0.34, 0.61, 0.84, 1.00 ] )
    # standard values
    # fades from red (low values) to blue (high values)
    red   = array('d', [ 0.00, 0.00, 0.87, 1.00, 0.51 ] )
    green = array('d', [ 0.00, 0.81, 1.00, 0.20, 0.00 ] )
    blue  = array('d', [ 0.51, 1.00, 0.12, 0.00, 0.00 ] )
    NRGBs = 5;
    NCont = 255;
    if d["ContourType"] == "RawChi2":
        NRGBs = 2
        stops = array('d', [ 0.0, 0.9 ] )
        red   = array('d', [ 0.9, 0.0 ] )
        green = array('d', [ 0.9, 0.0 ] )
        blue  = array('d', [ 0.9, 0.0 ] )
        NCont = 40
    if d["ContourType"] == "DeltaChi2":
        red   = array('d', [0.00, 0.40, 0.75, 0.90, 1.00] )
        green = array('d', [0.00, 0.40, 0.75, 0.90, 1.00] )
        blue  = array('d', [0.00, 0.40, 0.75, 0.90, 1.00] )
    
    ROOT.TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)

def rootStyle(d):
    ROOT.gROOT.SetStyle("Pub");
    ROOT.gStyle.SetCanvasColor(0);
    ROOT.gStyle.SetPadRightMargin(0.18);

def getPlotDirectory(x, y, space, contrib, short):
    assert space!="ObsContribution" or contrib, \
        "Need to specify which variable to plot the contribution of"
    index = getDirIndexFromMode(space)
    stem = ""
    if contrib:
        stem += "-%d" % contrib 
    if short:
        stem += "s"
    directory = "plots_%d_%d_%d%s" % ( x, y, index, stem )
    return directory

def drawHistogram(f,directory,conf,i):
    contour = f.Get(directory + "/hCont")

    contour.SetMaximum(conf["Zmax"])
    contour.SetMinimum(conf["Zmin"])
    contour.SetContour(conf["Zsteps"]);

    contour.Draw("colz");

    contour.GetXaxis().SetTitle(conf["XvarName"][i]);
    contour.GetYaxis().SetTitle(conf["YvarName"][i]);
    contour.GetYaxis().SetTitleOffset(1.1);
    ztitle = getZAxisTitle( conf["ContourType"] )
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

def drawLabel(conf):
    ltext = ("#color[%d]{%s}") % ( conf["LabelColor"], conf["Label"] )
    Tl = ROOT.TLatex()
    Tl.SetNDC(True);
    Tl.SetTextSize(conf["LabelTextSize"]);
    Tl.DrawLatex(conf["LabelLocation"][0], conf["LabelLocation"][1], ltext);
    return;

def main(argv=None):
    # import out configuration and command line options
    conf = configuration()
    options = opts()

    # set up root to look pretty 
    rootStyle(conf)
    colorPalette(conf)

    f = ROOT.TFile(options.filename)

    if not conf["Zmax"]:
        conf["Zmax"] = getZMax(conf["ContourType"])

    for i, (x, y) in enumerate( zip( conf["Xvar"], conf["Yvar"] ) ):
        canvas_title = "MCcontour_%d" % i
        canvas_name = "MC_%d" % i
        canvas = ROOT.TCanvas(canvas_name,canvas_title,1)

        directory = getPlotDirectory(x, y, conf["ContourType"], \
            conf["ContribVar"], options.short)

        if not options.no_histo:
            drawHistogram( f, directory, conf, i )
        if not options.no_contours:
            drawContours( f, directory, conf, i)

        drawLabel(conf)
        outfile = "%s_%s_%d_%d.%s" % (conf["OutfilePrefix"], conf["ContourType"], \
            conf["Xvar"][i], conf["Yvar"][i], conf["OutfileType"] )
        canvas.SaveAs(outfile)
        canvas.Close()

    f.Close()

if __name__ == "__main__":
    main()
