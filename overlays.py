#! /usr/bin/env python
from config import histo_list as hl
from modules import spaces as s
from modules import lh1d as lh

from sys import argv

def main() :
    spaces = hl.get_space_overlay_dict()
    histos = hl.get_1d_overlay_dict()
    files =  argv[1:] 

    s.make_single_space_overlay(spaces, files , "png")
    lh.make_single_1d_overlay(histos, files, "png")

if __name__ == "__main__":
    main()
