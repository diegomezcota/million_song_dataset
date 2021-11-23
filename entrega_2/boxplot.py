from numpy import loadtxt
import matplotlib.pyplot as plt

# indice de tempo
MY_VARIABLE_INDEX = 0

# load array
data = loadtxt('data.csv', delimiter=',')
my_variable_data = data[MY_VARIABLE_INDEX]

plt.boxplot(my_variable_data)

plt.show()