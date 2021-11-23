from numpy import loadtxt
import matplotlib.pyplot as plt
from scipy.stats import kurtosis
from scipy.stats import skew
import numpy as np

# indice de song_hottness
MY_VARIABLE_INDEX = 2

# load array
data = loadtxt('data.csv', delimiter=',')
my_variable_data = data[MY_VARIABLE_INDEX]

print("Media")
print(np.average(my_variable_data))
print("Varianza")
print(np.var(my_variable_data))
print("Desviacion estandar")
print(np.std(my_variable_data))
print("Simetria")
print(skew(my_variable_data))
print("Curtosis")
print(kurtosis(my_variable_data))