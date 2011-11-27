#! /usr/bin/env python
import ROOT
from array import array

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

def getHistoZAxisTitle(mode):
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

def getHistoZMax(mode):
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

def histoColorPalette(mode):
    stops = array('d', [ 0.00, 0.34, 0.61, 0.84, 1.00 ] )
    # standard values
    # fades from red (low values) to blue (high values)
    red   = array('d', [ 0.00, 0.00, 0.87, 1.00, 0.51 ] )
    green = array('d', [ 0.00, 0.81, 1.00, 0.20, 0.00 ] )
    blue  = array('d', [ 0.51, 1.00, 0.12, 0.00, 0.00 ] )
    NRGBs = 5;
    NCont = 255;
    if mode == "RawChi2":
        NRGBs = 2
        stops = array('d', [ 0.0, 0.9 ] )
        red   = array('d', [ 0.9, 0.0 ] )
        green = array('d', [ 0.9, 0.0 ] )
        blue  = array('d', [ 0.9, 0.0 ] )
        NCont = 40
    if mode == "DeltaChi2":
        red   = array('d', [0.00, 0.40, 0.75, 0.90, 1.00] )
        green = array('d', [0.00, 0.40, 0.75, 0.90, 1.00] )
        blue  = array('d', [0.00, 0.40, 0.75, 0.90, 1.00] )
    
    ROOT.TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)

def rootStyle(d):
    ROOT.gROOT.SetStyle("Pub");
    ROOT.gStyle.SetCanvasColor(0);
    ROOT.gStyle.SetPadRightMargin(0.18);
