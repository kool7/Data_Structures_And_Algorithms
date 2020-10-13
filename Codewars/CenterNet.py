import numpy as np
import pandas as pd
import keras
from keras.layers import Dense, Activation, Input, Conv2D, BatchNormalization, Add, UpSampling2D, ZeroPadding2D, Lambda


# Conversion from string to coordinates.

def str_to_coords(s, names=['id', 'yaw', 'pitch', 'roll', 'x', 'y', 'z']):
    coords = []
    for l in np.array(s.split()).reshape([-1, 7]):
        coords.append(dict(zip(names, l.astype('float'))))
        if 'id' in coords[-1]:
            coords[-1]['id'] = int(coords[-1]['id'])
        return coords

def coords_to_str(coords):
    s = []
    for c in coords:
        s.append(str(c[n]))
    return ' '.join(s)