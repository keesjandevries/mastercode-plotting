from config.default_plots import getDefaults as dp

def getSpaceDict() :
    return spaces

def get1DDict() :
    return hists


hists = {
            "data_histograms/iHist_119_dchi" : dp( "dchi", "neu1" ),
            "data_histograms/iHist_28_dchi" : dp( "dchi", "mh" )
        }

spaces = { 
            "data_histograms/iHist_1_2_chi2" : dp("chi2" , "m0",  "m12" ),
            "data_histograms/iHist_1_2_pval" : dp("pval" , "m0",  "m12" ),
            "data_histograms/iHist_1_2_dchi" : dp("dchi" , "m0",  "m12" ),
            "data_histograms/iHist_1_4_chi2" : dp("chi2" , "m0",  "tanb"),
            "data_histograms/iHist_1_4_pval" : dp("pval" , "m0",  "tanb"),
            "data_histograms/iHist_1_4_dchi" : dp("dchi" , "m0",  "tanb"),
            "data_histograms/iHist_4_2_chi2" : dp("chi2" , "tanb","m12" ),
            "data_histograms/iHist_4_2_pval" : dp("pval" , "tanb","m12" ),
            "data_histograms/iHist_4_2_dchi" : dp("dchi" , "tanb","m12" ),
         }
