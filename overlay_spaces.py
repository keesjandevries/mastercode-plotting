#! /usr/bin/env python
from config import overlay_spaces_list as hl
from modules import spaces as s

from sys import argv

def main() :
    spaces = hl.get_space_overlay_dict()
    files =  argv[1:] 

    s.make_single_space_overlay(spaces, files , "eps")

if __name__ == "__main__":
    main()
