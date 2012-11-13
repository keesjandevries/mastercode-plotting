#! /usr/bin/env python
from config import colour_contour_list as hl
from modules import spaces as s

from sys import argv

def main() :
    var1, var2 = hl.get_colour_contour_dict()
    for f in argv[1:] :
        s.make_colour_contour_overlay(var1,var2,f,"pdf" )

if __name__ == "__main__":
    main()
