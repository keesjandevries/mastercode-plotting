from config.plot_defaults import getDefaults as pd
from collections import OrderedDict


def get_1d_overlay_dict() :
    return dlh_overlay

dlh_overlay = {
#              "data_histograms/iHist_Bsmumu_dchi"     : pd("dchi", "bsmm" ),
#            "data_histograms/iHist_m_h^0_dchi"      : pd( "dchi", "mh" ),
#            "data_histograms/iHist_BsmumuRatio_dchi"     : pd("dchi", "bsmmratio" ),
#           "data_histograms/iHist_stau_1_dchi"     : pd("dchi","mstau1"),
#            "data_histograms/iHist_gluino_dchi"     : pd("dchi", "mg"   ),
#            "data_histograms/iHist_squark_r_dchi"  : pd("dchi", "msqr" ),
#            "data_histograms/iHist_stop1_dchi"  : pd("dchi", "stop1" ),
            "smooth_histograms/iHist_BsmumuRatio_dchi"     : pd("dchi", "bsmmratio" ),
#            "smooth_histograms/iHist_stau_1_dchi"     : pd("dchi","mstau1"),
#            "smooth_histograms/iHist_gluino_dchi"     : pd("dchi", "mg"   ),
#            "smooth_histograms/iHist_squark_r_dchi"  : pd("dchi", "msqr" ),
#            "smooth_histograms/iHist_stop1_dchi"  : pd("dchi", "stop1" ),
###              "data_histograms/iHist_BsmumuRatio_dchi"     : pd("dchi", "bsmmratio" ),
#                "data_histograms/iHist_neu1_dchi"     : pd("dchi", "mneu1" ),
               }

