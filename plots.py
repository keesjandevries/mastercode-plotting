#! /usr/bin/env python
from config import histo_list as hl
from modules import spaces as s
from modules import lh1d as lh

from sys import argv

def main() :
    spaces = hl.getSpaceDict()
    histos = hl.get1DDict()
    for file in argv[1:] :
        s.makeSingleSpacePlot(spaces, file)
        s.makeGridPlots(spaces, file)
        lh.makeSingle1DPlot(histos, file)

if __name__ == "__main__":
    main()
