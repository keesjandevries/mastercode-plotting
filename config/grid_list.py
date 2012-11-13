from config.plot_defaults import getDefaults as pd
from collections import OrderedDict


def get_grid_hists():
    return grid_hists

def get_grid_spaces():
    return grid_spaces

def get_grid_size_x_y():
    return grid_size_x_y


grid_size_x_y=[26,5]

grid_spaces=OrderedDict()
grid_spaces={
            "data_histograms/iHist_m0_m12_chi2"             : pd("chi2", "m0",  "m12" ),
            "data_histograms/iHist_m0_m12_dchi"             : pd("dchi", "m0",  "m12" ),
            "data_histograms/iHist_m0_m12_pred_m_h^0"       : pd("Pm_h0", "m0" ,"m12" ),
            "data_histograms/iHist_m0_m12_pred_Bsmumu"      : pd("Pbsmm", "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_R(b->sg)"    : pd("PRbsg", "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_R(D_ms)"     : pd("PRDms", "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_R(B->taunu)" : pd("PRBtaunu", "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_R(B->Xsll)"  : pd("PRBXsll", "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_R(K->lnu)"   : pd("PRKlnu", "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_Delta(g-2)"  : pd("PDeltag2", "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_MW"          : pd("PMW", "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_sintheta_eff": pd("Psintheta_eff", "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_Gamma_Z"     : pd("PGamma_Z"     , "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_Rl"          : pd("PRl"          , "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_Rb"          : pd("PRb"          , "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_Rc"          : pd("PRc"          , "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_Afb(b)"      : pd("PAfbb"        , "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_Ab16"        : pd("PAb16"        , "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_Ac17"        : pd("PAc17"        , "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_Al(SLD)"     : pd("PAlSLD"        , "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_Al(P_tau)"   : pd("PAlP_tau"      , "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_Al_fb"       : pd("PAl_fb"        , "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_sigma_had^0" : pd("Psigma_had0"   , "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_R(Delta_mk)" : pd("PRDelta_mk"    , "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_R(Kp->pinn)" : pd("PRKppinn"      , "m0"  ,"m12") , 
            "data_histograms/iHist_m0_m12_pred_BR(Bd->ll)"  : pd("PBRBdll"       , "m0"  ,"m12") , 



            "data_histograms/iHist_A0_tanb_chi2"             : pd("chi2", "A0",  "tanb" ),
            "data_histograms/iHist_A0_tanb_dchi"             : pd("dchi", "A0",  "tanb" ),
            "data_histograms/iHist_A0_tanb_pred_m_h^0"       : pd("Pm_h0", "A0" ,"tanb" ),
            "data_histograms/iHist_A0_tanb_pred_Bsmumu"      : pd("Pbsmm", "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_R(b->sg)"    : pd("PRbsg", "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_R(D_ms)"     : pd("PRDms", "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_R(B->taunu)" : pd("PRBtaunu", "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_R(B->Xsll)"  : pd("PRBXsll", "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_R(K->lnu)"   : pd("PRKlnu", "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_Delta(g-2)"  : pd("PDeltag2", "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_MW"          : pd("PMW", "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_sintheta_eff": pd("Psintheta_eff", "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_Gamma_Z"     : pd("PGamma_Z"     , "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_Rl"          : pd("PRl"          , "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_Rb"          : pd("PRb"          , "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_Rc"          : pd("PRc"          , "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_Afb(b)"      : pd("PAfbb"        , "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_Ab16"        : pd("PAb16"        , "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_Ac17"        : pd("PAc17"        , "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_Al(SLD)"     : pd("PAlSLD"        , "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_Al(P_tau)"   : pd("PAlP_tau"      , "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_Al_fb"       : pd("PAl_fb"        , "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_sigma_had^0" : pd("Psigma_had0"   , "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_R(Delta_mk)" : pd("PRDelta_mk"    , "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_R(Kp->pinn)" : pd("PRKppinn"      , "A0"  ,"tanb") , 
            "data_histograms/iHist_A0_tanb_pred_BR(Bd->ll)"  : pd("PBRBdll"       , "A0"  ,"tanb") , 


            "data_histograms/iHist_m0_tanb_chi2"             : pd("chi2", "m0",  "tanb" ),
            "data_histograms/iHist_m0_tanb_dchi"             : pd("dchi", "m0",  "tanb" ),
            "data_histograms/iHist_m0_tanb_pred_m_h^0"       : pd("Pm_h0", "m0" ,"tanb" ),
            "data_histograms/iHist_m0_tanb_pred_Bsmumu"      : pd("Pbsmm", "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_R(b->sg)"    : pd("PRbsg", "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_R(D_ms)"     : pd("PRDms", "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_R(B->taunu)" : pd("PRBtaunu", "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_R(B->Xsll)"  : pd("PRBXsll", "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_R(K->lnu)"   : pd("PRKlnu", "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_Delta(g-2)"  : pd("PDeltag2", "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_MW"          : pd("PMW", "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_sintheta_eff": pd("Psintheta_eff", "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_Gamma_Z"     : pd("PGamma_Z"     , "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_Rl"          : pd("PRl"          , "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_Rb"          : pd("PRb"          , "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_Rc"          : pd("PRc"          , "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_Afb(b)"      : pd("PAfbb"        , "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_Ab16"        : pd("PAb16"        , "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_Ac17"        : pd("PAc17"        , "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_Al(SLD)"     : pd("PAlSLD"        , "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_Al(P_tau)"   : pd("PAlP_tau"      , "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_Al_fb"       : pd("PAl_fb"        , "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_sigma_had^0" : pd("Psigma_had0"   , "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_R(Delta_mk)" : pd("PRDelta_mk"    , "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_R(Kp->pinn)" : pd("PRKppinn"      , "m0"  ,"tanb") , 
            "data_histograms/iHist_m0_tanb_pred_BR(Bd->ll)"  : pd("PBRBdll"       , "m0"  ,"tanb") , 



            "data_histograms/iHist_tanb_m12_chi2"             : pd("chi2", "tanb",  "m12" ),
            "data_histograms/iHist_tanb_m12_dchi"             : pd("dchi", "tanb",  "m12" ),
            "data_histograms/iHist_tanb_m12_pred_m_h^0"       : pd("Pm_h0", "tanb" ,"m12" ),
            "data_histograms/iHist_tanb_m12_pred_Bsmumu"      : pd("Pbsmm", "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_R(b->sg)"    : pd("PRbsg", "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_R(D_ms)"     : pd("PRDms", "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_R(B->taunu)" : pd("PRBtaunu", "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_R(B->Xsll)"  : pd("PRBXsll", "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_R(K->lnu)"   : pd("PRKlnu", "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_Delta(g-2)"  : pd("PDeltag2", "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_MW"          : pd("PMW", "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_sintheta_eff": pd("Psintheta_eff", "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_Gamma_Z"     : pd("PGamma_Z"     , "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_Rl"          : pd("PRl"          , "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_Rb"          : pd("PRb"          , "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_Rc"          : pd("PRc"          , "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_Afb(b)"      : pd("PAfbb"        , "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_Ab16"        : pd("PAb16"        , "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_Ac17"        : pd("PAc17"        , "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_Al(SLD)"     : pd("PAlSLD"        , "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_Al(P_tau)"   : pd("PAlP_tau"      , "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_Al_fb"       : pd("PAl_fb"        , "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_sigma_had^0" : pd("Psigma_had0"   , "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_R(Delta_mk)" : pd("PRDelta_mk"    , "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_R(Kp->pinn)" : pd("PRKppinn"      , "tanb"  ,"m12") , 
            "data_histograms/iHist_tanb_m12_pred_BR(Bd->ll)"  : pd("PBRBdll"       , "tanb"  ,"m12") , 



            "data_histograms/iHist_mA0_tanb_chi2"             : pd("chi2", "MA",  "tanb" ),
            "data_histograms/iHist_mA0_tanb_dchi"             : pd("dchi", "MA",  "tanb" ),
            "data_histograms/iHist_mA0_tanb_pred_m_h^0"       : pd("Pm_h0", "MA" ,"tanb" ),
            "data_histograms/iHist_mA0_tanb_pred_Bsmumu"      : pd("Pbsmm", "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_R(b->sg)"    : pd("PRbsg", "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_R(D_ms)"     : pd("PRDms", "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_R(B->taunu)" : pd("PRBtaunu", "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_R(B->Xsll)"  : pd("PRBXsll", "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_R(K->lnu)"   : pd("PRKlnu", "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_Delta(g-2)"  : pd("PDeltag2", "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_MW"          : pd("PMW", "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_sintheta_eff": pd("Psintheta_eff", "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_Gamma_Z"     : pd("PGamma_Z"     , "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_Rl"          : pd("PRl"          , "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_Rb"          : pd("PRb"          , "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_Rc"          : pd("PRc"          , "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_Afb(b)"      : pd("PAfbb"        , "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_Ab16"        : pd("PAb16"        , "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_Ac17"        : pd("PAc17"        , "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_Al(SLD)"     : pd("PAlSLD"        , "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_Al(P_tau)"   : pd("PAlP_tau"      , "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_Al_fb"       : pd("PAl_fb"        , "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_sigma_had^0" : pd("Psigma_had0"   , "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_R(Delta_mk)" : pd("PRDelta_mk"    , "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_R(Kp->pinn)" : pd("PRKppinn"      , "MA"  ,"tanb") , 
            "data_histograms/iHist_mA0_tanb_pred_BR(Bd->ll)"  : pd("PBRBdll"       , "MA"  ,"tanb") , 








#            "data_histograms/iHist_m0_tanb_chi2"        : pd("chi2", "m0",  "tanb" ),
#            "data_histograms/iHist_m0_tanb_dchi"        : pd("dchi", "m0",  "tanb" ),
#            "data_histograms/iHist_tanb_m12_chi2"       : pd("chi2", "tanb","m12" ),
#            "data_histograms/iHist_tanb_m12_dchi"       : pd("dchi", "tanb","m12" ),
#            "data_histograms/iHist_mA0_tanb_chi2"       : pd("chi2", "MA"  ,"tanb"),
#            "data_histograms/iHist_mA0_tanb_dchi"       : pd("dchi", "MA"  ,"tanb"),
#            "data_histograms/iHist_mA0_tanb_pred_m_h^0"     : pd("Pm_h0", "MA"  ,"tanb"),
#            "data_histograms/iHist_mA0_tanb_pred_R(b->sg)": pd("PRbsg", "MA"  ,"tanb"),
#            "data_histograms/iHist_mA0_tanb_pred_Bsmumu"    : pd("Pbsmm", "MA"  ,"tanb"),
         }

grid_hists=OrderedDict()
grid_hists={
#            "data_histograms/iHist_gluino_dchi"        : pd("dchi", "mg"   ),
#            "data_histograms/iHist_gluino_chi2"        : pd("chi2", "mg"   ),
#            "data_histograms/iHist_stau_1_dchi"        : pd("dchi","mstau1"),
#            "data_histograms/iHist_stau_1_chi2"        : pd("chi2","mstau1"),
#            "data_histograms/iHist_stop1_dchi"         : pd("dchi", "stop1" ),
#            "data_histograms/iHist_stop1_chi2"         : pd("chi2", "stop1" ),
#            "data_histograms/iHist_squark_r_dchi"      : pd("dchi", "msqr" ),
#            "data_histograms/iHist_squark_r_chi2"      : pd("chi2", "msqr" ),
#            "data_histograms/iHist_BsmumuRatio_dchi"   : pd("dchi", "bsmmratio" ),
#            "data_histograms/iHist_BsmumuRatio_chi2"   : pd("chi2", "bsmmratio" ),
           }

