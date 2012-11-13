#! /usr/bin/env python
from config import spaces_list as hl
from modules import spaces as s

from sys import argv

def main() :
    spaces = hl.get_spaces_dict()
    for f in argv[1:] :
        s.make_single_space_plot(spaces, f, "pdf")

if __name__ == "__main__":
    main()
