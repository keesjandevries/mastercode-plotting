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
          "mneu1" : 500,
          "ssi"   : 10e-40,
          "mh"    : 5,
          "MA"    : 500,
          "mstau1": 500,
          "mg"    : 500,
          "msqr"  : 500,
          "bsmm"  : 2e-9,
        }

m0m12Base   = { "xticks" : ticks["m0"],   "yticks" : ticks["m12"],  }
m0tanbBase  = { "xticks" : ticks["m0"],   "yticks" : ticks["tanb"], }
tanbm12Base = { "xticks" : ticks["tanb"], "yticks" : ticks["m12"],  }
MAtanbBase  = { "xticks" : ticks["MA"  ], "yticks" : ticks["tanb"], }
mneu1ssiBase= { "xticks" : ticks["mneu1"],"yticks" : ticks["ssi"],  }
mstau1Base  = { "xticks" : ticks["mstau1"],}
mgBase      = { "xticks" : ticks["mg"],    }
msqrBase    = { "xticks" : ticks["msqr"],  }
bsmmBase    = { "xticks" : ticks["bsmm"],  }
mhBase      = { "xticks" : ticks["mh"], }
mneu1Base   = { "xticks" : ticks["mneu1"], }

# per type
colors  = [ 'r', 'b' ]

chi2Base = { 
               "title"    : r"$\chi^{2}$",
               "contours" : [22.23, 25.99], # need more sensible values
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
                "contours" : [2.23, 5.99],
                "colors"   : colors,
                "zrange"   : [0.,  7.],
                "zrange1d" : [0., 9.],
           }

PbsmmBase = {
                "title"    : r"Prediction for $BR(B_{s}\rightarrow\mu\mu) $  ",
                "contours" : [2.23, 5.99],
                "colors"   : colors,
                "zrange"   : [0., 6.92e-9  ],
                "zrange1d" : [0., 9.],
           }
