def file_name( filename ) :
    basename = filename.split('/')[-1]
    no_extension = "".join(basename.split('.')[:-1])
    return no_extension

def grid_name( filename ) :
    fname = file_name( filename )
    return "%s_grid" % fname

def fig_name( fig, filename ) :
    fname = file_name( filename )
    name_format = "%s"
    name_format += "_%s"*len( fig["short_names"] )
    name_format += "_%s"
    name = name_format % ( tuple( [fname] + fig["short_names"] + [ fig["mode"] ] ) )
    return name
    
