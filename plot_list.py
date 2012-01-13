#! /usr/bin/env python

def dict_test() :
    l = {
          "/home/hyper/Projects/mastercode-plotting/plots_out.root" :
            { 
                "entry_histograms" : [ "iHist_1_2", "iHist_2_4" ], 
          #      "second_dir"       : [ "hcc2" ],
            },
          #"/some/other/file" :   
          #  {
          #      "some_dir" : [ "h1", "h2" ],
          #  }
        }
    return l


def get_dict() :
    return dict_test()
    

