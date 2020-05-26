import numpy as np

def get_h10pyr_geom(r):
    hpyr = np.sqrt(2.0/3) * r
    htri = np.cos(np.pi / 6.0) * r

    a1x =  0.0
    a2x = -0.5 * r
    a3x =  0.5 * r
    a4x = -r
    a5x =  0.0
    a6x =  r
    a7x =  0.0
    a8x = -0.5 * r
    a9x =  0.5 * r
    a10x = 0.0

    a1y =  (4.0/3) * htri
    a2y =  (1.0/3) * htri
    a3y =  (1.0/3) * htri
    a4y = -(2.0/3) * htri
    a5y = -(2.0/3) * htri
    a6y = -(2.0/3) * htri
    a7y =  (2.0/3) * htri
    a8y = -(1.0/3) * htri
    a9y = -(1.0/3) * htri
    a10y =  0.0

    a1z = -hpyr
    a2z = -hpyr
    a3z = -hpyr
    a4z = -hpyr
    a5z = -hpyr
    a6z = -hpyr
    a7z =  0.0
    a8z =  0.0
    a9z =  0.0
    a10z = hpyr

    g1 = '         '
    g2 = '     '


    geom =  'H' + g1 + str(a1x)  + g2 + str(a1y)  + g2 + str(a1z)  + '\n' + \
            'H' + g1 + str(a2x)  + g2 + str(a2y)  + g2 + str(a2z)  + '\n' + \
            'H' + g1 + str(a3x)  + g2 + str(a3y)  + g2 + str(a3z)  + '\n' + \
            'H' + g1 + str(a4x)  + g2 + str(a4y)  + g2 + str(a4z)  + '\n' + \
            'H' + g1 + str(a5x)  + g2 + str(a5y)  + g2 + str(a5z)  + '\n' + \
            'H' + g1 + str(a6x)  + g2 + str(a6y)  + g2 + str(a6z)  + '\n' + \
            'H' + g1 + str(a7x)  + g2 + str(a7y)  + g2 + str(a7z)  + '\n' + \
            'H' + g1 + str(a8x)  + g2 + str(a8y)  + g2 + str(a8z)  + '\n' + \
            'H' + g1 + str(a9x)  + g2 + str(a9y)  + g2 + str(a9z)  + '\n' + \
            'H' + g1 + str(a10x) + g2 + str(a10y) + g2 + str(a10z)

    return geom
