#! /usr/bin/env python
from config import histo_list as hl
from modules import spaces as s
from modules import lh1d as lh

from sys import argv

def main() :
    r_s_histos = hl.get_raw_smooth()
    files =  argv[1:] 
    for file in files:
        lh.make_raw_smooth_overlays(r_s_histos, file, "eps")

if __name__ == "__main__":
    main()
