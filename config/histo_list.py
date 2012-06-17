from config.plot_defaults import getDefaults as pd
from collections import OrderedDict

def getSpaceDict() :
    return spaces

def get_space_overlay_dict() :
    return space_overlay

def get1DDict() :
    return hists

def get_1d_overlay_dict() :
    return dlh_overlay

def get_colour_contour_dict():
    return colour, contour


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
            "data_histograms/iHist_m0_m12_dchi"     : pd("dchi", "m0",  "m12" ),
            "data_histograms/iHist_m0_m12_chi2"     : pd("chi2", "m0",  "m12" ),
#            "data_histograms/iHist_m0_tanb_dchi"    : pd("dchi", "m0",  "m12" ),
#            "data_histograms/iHist_m0_tanb_chi2"    : pd("chi2", "m0",  "m12" ),
#            "data_histograms/iHist_tanb_m12_dchi"   : pd("dchi", "tanb","m12" ),
#            "data_histograms/iHist_tanb_m12_chi2"   : pd("chi2", "tanb","m12" ),
#            "data_histograms/iHist_mA0_tanb_dchi"   : pd("dchi", "MA"  ,"tanb"),
#            "data_histograms/iHist_mA0_tanb_chi2"   : pd("chi2", "MA"  ,"tanb"),
#            "data_histograms/iHist_neu1_sigma_pp^SI_dchi"   : pd("dchi", "mneu1"  ,"ssi"),
#            "data_histograms/iHist_neu1_sigma_pp^SI_chi2"   : pd("chi2", "mneu1"  ,"ssi"),
###            "data_histograms/iHist_mA0_tanb_pred_Bsmumu"   : pd("Pbsmm", "MA"  ,"tanb"),
##            "data_histograms/iHist_mneu1_ssi_dchi": pd("dchi","mneu1","ssi" ),
        }

dlh_overlay = {
                "data_histograms/iHist_Bsmumu_dchi"     : pd("dchi", "bsmm" ),
               }

space_overlay = {
            "data_histograms/iHist_m0_m12_dchi"     : pd("dchi", "m0",  "m12" ),
            "data_histograms/iHist_m0_tanb_dchi"    : pd("dchi", "m0",  "tanb" ),
            "data_histograms/iHist_tanb_m12_dchi"   : pd("dchi", "tanb","m12" ),
            "data_histograms/iHist_mA0_tanb_dchi"   : pd("dchi", "MA"  ,"tanb"),
                }
#contour = OrderedDict()
contour = [
            ["data_histograms/iHist_m0_m12_dchi"     , pd("dchi", "m0",  "m12" )],
#            ["data_histograms/iHist_m0_m12_dchi"     , pd("dchi", "m0",  "m12" )],
#            ["data_histograms/iHist_m0_m12_dchi"     , pd("dchi", "m0",  "m12" )],
            ["data_histograms/iHist_mA0_tanb_dchi"   , pd("dchi", "MA"  ,"tanb")],
#            ["data_histograms/iHist_mA0_tanb_dchi"   , pd("dchi", "MA"  ,"tanb")],
#            ["data_histograms/iHist_mA0_tanb_dchi"   , pd("dchi", "MA"  ,"tanb")],
          ]

colour = OrderedDict()
colour =[
#          [  "data_histograms/iHist_m0_m12_pred_MW"          , pd("PMW", "m0"  ,"m12") ], 
          [  "data_histograms/iHist_m0_m12_pred_Bsmumu"      , pd("Pbsmm", "m0"  ,"m12") ], 
#          [  "data_histograms/iHist_m0_m12_pred_Oh^2"        , pd("POh2", "m0",  "m12" ) ],
#          [  "data_histograms/iHist_m0_m12_pred_m_h^0"       , pd("Pm_h0", "m0",  "m12" )],

#          [  "data_histograms/iHist_mA0_tanb_pred_MW"        , pd("PMW", "MA"  ,"tanb")],
          [  "data_histograms/iHist_mA0_tanb_pred_Bsmumu"    , pd("Pbsmm", "MA"  ,"tanb")],
#          [  "data_histograms/iHist_mA0_tanb_pred_Oh^2"      , pd("POh2", "MA",  "tanb" )],
#          [  "data_histograms/iHist_mA0_tanb_pred_m_h^0"     , pd("Pm_h0", "MA"  ,"tanb")],
        ]
