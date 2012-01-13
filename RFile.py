from collections import defaultdict

class RFile( object ) :  # an individual file with a dictionary of key(folders) and
                         # data(list(histogram, property))
    def __init__( self, fname ) :
        self._filename = fname
        self._plots = defaultdict(list)

    def add_plot( self, directory, hist_name, rproperty  ) :
        self.plots[directory].append( hist_name, rproperty )


class RProperty( object ) : # an object containing all the information we would
                            # need to format a plot
    def __init__( self, hname , properties = None ) :
        self._properties( properties )
        self._name = hname
        self._logx = logx
        self._logy = logy
