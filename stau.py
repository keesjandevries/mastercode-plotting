#! /usr/bin/env python
from config import histo_list as hl
from modules import spaces as s
from modules import lh1d as lh

from sys import argv

def main() :
    histos = hl.get_stau_plots()
    for f in argv[1:] :
        lh.make_red_band_plot_raw(histos, f, "eps")

if __name__ == "__main__":
    main()
