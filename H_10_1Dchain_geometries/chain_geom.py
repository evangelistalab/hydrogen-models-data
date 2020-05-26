def get_h10chain_geom(r):

    a1z = 9.*r/2
    a2z = 7.*r/2
    a3z = 5.*r/2
    a4z = 3.*r/2
    a5z = r/2.
    a6z = -r/2.
    a7z = -3.*r/2
    a8z = -5.*r/2
    a9z = -7.*r/2
    a10z = -9.*r/2

    g1 = '         '
    g2 = '     '


    geom =  'H' + g1 + str(0.00)  + g2 + str(0.00)  + g2 + str(a1z)  + '\n' + \
            'H' + g1 + str(0.00)  + g2 + str(0.00)  + g2 + str(a2z)  + '\n' + \
            'H' + g1 + str(0.00)  + g2 + str(0.00)  + g2 + str(a3z)  + '\n' + \
            'H' + g1 + str(0.00)  + g2 + str(0.00)  + g2 + str(a4z)  + '\n' + \
            'H' + g1 + str(0.00)  + g2 + str(0.00)  + g2 + str(a5z)  + '\n' + \
            'H' + g1 + str(0.00)  + g2 + str(0.00)  + g2 + str(a6z)  + '\n' + \
            'H' + g1 + str(0.00)  + g2 + str(0.00)  + g2 + str(a7z)  + '\n' + \
            'H' + g1 + str(0.00)  + g2 + str(0.00)  + g2 + str(a8z)  + '\n' + \
            'H' + g1 + str(0.00)  + g2 + str(0.00)  + g2 + str(a9z)  + '\n' + \
            'H' + g1 + str(0.00)  + g2 + str(0.00)  + g2 + str(a10z)

    return geom
