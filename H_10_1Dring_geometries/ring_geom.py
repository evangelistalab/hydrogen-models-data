import numpy as np

def get_h10ring_geom(r):
    phi_o = 2 * np.pi / 10
    rad_denom = 2 * np.sin(np.pi/10)
    rad = r / rad_denom

    a1x = rad * np.cos(phi_o * 0)
    a2x = rad * np.cos(phi_o * 1)
    a3x = rad * np.cos(phi_o * 2)
    a4x = rad * np.cos(phi_o * 3)
    a5x = rad * np.cos(phi_o * 4)
    a6x = rad * np.cos(phi_o * 5)
    a7x = rad * np.cos(phi_o * 6)
    a8x = rad * np.cos(phi_o * 7)
    a9x = rad * np.cos(phi_o * 8)
    a10x = rad * np.cos(phi_o * 9)


    a1y = rad * np.sin(phi_o * 0)
    a2y = rad * np.sin(phi_o * 1)
    a3y = rad * np.sin(phi_o * 2)
    a4y = rad * np.sin(phi_o * 3)
    a5y = rad * np.sin(phi_o * 4)
    a6y = rad * np.sin(phi_o * 5)
    a7y = rad * np.sin(phi_o * 6)
    a8y = rad * np.sin(phi_o * 7)
    a9y = rad * np.sin(phi_o * 8)
    a10y = rad * np.sin(phi_o * 9)

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
