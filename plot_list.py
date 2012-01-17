#! /usr/bin/env python

def dict_test() :
    l = {
          "/home/hyper/Documents/mastercode_data/cmssm_test.root" :
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

# change this to your function of choice
def get_file_dict() :
    tree_props = {
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
    }
    return dict_test(), tree_props
    

