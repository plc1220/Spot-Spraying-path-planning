import numpy as np
from Categorization import lin_categorize, height_categorize
from Slicing import slicing, zigzag
from Polygon import Concave_hull

def F(sm,sl,di,dlist,PCY,PCX):
    m = sm**3
    layer = int(sl)
    c = PCY - m*PCX
    pdata = Concave_hull(dlist,m)[4]
    d = lin_categorize(dlist,m,layer,pdata)
    zzlist = zigzag(slicing(d,m,di))
    # Arrange original list
    arr = np.array(dlist)
    path = arr[zzlist]

    return path,m,c

def F2(sh, dlist):
    dh = sh
    d = height_categorize(dlist,dh)
    zzlist = zigzag(slicing(d,0.3,0))
    arr = np.array(dlist)
    path = arr[zzlist]

    return path
