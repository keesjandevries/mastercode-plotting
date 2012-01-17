#! /usr/bin/env python

import plot_list as pl
import plot_options as po

def main( argv=None ) :
    fileout = "sample_output.pdf"
    
    d, tree_props = pl.get_file_dict()
    hd = pl.get_hist_dict( d )

    hists = pl.get_filled_hists( hd, tree_props )
    po.print_to_single_file( hists, fileout )

if __name__ == "__main__":
    main()
