def getDefaults( mode, *axes ) :
    axes_format = "%s"*len(axes)
    format_string = "dict(" + axes_format + "Base.items() +%sBase.items())"
    return eval( format_string % tuple( list(axes) + [mode] ) )

# per value
m0m12Base   = { "xticks" : ticks["m0"],   "yticks" : ticks["m12"],  }
m0tanbBase  = { "xticks" : ticks["m0"],   "yticks" : ticks["tanb"], }
tanbm12Base = { "xticks" : ticks["tanb"], "yticks" : ticks["m12"],  }
neu1Base    = { "xticks" : ticks["neu1"], } 
mhBase = { "xticks" : ticks["mh"], } 

ticks = { 
          "m0"   : 500,
          "m12"  : 500,
          "tanb" : 10,
          "neu1" : 100,
          "mh"   : 5,
        }


# per type

colors = [ 'r', 'b' ]
clevels = { 
              "dchi" : [2.23,5.99],
              "pval" : [0.05,0.10],
          }

chi2Base = { 
               "title"    : r"$\chi^{2}$",
               "contours" : cLevelDelta(20.), 
               "colors"   : colors, 
               "zrange"   : [20., 45.]
           }

pvalBase = {
                "title"    : r"$P(\chi^{2},N_{DOF})$",
                "contours" : clevels["pval"],
                "colors"   : colors,
                "zrange"   : [0., 0.2],
           }

dchiBase = {
                "title"    : r"$\Delta\chi^{2}$",
                "contours" : clevels["dchi"],
                "colors"   : colors,
                "zrange"   : [0., 25.],
                "zrange1d" : [0., 9.],
           }

def cLevelDelta( delta = 0.0 ) :
    return [ x+delta for x in clevels["dchi"] ] 
