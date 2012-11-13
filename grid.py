#! /usr/bin/env python
from config import grid_list as hl
from modules import spaces as s
from modules import lh1d as lh
from modules import grid 

from sys import argv

def main() :
    grid_spaces = hl.get_grid_spaces()
    grid_hists = hl.get_grid_hists()
    grid_size_x_y = hl.get_grid_size_x_y()
    for f in argv[1:] :
        grid.make_grid_plot(grid_spaces, grid_hists,grid_size_x_y, f , "pdf")

if __name__ == "__main__":
    main()
