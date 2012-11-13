#! /usr/bin/env python
from config import histo_list as hl
from modules import spaces as s
from modules import lh1d as lh
#from modules import grid 

from sys import argv

def main() :
    histos = hl.get1DDict()
    for f in argv[1:] :
        lh.makeSingle1DPlot(histos, f, "pdf")

if __name__ == "__main__":
    main()
