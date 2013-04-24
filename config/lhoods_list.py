from config.plot_defaults import getDefaults as pd
from collections import OrderedDict


def get_1d_dict() :
    return hists


hists = {
#            "data_histograms/iHist_neu1_dchi"      : pd( "dchi", "mneu1" ),
#            "data_histograms/iHist_Dm_stau1_neu1_dchi"      : pd( "dchi", "Dm_stau1_neu1" ),
#            "smooth_histograms/iHist_Dm_stau1_neu1_dchi"      : pd( "dchi", "Dm_stau1_neu1" ),
#            "smooth_histograms/iHist_Dm_nslp_lsp_dchi"      : pd( "dchi", "Dm_nslp_lsp" ),
#            "data_histograms/iHist_Dm_nslp_lsp_dchi"      : pd( "dchi", "Dm_nslp_lsp" ),
#            "smooth_histograms/iHist_Dm_nslp_lsp_dchi"      : pd( "dchi", "Dm_nslp_lsp" ),
#            "data_histograms/iHist_m_h^0_dchi"      : pd( "dchi", "mh" ),
            "data_histograms/iHist_stau_1_dchi"     : pd("dchi","mstau1"),
            "data_histograms/iHist_gluino_dchi"     : pd("dchi", "mg"   ),
            "data_histograms/iHist_squark_r_dchi"  : pd("dchi", "msqr" ),
            "data_histograms/iHist_BsmumuRatio_dchi"     : pd("dchi", "bsmmratio" ),
            "data_histograms/iHist_stop1_dchi"  : pd("dchi", "stop1" ),
#            "data_histograms/iHist_stau_1_chi2"         : pd("chi2",    "mstau1"    ),
#            "data_histograms/iHist_gluino_chi2"         : pd("chi2",    "mg"        ),
#            "data_histograms/iHist_squark_r_chi2"       : pd("chi2",    "msqr"      ),
#            "data_histograms/iHist_BsmumuRatio_chi2"    : pd("chi2",    "bsmmratio" ),
#            "data_histograms/iHist_BsmumuRatio_chi2"    : pd("chi2",    "bsmm" ),
#            "data_histograms/iHist_stop1_chi2"          : pd("chi2",    "stop1"     ),
        }

