from config.plot_defaults import getDefaults as pd
from collections import OrderedDict

def get_higgs_plot():
    return higgs_plot

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


grid_list={
                
            "data_histograms/iHist_m0_m12_dchi"     : pd("dchi", "m0",  "m12" ),
            "data_histograms/iHist_m0_m12_chi2"     : pd("chi2", "m0",  "m12" ),
            "data_histograms/iHist_gluino_dchi"     : pd("dchi", "mg"   ),
            "data_histograms/iHist_gluino_chi2"     : pd("dchi", "mg"   ),
          }

hists = {
#            "data_histograms/iHist_neu1_dchi"      : pd( "dchi", "mneu1" ),
#            "data_histograms/iHist_m_h^0_dchi"      : pd( "dchi", "mh" ),
            "data_histograms/iHist_stau_1_dchi"     : pd("dchi","mstau1"),
            "data_histograms/iHist_gluino_dchi"     : pd("dchi", "mg"   ),
            "data_histograms/iHist_squark_r_dchi"  : pd("dchi", "msqr" ),
            "data_histograms/iHist_BsmumuRatio_dchi"     : pd("dchi", "bsmmratio" ),
##            "data_histograms/iHist_RatioBsmumu_dchi"     : pd("dchi", "bsmm" ),
#           "data_histograms/iHist_stop1_dchi"  : pd("dchi", "stop1" ),
        }

spaces = { 
            "data_histograms/iHist_m0_m12_dchi"     : pd("dchi", "m0",  "m12" ),
##            "data_histograms/iHist_m0_m12_pred_m_h^0": pd("Pm_h0", "m0" ,"m12" ),
##           "data_histograms/iHist_m0_m12_pred_Bsmumu":       pd("Pbsmm", "m0"  ,"m12") , 
           "data_histograms/iHist_m0_m12_chi2"     : pd("chi2", "m0",  "m12" ),
            "data_histograms/iHist_m0_tanb_dchi"    : pd("dchi", "m0",  "tanb" ),
            "data_histograms/iHist_m0_tanb_chi2"    : pd("chi2", "m0",  "m12" ),
            "data_histograms/iHist_tanb_m12_dchi"   : pd("dchi", "tanb","m12" ),
            "data_histograms/iHist_tanb_m12_chi2"   : pd("chi2", "tanb","m12" ),
            "data_histograms/iHist_mA0_tanb_dchi"   : pd("dchi", "MA"  ,"tanb"),
            "data_histograms/iHist_mA0_tanb_chi2"   : pd("chi2", "MA"  ,"tanb"),
#            "data_histograms/iHist_mA0_tanb_pred_m_h^0"     : pd("Pm_h0", "MA"  ,"tanb"),
#            "data_histograms/iHist_mA0_tanb_pred_Bsmumu"    : pd("Pbsmm", "MA"  ,"tanb"),
#            "data_histograms/iHist_neu1_sigma_pp^SI_dchi"   : pd("dchi", "mneu1"  ,"ssi"),
#            "data_histograms/iHist_neu1_sigma_pp^SI_chi2"   : pd("chi2", "mneu1"  ,"ssi"),
#            "data_histograms/iHist_neu1_sigma_pp^SI_cm-2_dchi"   : pd("dchi", "mneu1"  ,"ssicm"),
#            "data_histograms/iHist_neu1_sigma_pp^SI_cm-2_chi2"   : pd("chi2", "mneu1"  ,"ssicm"),
####            "data_histograms/iHist_mA0_tanb_pred_Bsmumu"   : pd("Pbsmm", "MA"  ,"tanb"),
##            "data_histograms/iHist_mneu1_ssi_dchi": pd("dchi","mneu1","ssi" ),
        }

