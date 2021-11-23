import os
import glob
import hdf5_getters
import numpy as np
import matplotlib.pyplot as plt

def get_all_titles(basedir,ext='.h5') :
    x = []
    y = []
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            h5 = hdf5_getters.open_h5_file_read(f)
            # sacamos los atributos de la cancion
            x.append( hdf5_getters.get_tempo(h5))
            y.append( hdf5_getters.get_duration(h5))
            h5.close()

    return (x, y)

array1, array2 = get_all_titles("C:\\Users\\diego\\OneDrive\\Escritorio\\TEC 7mo semestre\\Metodos Cuantitativos\\Proyecto\\Canciones\\MillionSongSubset")

np_array1 = np.array(array1)
np_array2 = np.array(array2)

plt.scatter(np_array1,np_array2)
plt.show()
