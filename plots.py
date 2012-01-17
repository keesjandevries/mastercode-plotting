#! /usr/bin/env python

import plot_list as pl
import plot_options as po
import histograms as hfuncs

def main( argv=None ) :
    fileout = "sample_output.pdf"
    
    d, tree_props = pl.get_file_dict()
    hd = hfuncs.get_hist_dict( d )

    hists = hfuncs.get_filled_hists( hd, tree_props )
    po.print_to_single_file( hists, fileout )

if __name__ == "__main__":
    main()
