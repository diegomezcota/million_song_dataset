import os
import glob

from numpy.core.defchararray import array
import hdf5_getters
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kurtosis
from scipy.stats import skew
# save numpy array as csv file
from numpy import asarray
from numpy import savetxt

# Change for your specific path
LOCAL_PATH = "C:\\Users\\diego\\OneDrive\\Escritorio\\TEC 7mo semestre\\Metodos Cuantitativos\\Proyecto\\Canciones\\MillionSongSubset"

def get_features(basedir,ext='.h5') :
    v = []
    w = []
    x = []
    y = []
    z = []
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            h5 = hdf5_getters.open_h5_file_read(f)
            # sacamos los atributos de la cancion
            v.append(hdf5_getters.get_artist_hotttnesss(h5))
            w.append(hdf5_getters.get_duration(h5))
            x.append( hdf5_getters.get_song_hotttnesss(h5))
            y.append(hdf5_getters.get_artist_familiarity(h5))
            z.append(hdf5_getters.get_tempo(h5))
            h5.close()

    return (v, w, x, y, z)

arr1, arr2, arr3, arr4, arr5 = get_features(LOCAL_PATH)

np_arr1, np_arr2, np_arr3, np_arr4, np_arr5 = np.array(arr1), np.array(arr2), np.array(arr3), np.array(arr4), np.array(arr5)

mask = np.logical_and.reduce((~np.isnan(arr1), ~np.isnan(arr2), ~np.isnan(arr3), ~np.isnan(arr4), ~np.isnan(arr5)))

v = np_arr1[mask]
w = np_arr2[mask]
x = np_arr3[mask]
y = np_arr4[mask]
z = np_arr5[mask]

print(len(v))
print(len(w))
print(len(x))
print(len(y))
print(len(z))

data = [v, w, x, y, z]

# save to csv file
savetxt('data.csv', data, delimiter=',')

# print("Media")
# print(np.average(x))
# print("Varianza")
# print(np.var(x))
# print("Desviacion estandar")
# print(np.std(x))
# print("Simetria")
# print(skew(x))
# print("Curtosis")
# print(kurtosis(x))