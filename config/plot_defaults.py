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
          "m12"   : 500,
          "tanb"  : 10,
          "mneu1" : 100,
          "ssi"   : 10e-12,
          "mh"    : 5,
          "MA"    : 500,
          "mstau1": 1000,
          "mg"    : 1000,
          "msqr"  : 1000,
          "stop1"  : 1000,
          "bsmm"  : 1.0e-9,
          "bsmmratio"  : 0.5,
        }

m0m12Base   = { "xticks" : ticks["m0"],   "yticks" : ticks["m12"],  }
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

# per type
colors  = [ 'r', 'b' ]

chi2Base = { 
               "title"    : r"$\chi^{2}$",
               "contours" : [0.   , 0.   ], # need more sensible values
               "colors"   : colors, 
               "zrange"   : [20., 45.]
           }

pvalBase = {
                "title"    : r"$P(\chi^{2},N_{DOF})$",
                "contours" : [0.05, 0.1],
                "colors"   : colors,
                "zrange"   : [0., 0.2],
           }

dchiBase = {
                "title"    : r"$\Delta\chi^{2}$",
                "contours" : [2.30, 5.99],
                "colors"   : colors,
                "zrange"   : [0.,  7.],
                "zrange1d" : [0., 9.],
           }

dchi_red_bandBase = {
                "title"    : r"$\Delta\chi^{2}$",
                "contours" : [2.30, 5.99],
                "colors"   : colors,
                "zrange"   : [0.,  7.],
                "zrange1d" : [0., 9.],
           }

PbsmmBase = {
                "title"    : r"Prediction for $BR(B_{s}\rightarrow\mu\mu) $  ",
                "contours" : [3.46e-9, 1],
                "colors"   : colors,
                "zrange"   : [0., 6.92e-9  ],
                "zrange1d" : [0., 6.92e-9  ],
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
                "contours" : [125,0],
                "colors"   : colors,
                "zrange"   : [122.,128.    ],
                "zrange1d" : [115.,130.    ],
           }

PMWBase = {
                "title"    : r"Prediction for $M_{W} $  ",
#                "contours" : [2.23, 5.99],
                "colors"   : colors,
                "zrange"   : [80.34834, 80.42106    ],
                "zrange1d" : [115.,130.    ],
           }
PtanbBase = {
                "title"    : r"Value of $\tan\beta $  ",
                "contours" : [0, 40],
                "colors"   : colors,
                "zrange"   : [0,60    ],
                "zrange1d" : [0.,60.    ],
           }
