
from pandas import read_csv
from matplotlib import pyplot
series = read_csv('data.csv', header=0, index_col=0)
print(series)
pyplot.plot(series)
pyplot.show()