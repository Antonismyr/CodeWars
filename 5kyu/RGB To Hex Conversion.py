import numpy as np 
def rgb(r, g, b):
    r = format(np.clip(round(r), 0, 255), '02X')
    g = format(np.clip(round(g), 0, 255), '02X')
    b = format(np.clip(round(b), 0, 255), '02X')
    return ''.join([r,g,b])