contour = [
#            ["data_histograms/iHist_m0_m12_dchi"     , pd("dchi", "m0",  "m12" )],
#            ["data_histograms/iHist_m0_m12_dchi"     , pd("dchi", "m0",  "m12" )],
#            ["data_histograms/iHist_m0_m12_dchi"     , pd("dchi", "m0",  "m12" )],
#            ["data_histograms/iHist_mA0_tanb_dchi"   , pd("dchi", "MA"  ,"tanb")],
#            ["data_histograms/iHist_mA0_tanb_dchi"   , pd("dchi", "MA"  ,"tanb")],
#            ["data_histograms/iHist_mA0_tanb_dchi"   , pd("dchi", "MA"  ,"tanb")],
#            ["data_histograms/iHist_neu1_sigma_pp^SI_cm-2_dchi"   , pd("dchi", "mneu1"  ,"ssicm")],
          ]

colour =[
#          [  "data_histograms/iHist_m0_m12_pred_MW"          , pd("PMW", "m0"  ,"m12") ], 
#          [  "data_histograms/iHist_m0_m12_pred_Bsmumu"      , pd("Pbsmm", "m0"  ,"m12") ], 
#          [  "data_histograms/iHist_m0_m12_pred_tanb"       , pd("Ptanb", "m0"  ,"m12") ], 
#           [ "data_histograms/iHist_m0_m12_chi2"     , pd("chi2", "m0",  "m12" ),]
#          [  "data_histograms/iHist_m0_m12_pred_Oh^2"        , pd("POh2", "m0",  "m12" ) ],
#          [  "data_histograms/iHist_m0_m12_pred_m_h^0"       , pd("Pm_h0", "m0",  "m12" )],
#          [  "data_histograms/iHist_mA0_tanb_pred_MW"        , pd("PMW", "MA"  ,"tanb")],
#          [  "data_histograms/iHist_mA0_tanb_pred_Bsmumu"    , pd("Pbsmm", "MA"  ,"tanb")],
#          [  "data_histograms/iHist_mA0_tanb_pred_Oh^2"      , pd("POh2", "MA",  "tanb" )],
#          [  "data_histograms/iHist_mA0_tanb_pred_m_h^0"     , pd("Pm_h0", "MA"  ,"tanb")],
#            ["data_histograms/iHist_neu1_sigma_pp^SI_cm-2_chi2"   , pd("chi2", "mneu1"  ,"ssicm")],
        ]







higgs_plot =       {
            "data_histograms/iHist_m_h^0_dchi"      : pd( "dchi_red_band", "mh" ),
#            "data_histograms/iHist_m_h^0_dchi"      : pd( "dchi", "mh" ),
        }
dlh_overlay = {
#              "data_histograms/iHist_BsmumuRatio_dchi"     : pd("dchi", "bsmmratio" ),
##              "data_histograms/iHist_Bsmumu_dchi"     : pd("dchi", "bsmm" ),
#            "data_histograms/iHist_m_h^0_dchi"      : pd( "dchi", "mh" ),
#            "data_histograms/iHist_stau_1_dchi"     : pd("dchi","mstau1"),
#            "data_histograms/iHist_gluino_dchi"     : pd("dchi", "mg"   ),
#            "data_histograms/iHist_squark_r_dchi"  : pd("dchi", "msqr" ),
#            "data_histograms/iHist_stop1_dchi"  : pd("dchi", "stop1" ),
##                "data_histograms/iHist_neu1_dchi"     : pd("dchi", "mneu1" ),
               }

space_overlay = {
            "data_histograms/iHist_m0_m12_dchi"     : pd("dchi", "m0",  "m12" ),
#            "data_histograms/iHist_m0_tanb_dchi"    : pd("dchi", "m0",  "tanb" ),
#            "data_histograms/iHist_tanb_m12_dchi"   : pd("dchi", "tanb","m12" ),
            "data_histograms/iHist_mA0_tanb_dchi"   : pd("dchi", "MA"  ,"tanb"),
##            "data_histograms/iHist_neu1_sigma_pp^SI_cm-2_dchi"   : pd("dchi", "mneu1"  ,"ssicm"),
                }
#contour = OrderedDict()
