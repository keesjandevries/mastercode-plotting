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
    parser.add_option("--merge",      dest = "merge",      default = False, action  = "store_true", help = "merge job output")
    options,args = parser.parse_args()
    assert options.filename!=None,"File must be specified"
    return options
############################################


# you should definitely change this stuff :) it's what's going ot be plotted
def configuration():
    return { "MinPointsToDraw": 35, 
             "SpaceType":       ["RawChi2", "DeltaChi2", "PValue", "FTestSM", \
                                 "ObsContribution" ][1],
             "varX": 1,
             "varY": 2,
             "varContrib": None
           }

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

def colorPalette(d):
    stops = array('d', [ 0.00, 0.34, 0.61, 0.84, 1.00 ] )
    # standard values
    # fades from red (low values) to blue (high values)
    red   = array('d', [ 0.00, 0.00, 0.87, 1.00, 0.51 ] )
    green = array('d', [ 0.00, 0.81, 1.00, 0.20, 0.00 ] )
    blue  = array('d', [ 0.51, 1.00, 0.12, 0.00, 0.00 ] )
    NRGBs = 5;
    NCont = 255;
    # 0: CL
    if d["SpaceType"] == "RawChi2":
        NRGBs = 2
        stops = array('d', [ 0.0, 0.9 ] )
        red   = array('d', [ 0.9, 0.0 ] )
        green = array('d', [ 0.9, 0.0 ] )
        blue  = array('d', [ 0.9, 0.0 ] )
        NCont = 40
    if d["SpaceType"] == "DeltaChi2":
        red   = array('d', [0.00, 0.40, 0.75, 0.90, 1.00] )
        green = array('d', [0.00, 0.40, 0.75, 0.90, 1.00] )
        blue  = array('d', [0.00, 0.40, 0.75, 0.90, 1.00] )
    
    ROOT.TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)

def rootStyle(d):
    ROOT.gROOT.SetStyle("Pub");
    ROOT.gStyle.SetCanvasColor(0);
    ROOT.gStyle.SetPadRightMargin(0.18);

def getPlotDirectory(c, short):
    index = getDirIndexFromMode(c["SpaceType"])
    stem = ""
    if c["varContrib"]:
        stem += "-%d" % c["varContrib"] 
    if short:
        stem += "s"
    directory = "plots_%d_%d_%d%s" % ( c["varX"], c["varY"], index, stem )
    return directory

def drawContour(filename,directory):
    f = ROOT.TFile(filename)

def main(argv=None):
    options = opts()
    conf = configuration()
    rootStyle(conf)
    colorPalette(conf)
    directory = getPlotDirectory(conf,options.short)
    drawContour(options.filename, directory)
    print directory 


if __name__ == "__main__":
    main()
