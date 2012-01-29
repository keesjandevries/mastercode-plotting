#! /usr/bin/env python

import plot_list as pl
import histograms as hfuncs

def main( argv=None ) :
    fileout = "sample_output.root"
    
    d, tree_props = pl.get_file_dict()
    hd = hfuncs.get_hist_dict( d )

    hists = hfuncs.get_filled_hists( hd, tree_props )

    hfuncs.save_hlist_to_root_file( hists, fileout)

if __name__ == "__main__":
    main()
