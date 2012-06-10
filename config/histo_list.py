from config.plot_defaults import getDefaults as pd

def getSpaceDict() :
    return spaces

def get1DDict() :
    return hists


hists = {
#            "data_histograms/iHist_neu1_dchi"      : pd( "dchi", "mneu1" ),
#            "data_histograms/iHist_m_h^0_dchi"      : pd( "dchi", "mh" ),
#            "data_histograms/iHist_stau_1_dchi"     : pd("dchi","mstau1"),
#            "data_histograms/iHist_gluino_dchi"     : pd("dchi", "mg"   ),
#            "data_histograms/iHist_squark_r_dchi"  : pd("dchi", "msqr" ),
#            "data_histograms/iHist_Bsmumu_dchi"     : pd("dchi", "bsmm" ),
        }

#spaces = { 
#            "data_histograms/iHist_m0_m12_chi2"   : pd("chi2", "m0",  "m12" ),
#            "data_histograms/iHist_m0_m12_pval"   : pd("pval", "m0",  "m12" ),
#            "data_histograms/iHist_m0_m12_dchi"   : pd("dchi", "m0",  "m12" ),
#            "data_histograms/iHist_m0_tanb_chi2"  : pd("chi2", "m0",  "tanb"),
#            "data_histograms/iHist_m0_tanb_pval"  : pd("pval", "m0",  "tanb"),
#            "data_histograms/iHist_m0_tanb_dchi"  : pd("dchi", "m0",  "tanb"),
#            "data_histograms/iHist_tanb_m12_chi2" : pd("chi2", "tanb","m12" ),
#            "data_histograms/iHist_tanb_m12_pval" : pd("pval", "tanb","m12" ),
#            "data_histograms/iHist_tanb_m12_dchi" : pd("dchi", "tanb","m12" ),
#         }
spaces = { 
#            "data_histograms/iHist_m0_m12_dchi"     : pd("dchi", "m0",  "m12" ),
#            "data_histograms/iHist_m0_m12_chi2"     : pd("chi2", "m0",  "m12" ),
#            "data_histograms/iHist_m0_m12_dX_Oh^2"     : pd("chi2", "m0",  "m12" ),
            "data_histograms/iHist_m0_m12_pred_Bsmumu"     : pd("chi2", "m0",  "m12" ),
#            "data_histograms/iHist_m0_tanb_dchi"    : pd("dchi", "m0",  "m12" ),
#            "data_histograms/iHist_m0_tanb_chi2"    : pd("chi2", "m0",  "m12" ),
#            "data_histograms/iHist_tanb_m12_dchi"   : pd("dchi", "tanb","m12" ),
#            "data_histograms/iHist_tanb_m12_chi2"   : pd("chi2", "tanb","m12" ),
#            "data_histograms/iHist_mA0_tanb_dchi"   : pd("dchi", "MA"  ,"tanb"),
#            "data_histograms/iHist_mA0_tanb_chi2"   : pd("chi2", "MA"  ,"tanb"),
##            "data_histograms/iHist_mneu1_ssi_dchi": pd("dchi","mneu1","ssi" ),
        }
