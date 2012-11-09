#! /usr/bin/env python
from config import histo_list as hl
from modules import spaces as s
from modules import lh1d as lh
#from modules import grid 

from sys import argv

def main() :
#    grid_spaces = hl.get_grid_spaces()
#    grid_hists = hl.get_grid_hists()
#    grid_size_x_y = hl.get_grid_size_x_y()
    spaces = hl.getSpaceDict()
    histos = hl.get1DDict()
#    var1, var2 = hl.get_colour_contour_dict()
    for f in argv[1:] :
        s.makeSingleSpacePlot(spaces, f, "pdf")
#        grid.make_grid_plot(grid_spaces, grid_hists,grid_size_x_y, f , "pdf")
#        s.make_colour_contour_overlay(var1,var2,f,"pdf" )
        lh.makeSingle1DPlot(histos, f, "pdf")

if __name__ == "__main__":
    main()
