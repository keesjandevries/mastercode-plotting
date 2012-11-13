from config.plot_defaults import getDefaults as pd
from collections import OrderedDict

def get_higgs_plot():
    return higgs_plot


higgs_plot =       {
#            "data_histograms/iHist_m_h^0_dchi"      : pd( "dchi_red_band", "mh" ),
            "smooth_histograms/iHist_m_h^0_dchi"      : pd( "dchi_red_band", "mh" ),
#            "data_histograms/iHist_m_h^0_dchi"      : pd( "dchi", "mh" ),
        }
