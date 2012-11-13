#! /usr/bin/env python
from config import red_band_list as hl
from modules import spaces as s
from modules import lh1d as lh

from sys import argv

def main() :
    histos = hl.get_higgs_plot()
    for f in argv[1:] :
        lh.make_red_band_plot_raw(histos, f, "eps")
#        lh.make_red_band_plot_smooth(histos, f, "eps")

if __name__ == "__main__":
    main()
