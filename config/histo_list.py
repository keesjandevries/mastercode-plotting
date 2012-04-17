from defaults.default_plots import getDefaults as pds

def getSpaceDict() :
    return spaces

def get1DDict() :
    return hists


hists = {
            "data_histograms/iHist_119_dchi" : pds( "dchi", "neu1" )
        }

spaces = { 
            "data_histograms/iHist_1_2_chi2" : pds("chi2" , "m0",  "m12" ),
            "data_histograms/iHist_1_2_pval" : pds("pval" , "m0",  "m12" ),
            "data_histograms/iHist_1_2_dchi" : pds("dchi" , "m0",  "m12" ),
            "data_histograms/iHist_1_4_chi2" : pds("chi2" , "m0",  "tanb"),
            "data_histograms/iHist_1_4_pval" : pds("pval" , "m0",  "tanb"),
            "data_histograms/iHist_1_4_dchi" : pds("dchi" , "m0",  "tanb"),
            "data_histograms/iHist_4_2_chi2" : pds("chi2" , "tanb","m12" ),
            "data_histograms/iHist_4_2_pval" : pds("pval" , "tanb","m12" ),
            "data_histograms/iHist_4_2_dchi" : pds("dchi" , "tanb","m12" ),
         }
