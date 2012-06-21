#! /usr/bin/env python
from config import histo_list as hl
from modules import spaces as s
from modules import lh1d as lh

from sys import argv

def main() :
    spaces = hl.getSpaceDict()
    histos = hl.get1DDict()
    for f in argv[1:] :
        s.individual_space_plots(spaces, f, "png")
        s.grid_plot(spaces, f, "png")
        lh.individual_1d_plot(histos, f, "png")

if __name__ == "__main__":
    main()
