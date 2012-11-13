#! /usr/bin/env python
from config import lhoods_list  as hl
#from modules import spaces as s
from modules import lh1d as lh
#from modules import grid 

from sys import argv

def main() :
    histos = hl.get_1d_dict()
    for f in argv[1:] :
        lh.make_single_1d_plot(histos, f, "pdf")

if __name__ == "__main__":
    main()
