from config.plot_defaults import getDefaults as pd
from collections import OrderedDict


def get_space_overlay_dict() :
    return space_overlay

space_overlay = {
            "data_histograms/iHist_m0_m12_dchi"     : pd("dchi", "m0",  "m12" ),
#            "data_histograms/iHist_m0_tanb_dchi"    : pd("dchi", "m0",  "tanb" ),
#            "data_histograms/iHist_tanb_m12_dchi"   : pd("dchi", "tanb","m12" ),
            "data_histograms/iHist_mA0_tanb_dchi"   : pd("dchi", "MA"  ,"tanb"),
#            "data_histograms/iHist_neu1_sigma_pp^SI_cm-2_dchi"   : pd("dchi", "mneu1"  ,"ssicm"),
                }
