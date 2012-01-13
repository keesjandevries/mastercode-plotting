#! /usr/bin/env python

import ROOT as r
import plot_list as pl

def get_hists( d ) :
    hlist = []
    for rfile in d.keys() :
        hnames = []
        for rdir in d[rfile].keys() :
            for hname in d[rfile][rdir] :
                hnames.append( "%s/%s" % ( rdir, hname ) )
        f = r.TFile.Open( rfile )
        r.gROOT.cd()
        for hn in hnames :
            hlist.append( f.Get( hn ).Clone() )
        f.Close()
    return hlist
            

def main( argv=None ) :
    d = pl.get_dict()
    hl = get_hists( d )
    print hl[1].FindBin(115,115)


if __name__ == "__main__":
    main()
