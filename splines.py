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

def configuration():
    out = {
             "FolderType":      mcc.calcModes[1],
             "Ymax":            9.0,
             "Var1":            [138,119],
             "Var2":            [0,0],
             "Draw1":           True,
             "Draw2":           False,
             "XvarName":        ["m_{0}","tan(#beta)"],
             "YvarName":        ["#Delta#chi^{2}"],
             "OutfilePrefix":   "~/mc7",
             "OutfileType":     "png",
             "LineColors":      [ROOT.kBlue, ROOT.kRed, ROOT.kGreen][:-1],
             "Label":           "CMSSM preLHC",
             "LabelColor":      8,
             "LabelLocation":   [0.2,0.8],
             "LabelTextSize":   0.05
          }       
    return out

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

def getLine( filename, d, i, short ):
    f = ROOT.gROOT.GetListOfFiles().FindObject(filename)
    if f is None:
        f = ROOT.TFile.Open(filename,"UPDATE")
    directory = mcf.getPlotDirectory( d["Var1"][i], d["Var2"][i], \
        d["ContourType"], short )
    assert f.GetDirectory( directory ), \
        "Failed to open directory %s" % ( directory )
    hist1 = f.Get( directory+"/h1" )    
    hist2 = f.Get( directory+"/h2" )    


class splineInfo(object) :
    def __init__( self, d ) :
        self.xmax_list    = d["Xmax"]
        self.xmin_list    = d["Xmin"]
        self.yoffset_list = d["Yoffset"]
        self.smooth_list  = d["Smoothing"]

        self.filename     = d["Filename"]
        self.plotvar      = d["PlotVar"]
        self.label        = d["Label"]

        self.directory    = mcf.getPlotDirectory( d["Var1"], d["Var2"], d["CalcMode"], d["Short"] )

    def addSmooth( xmin, xmax, yoffset, smoothing ) :
        self.xmax_list.append(xmax)
        self.xmin_list.append(xmin)
        self.yoffset_list.append(yoffset)
        self.smooth.append(smoothing)
    def setLabel( label ) :
        self.label = label

def makeSplineObject( filename, x, y, plotVar, calcMode, short = False, label = "" ) :
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
          "Smoothing": []
         }   
    splineObj = splineInfo( d )
    return splineObj

def main(argv=None):
    print "Sweet"

if __name__ == "__main__":
    main()
