#! /usr/bin/env python
from config import histo_list as hl
from modules import spaces as s

def main() :
    histos = hl.getSpaceDict()
    s.makeSinglePlots(histos)

if __name__ == "__main__":
    main()
