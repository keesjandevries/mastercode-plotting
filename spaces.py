#! /usr/bin/env python
from config import histo_list as hl
from modules import spaces as s

from sys import argv

def main() :
    spaces = hl.getSpaceDict()
    for f in argv[1:] :
        s.makeSingleSpacePlot(spaces, f, "pdf")

if __name__ == "__main__":
    main()
