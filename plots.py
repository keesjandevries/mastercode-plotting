#! /usr/bin/env python
from config import histo_list as hl
from modules import spaces as s

def main() :
    spaces = hl.getSpaceDict()
    histos = hl.get1DDict()
    #s.makeSingleSpacePlot(spaces)
    s.makeSingle1DPlot(histos)

if __name__ == "__main__":
    main()
