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
    options,args = parser.parse_args()
    assert options.filename!=None,"File must be specified"
    return options
############################################

# you should definitely change this stuff :) it's what's going ot be plotted
def configuration():
    out = { "MinPointsToDraw": 35, 
             "ContourType":     ["RawChi2", "DeltaChi2", "PValue", "FTestSM", \
                                 "ObsContribution" ][2],
             "OutfilePrefix":   "test_file",
             "Xvar":            [1,4],
             "Yvar":            [2,2],
             "XvarName":        ["m_{0}","tan(#beta)"],
             "YvarName":        ["m_{1/2}","m_{1/2}"],
             "Zmax":            1.0,
             "Zmin":            0.0,
             "Zsteps":          25,
             "label":           "TEST PLOT",
             "labelLocation":   array( 'd', [0.1, 0.1, 1.0, 1.0] ),
             "ContribVar":       None
          }
    assert len(out["Xvar"]) == len(out["Yvar"]) and \
           len(out["Xvar"]) == len(out["XvarName"]) and \
           len(out["Xvar"]) == len(out["YvarName"]), \
           "Size of array of variables to plot and their names do not match"
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

def drawContour(filename,directory,conf,i):
    f = ROOT.TFile(filename)
    contour = f.Get(directory + "/hCont")
    contour.SetMaximum(conf["Zmax"])
    contour.SetMinimum(conf["Zmin"])
    contour.SetContour(conf["Zsteps"]);

    canvas = ROOT.TCanvas("MC","MCcontour",1)
    contour.Draw("colz");

    contour.GetXaxis().SetTitle(conf["XvarName"][i]);
    contour.GetYaxis().SetTitle(conf["YvarName"][i]);
    contour.GetYaxis().SetTitleOffset(1.1);
    ztitle = getZAxisTitle( conf["ContourType"] )
    contour.GetZaxis().SetTitle(ztitle)

    outfile = "~/%s_%d_%d.eps" % (conf["OutfilePrefix"], conf["Xvar"][i], \
        conf["Yvar"][i] )
    canvas.SaveAs(outfile)
    f.Close()


def main(argv=None):
    conf = configuration()
    options = opts()
    rootStyle(conf)
    colorPalette(conf)
    for i, (x, y) in enumerate( zip( conf["Xvar"], conf["Yvar"] ) ):
        directory = getPlotDirectory(x, y, conf["ContourType"], \
            conf["ContribVar"], options.short)
        drawContour( options.filename, directory, conf, i )

if __name__ == "__main__":
    main()
