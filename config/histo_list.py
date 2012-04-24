from config.plot_defaults import getDefaults as pd

def getSpaceDict() :
    return spaces

def get1DDict() :
    return hists


hists = {
            "data_histograms/iHist_mneu1_dchi" : pd( "dchi", "mneu1" ),
            "data_histograms/iHist_mh_dchi"    : pd( "dchi", "mh" )
        }

spaces = { 
            "data_histograms/iHist_m0_m12_chi2"   : pd("chi2", "m0",  "m12" ),
            "data_histograms/iHist_m0_m12_pval"   : pd("pval", "m0",  "m12" ),
            "data_histograms/iHist_m0_m12_dchi"   : pd("dchi", "m0",  "m12" ),
            "data_histograms/iHist_m0_tanb_chi2"  : pd("chi2", "m0",  "tanb"),
            "data_histograms/iHist_m0_tanb_pval"  : pd("pval", "m0",  "tanb"),
            "data_histograms/iHist_m0_tanb_dchi"  : pd("dchi", "m0",  "tanb"),
            "data_histograms/iHist_tanb_m12_chi2" : pd("chi2", "tanb","m12" ),
            "data_histograms/iHist_tanb_m12_pval" : pd("pval", "tanb","m12" ),
            "data_histograms/iHist_tanb_m12_dchi" : pd("dchi", "tanb","m12" ),
         }
