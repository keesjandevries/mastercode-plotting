#! /usr/bin/env python
from config import histo_list as hl
from modules import spaces as s
from modules import lh1d as lh

from sys import argv

def main() :
    spaces = hl.getSpaceDict()
    histos = hl.get1DDict()
    files =  argv[1:] 

    s.make_single_space_overlay(spaces, files , "png")
    s.makeGridPlots(spaces, f, "png")
    lh.makeSingle1DPlot(histos, f, "png")

if __name__ == "__main__":
    main()
