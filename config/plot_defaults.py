def getDefaults( mode, *axes ) :
    axes_format = "%s"*len(axes)
    format_string = "dict(" + axes_format + "Base.items() +%sBase.items())"
    d = eval( format_string % tuple( list(axes) + [mode] ) )
    d["short_names"] = list(axes)
    d["mode"] = mode
    return d

# per value
ticks = { 
          "m0"    : 500,
          "m12"   : 500,
          "tanb"  : 10,
          "mneu1" : 100,
          "mh"    : 5,
        }

m0m12Base   = { "xticks" : ticks["m0"],   "yticks" : ticks["m12"],  }
m0tanbBase  = { "xticks" : ticks["m0"],   "yticks" : ticks["tanb"], }
tanbm12Base = { "xticks" : ticks["tanb"], "yticks" : ticks["m12"],  }
mneu1Base   = { "xticks" : ticks["mneu1"], }
mhBase      = { "xticks" : ticks["mh"], }

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
                "zrange"   : [0., 25.],
                "zrange1d" : [0., 9.],
           }
