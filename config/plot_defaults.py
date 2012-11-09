def getDefaults( mode, *axes ) :
    axes_format = "%s"*len(axes)
    format_string = "dict(" + axes_format + "Base.items() +%sBase.items())"
    d = eval( format_string % tuple( list(axes) + [mode] ) )
    d["short_names"] = list(axes)
    d["mode"] = mode
    return d

# per value
ticks = { 
          "m0"    :1000,
          "A0"    :1000,
          "m12"   : 500,
          "tanb"  : 10,
          "mneu1" : 100,
          "Dm_stau1_neu1" : 5,
          "Dm_nslp_lsp" :10,
          "ssi"   : 10e-12,
          "mh"    : 5,
          "MA"    : 1000,
          "mstau1": 200,
          "mg"    : 1000,
          "msqr"  : 1000,
          "stop1"  : 1000,
          "bsmm"  : 1.0e-9,
          "bsmmratio"  : 0.5,
        }

m0m12Base   = { "xticks" : ticks["m0"],   "yticks" : ticks["m12"],  }
A0tanbBase   = { "xticks" : ticks["A0"],   "yticks" : ticks["tanb"],  }
Dm_stau1_neu1mhBase   = { "xticks" : ticks["Dm_stau1_neu1"],   "yticks" : ticks["mh"],  }
mstau1Dm_stau1_neu1Base  = {  "xticks" : ticks["mstau1"],"yticks" : ticks["Dm_stau1_neu1"] , "green_band":[0,1.777,'y']  }
Dm_stau1_neu1tanbBase   = { "xticks" : ticks["Dm_stau1_neu1"],   "yticks" : ticks["tanb"], "green_band":[0,1.777,'x'] }
m0tanbBase  = { "xticks" : ticks["m0"],   "yticks" : ticks["tanb"], }
tanbm12Base = { "xticks" : ticks["tanb"], "yticks" : ticks["m12"],  }
MAtanbBase  = { "xticks" : ticks["MA"  ], "yticks" : ticks["tanb"], }
mneu1ssiBase= { "ylog" : True, "xlog" : True}
mneu1ssicmBase= { "ylog" : True, "xlog" : True}
mstau1Base  = { "xticks" : ticks["mstau1"],}
mgBase      = { "xticks" : ticks["mg"],    }
msqrBase    = { "xticks" : ticks["msqr"],  }
stop1Base    = { "xticks" : ticks["stop1"],  }
bsmmBase    = { "xticks" : ticks["bsmm"],  }
bsmmratioBase    = { "xticks" : ticks["bsmmratio"],  }
mhBase      = { "xticks" : ticks["mh"], }
mneu1Base   = { "xticks" : ticks["mneu1"], }
Dm_stau1_neu1Base   = { "xticks" : ticks["Dm_stau1_neu1"], "green_band":[0,1.777] }
Dm_nslp_lspBase   = { "xticks" : ticks["Dm_nslp_lsp"], "green_band":[0,1.777] }


# per type
colors  = [ 'r', 'b' ]

chi2Base = { 
               "title"    : r"$\chi^{2}$",
               "contours" : [0.   , 0.   ], # need more sensible values
               "colors"   : colors, 
               "zrange"   : [20, 45.],
               "zrange1d" : [20, 45.],
           }

pvalBase = {
                "title"    : r"$P(\chi^{2},N_{DOF})$",
                "contours" : [0.05, 0.1],
                "colors"   : colors,
                "zrange"   : [0., 0.2],
           }

dchiBase = {
                "title"    : r"$\Delta\chi^{2}$",
#                "title"    : r"",
                "contours" : [ 2.30,5.99],
                "colors"   : colors,
                "zrange"   : [0., 20.0],
                "zrange1d" : [0., 9.],
           }

dchi_red_bandBase = {
                "title"    : r"$\Delta\chi^{2}$",
                "contours" : [2.30, 5.99],
                "colors"   : colors,
                "zrange"   : [0.,  7.],
                "zrange1d" : [0., 4.],
           }

PbsmmBase = {
                "title"    : r"Prediction for $BR(B_{s}\rightarrow\mu\mu) $  ",
                "contours" : [ 3.e-9 , 3.46e-9, 6.95e-9 ],
                #"colors"   : colors,
                "colors"   : ["#002000","#006000","#00FF00"],
                "zrange"   : [0., 6.92e-9  ],
                "zrange1d" : [0., 6.92e-9  ],
                "colorbar" : "RdBu",
           }

POh2Base = {
                "title"    : r"Prediction for $\Omega_{CDM}h^2$  ",
#                "contours" : [2.23, 5.99],
                "colors"   : colors,
                "zrange"   : [0.090, 0.130   ], # 0.1109 +- ~ (7 x the standard deviation) ! !
                "zrange1d" : [0.075, 0.175   ],
           }

Pm_h0Base = {
                "title"    : r"Prediction for $M_{h} $  ",
                #"contours" : [122, 124, 125, 126,128],
                "contours" : [123, 125, 127],
                #"colors"   : colors,
                "colors"   : ["#002000","#006000","#00FF00"],
                "zrange"   : [122.,128.    ],
                "zrange1d" : [115.,130.    ],
           }

PMWBase = {
                "title"    : r"Prediction for $M_{W} $  ",
                "contours" : [2.23, 5.99],
                "colors"   : colors,
                "zrange"   : [80.34834, 80.42106    ],
                "zrange1d" : [115.,130.    ],
           }
