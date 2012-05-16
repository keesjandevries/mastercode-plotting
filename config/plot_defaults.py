def getDefaults( mode, *axes ) :
    d = {}
    d.update(spaceBases[ "".join(axes) ])
    d.update( typeBases[mode] )
    d["short_names"] = list(axes)
    d["mode"] = mode
    return d

# per value
ticks = { 
          "m0"    : 500,
          "m12"   : 500,
          "tanb"  : 10,
          "neu1"  : 100,
          "m_h^0" : 5,
        }

spaceBases = {
    "m0m12"   : { "xticks" : ticks["m0"],   "yticks" : ticks["m12"],  },
    "m0tanb"  : { "xticks" : ticks["m0"],   "yticks" : ticks["tanb"], },
    "tanbm12" : { "xticks" : ticks["tanb"], "yticks" : ticks["m12"],  },
    "neu1"    : { "xticks" : ticks["neu1"], },
    "m_h^0"   : { "xticks" : ticks["m_h^0"], },
}

# per type
colors  = [ 'r', 'b' ]

typeBases = {
    "chi2" : { 
        "title"    : r"$\chi^{2}$",
        "contours" : [22.23, 25.99], # need more sensible values
        "colors"   : colors, 
        "zrange"   : [20., 45.]
    },

    "pval" : {
        "title"    : r"$P(\chi^{2},N_{DOF})$",
        "contours" : [0.05, 0.1],
        "colors"   : colors,
        "zrange"   : [0., 0.2],
    },

    "dchi" : {
        "title"    : r"$\Delta\chi^{2}$",
        "contours" : [2.23, 5.99],
        "colors"   : colors,
        "zrange"   : [0., 25.],
        "zrange1d" : [0., 9.],
    },
}
