#! /usr/bin/env python
from config import overlay_lhoods_list as hl
from modules import lh1d as lh

from sys import argv

def main() :
    histos = hl.get_1d_overlay_dict()
    files =  argv[1:] 

    lh.make_single_1d_overlay(histos, files, "eps")

if __name__ == "__main__":
    main()
