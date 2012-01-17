#! /usr/bin/env python

import ROOT as r
import styles as sty

def get_canvas( batch = True) :
    r.gROOT.SetBatch(batch)
    r.gStyle.SetPalette(1)
    canvas = r.TCanvas("canvas","Parameter space",10,10,700,600);
    canvas.SetFillColor(0);
    canvas.SetBorderMode(0);
    canvas.SetRightMargin(0.15);
    canvas.SetLeftMargin(0.15);
    return canvas

def print_to_single_file( hists, f ) :
    sty.set_root_style()
    canvas = get_canvas()
    canvas.Draw();
    canvas.Print(f + "[")
    for h in hists :
        h.Draw("colz")
        canvas.Update()
        canvas.Print(f)
    canvas.Print(f + "]")

def set_hist_properties( h ) :
    set_chi2_hist_properties( h )

def set_chi2_hist_properties( h ) :
    h.GetYaxis().SetTitleOffset(1.5)
    h.GetZaxis().SetTitle( "#chi^{2}" )
    h.SetMinimum(20.)
    h.SetMaximum(30.)
    h.SetContour(10)
