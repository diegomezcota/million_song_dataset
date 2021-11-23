from numpy import loadtxt
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import anderson

# indice de song_hottness
MY_VARIABLE_INDEX = 1

# load array
data = loadtxt('data.csv', delimiter=',')
my_variable_data = data[MY_VARIABLE_INDEX]

# ver como analizarlo en https://www.statology.org/anderson-darling-test-python/
print(anderson(my_variable_data))