PA0Base = {
                "title"    : r"Value of $A_{0} $  ",
                "contours" : [10000, 40000],
                "colors"   : colors,
                "zrange"   : [-4000,4000    ],
                "zrange1d" : [0.,60.    ],
           }
PtanbBase = {
                "title"    : r"Value of $\tan\beta $  ",
                "contours" : [1000, 4000],
                "colors"   : colors,
                "zrange"   : [0,60    ],
                "zrange1d" : [0.,60.    ],
           }
dX_mhBase = {
                "title"    : r"$ \Delta \chi^2$ from  $M_h$  ",
                "contours" : [0, 40],
                "colors"   : colors,
                "zrange"   : [0,60    ],
                "zrange1d" : [0.,60.    ],
           }

#R(b->sg)
PRbsgBase = {
                "title"    : r"Prediction for $R(b\rightarrow s\gamma)$  ",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0.877, 1.357 ],
                "zrange1d" : [115.,130.    ],
           }
#R(D_ms)
PRDmsBase = {
                "title"    : r"Prediction for $R(\Delta_{ms})$  ",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0.4296,1.5104],
                "zrange1d" : [115.,130.    ],
           }
#R(B->taunu)
PRBtaunuBase = {
                "title"    : r"Prediction for $R(B\rightarrow\tau\nu)$  ",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0.57,2.29],
                "zrange1d" : [115.,130.    ],
           }
#R(B->Xsll)
PRBXsllBase = {
                "title"    : r"Prediction for $R(B\rightarrow X_{s}\ell\ell)$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0.35,1.63],
                "zrange1d" : [115.,130.    ],
           }
#R(K->lnu)
PRKlnuBase = {
                "title"    : r"Prediction for $R(K\rightarrow\ell\nu)$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0.98,1.036],
                "zrange1d" : [115.,130.    ],
           }
#Delta(g-2)
PDeltag2Base={
                "title"    : r"Prediction for $\Delta(g-2)_{\mu}$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0.,4.8248E-09],
                "zrange1d" : [115.,130.    ],
           }
#sintheta_eff
Psintheta_effBase={
                "title"    : r"Prediction for $\sin(\theta_{eff}) (Q_{fb})$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0.23,0.2348],
                "zrange1d" : [115.,130.    ],
           }
#Gamma_Z
PGamma_ZBase={
                "title"    : r"Prediction for $\Gamma_{Z}$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [2490.184,2500.216],
                "zrange1d" : [115.,130.    ],
           }
#Rl     
PRlBase={
                "title"    : r"Prediction for $R_{\ell}$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [20.717,20.817    ],
                "zrange1d" : [115.,130.    ],
           }
#Rb     
PRbBase={
                "title"    : r"Prediction for $R_{b}$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0.21497,0.21761  ],
                "zrange1d" : [115.,130.    ],
           }
#Rc     
PRcBase={
                "title"    : r"Prediction for $R_{c}$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0.1661,0.1781  ],
                "zrange1d" : [115.,130.    ],
           }
#Afb(b) 
PAfbbBase={
                "title"    : r"Prediction for $A_{fb}(b)$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0.096,0.1024   ],
                "zrange1d" : [115.,130.    ],
           }
#Afb(c)
PAfbcBase={
                "title"    : r"Prediction for $A_{fb}(c)$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0.0637,0.0777  ],
                "zrange1d" : [115.,130.    ],
           }
#Ab16
PAb16Base={
                "title"    : r"Prediction for $A_{b}$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0.883,0.963    ],
                "zrange1d" : [115.,130.    ],
           }
#Ab17
PAc17Base={
                "title"    : r"Prediction for $A_{c}$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0.616,0.724    ],
                "zrange1d" : [115.,130.    ],
           }
#Al(SLD)
PAlSLDBase={
                "title"    : r"Prediction for $A_{\ell} (SLD)$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0.1471,0.1555  ],
                "zrange1d" : [115.,130.    ],
           }
#Al(P_tau)
PAlP_tauBase={
                "title"    : r"Prediction for $A\ell (P_{\tau})$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0.1401,0.1529  ],
                "zrange1d" : [115.,130.    ],
           }
#Al_fb   )
PAl_fbBase={
                "title"    : r"Prediction for $A\ell FB$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0.01524,0.01904],
                "zrange1d" : [115.,130.    ],
           }
#sigma_had^0
Psigma_had0Base={
                "title"    : r"Prediction for $\sigma_{had}^{0} (nb)$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [41.466,41.614],
                "zrange1d" : [115.,130.    ],
           }
#R(Delta_mk)
PRDelta_mkBase={
                "title"    : r"Prediction for $R(\Delta_{mk})$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0.8,1.36     ],
                "zrange1d" : [115.,130.    ],
           }
#R(Kp->pinn)
PRKppinnBase={
                "title"    : r"Prediction for $R(K\pi\rightarrow\pi nn)$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0.99,1.01     ],
                "zrange1d" : [115.,130.    ],
           }
#BR(Bd->ll)
PBRBdllBase={
                "title"    : r"Prediction for $BR(B_{d}\rightarrow\ell\ell$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0       ,4.0E-10],
                "zrange1d" : [115.,130.    ],
           }
#R(Dms)/R(Dmd)
PRDmsRDmdBase={
                "title"    : r"Prediction for $R(\Delta_{ms})/R(\Delta_{md})$",
                "contours" : [125,1000],
                "colors"   : colors,
                "zrange"   : [0.7392,1.2608 ],   
                "zrange1d" : [115.,130.    ],
           }
