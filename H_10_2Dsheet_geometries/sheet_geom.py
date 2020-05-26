import numpy as np

def get_h10sheet_geom(r):

    htri = np.cos(np.pi / 6.0) * r

    a1x = -r
    a2x =  0.0
    a3x =  r
    a4x = -(3.0/2) * r
    a5x = -r/2
    a6x =  r/2
    a7x = (3.0/2) * r
    a8x = -r
    a9x =  0.0
    a10x =  r

    a1y = htri
    a2y = htri
    a3y = htri
    a4y = 0.0
    a5y = 0.0
    a6y = 0.0
    a7y = 0.0
    a8y = -htri
    a9y = -htri
    a10y = -htri

    g1 = '         '
    g2 = '     '

    geom =  'H' + g1 + str(a1x)  + g2 + str(a1y)  + g2 + str(0.00)  + '\n' + \
            'H' + g1 + str(a2x)  + g2 + str(a2y)  + g2 + str(0.00)  + '\n' + \
            'H' + g1 + str(a3x)  + g2 + str(a3y)  + g2 + str(0.00)  + '\n' + \
            'H' + g1 + str(a4x)  + g2 + str(a4y)  + g2 + str(0.00)  + '\n' + \
            'H' + g1 + str(a5x)  + g2 + str(a5y)  + g2 + str(0.00)  + '\n' + \
            'H' + g1 + str(a6x)  + g2 + str(a6y)  + g2 + str(0.00)  + '\n' + \
            'H' + g1 + str(a7x)  + g2 + str(a7y)  + g2 + str(0.00)  + '\n' + \
            'H' + g1 + str(a8x)  + g2 + str(a8y)  + g2 + str(0.00)  + '\n' + \
            'H' + g1 + str(a9x)  + g2 + str(a9y)  + g2 + str(0.00)  + '\n' + \
            'H' + g1 + str(a10x) + g2 + str(a10y) + g2 + str(0.00)

    return geom
