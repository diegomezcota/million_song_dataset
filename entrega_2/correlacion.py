#matriz correlacion
import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt

# MY_VARIABLE_INDEX = 0

# load array
data = loadtxt('data.csv', delimiter=',')
mat = np.corrcoef(data)

print(data)
print(mat)