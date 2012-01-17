#! /usr/bin/env python

import ROOT as r
from array import array

def set_root_style() :
    NRGBs = 5
    NCont = 255

    r.gROOT.SetStyle("Pub");
    r.gStyle.SetCanvasColor(0);
    r.gStyle.SetPadRightMargin(0.18);

    r.gStyle.SetOptStat(0);
    r.gStyle.SetOptTitle(0);
    r.gStyle.SetOptDate(0);
    r.gStyle.SetLabelFont(63,"xy");
    r.gStyle.SetLabelSize(16,"xy");
    r.gStyle.SetTitleOffset(1.07,"y");
    r.gStyle.SetHatchesLineWidth(1);

    stops = array( 'd', [ 0.00, 0.34, 0.61, 0.84, 1.00 ] )
    red   = array( 'd', [ 0.00, 0.00, 0.87, 1.00, 0.51 ] )
    green = array( 'd', [ 0.00, 0.81, 1.00, 0.20, 0.00 ] )
    blue  = array( 'd', [ 0.51, 1.00, 0.12, 0.00, 0.00 ] )
    red   = array( 'd', [ 1.00, 0.75, 0.50, 0.25, 0.00 ] )
    green = array( 'd', [ 1.00, 0.75, 0.50, 0.25, 0.00 ] )
    blue  = array( 'd', [ 1.00, 0.75, 0.50, 0.25, 0.00 ] )

    r.TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont);
