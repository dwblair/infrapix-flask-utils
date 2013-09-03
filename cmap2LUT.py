import matplotlib as mpl
import matplotlib.cm as cm
import numpy as np
import matplotlib
 
norm = mpl.colors.Normalize(vmin=0, vmax=255)


#cmap = cm.spectral

cdict = {
    'red'  :  ((0.00, 0.00, 0.00), 
               (0.20, 0.00, 0.00),
               (0.50, 0.00, .00),
               (0.70, 1.00, 1.00),
               (1.00, 1.00, 1.00)),
    'green':  ((0.00, 0.00, 0.00), 
               (0.20, 0.00, 0.00),
               (0.50, 1.00,.50),
               (0.70, 1.00, 1.00),
               (1.00, 0.00, 0.00)),
    'blue' :  ((0.00, 0.00, 0.00), 
               (0.20, 1.00, 1.00),
    #           (0.40, 0.00, 0.00),
               (0.50, 1.00, 0.00),
               (0.70, 0.00, 0.00), 
               (1.00, 0.00, 0.00)),
    }


cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap',cdict,256)
 
m = cm.ScalarMappable(norm=norm, cmap=cmap)
for i in range(0,256):
    vals=m.to_rgba(i)
    print str(i) + "," + str(int(vals[0]*255)) + "," + str(int(vals[1]*255))+","+str(int(vals[2]*255))
