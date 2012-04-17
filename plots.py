#! /usr/bin/env python
from config import histo_list as hl
from modules import spaces as s
from modules import lh1d as lh

def main() :
    spaces = hl.getSpaceDict()
    histos = hl.get1DDict()
    s.makeSingleSpacePlot(spaces)
    lh.makeSingle1DPlot(histos)

if __name__ == "__main__":
    main()
