#1
import numpy
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.figure import Figure

print(numpy.__version__)

# Import `numpy` as `np`
import numpy as np

#2
# Make the array `my_array`
my_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=np.int64)

# Print `my_array`
print(my_array)

#3
# Create an array of ones
a = np.ones((3,4))
print(a)
print('---')
# Create an array of zeros
a = np.zeros((2,3,4),dtype=np.int16)
print(a)
print('---')

# Create an array with random values
a = np.random.random((2,2))
print(a)
print('---')

# Create an empty array
a = np.empty((3,2))
print(a)
print('---')

# Create a full array
a = np.full((2,2),7)
print(a)
print('---')

# Create an array of evenly-spaced values
a = np.arange(10,25,5)
print(a)
print('---')

# Create an array of evenly-spaced values
a = np.linspace(0,2,9)
print(a)
print('---')

a = np.zeros((3,2,6))
print(a)
print('---')

sandy = np.loadtxt('data-asli.txt',delimiter=',', unpack=False, skiprows=1)
a = sandy
print(a)

np.savetxt('data-out.txt', a, delimiter=';')

#check dim
my_array = a
# Print the number of `my_array`'s dimensions
print(my_array.ndim)

# Print the number of `my_array`'s elements
print(my_array.size)

# Print information about `my_array`'s memory layout
print(my_array.flags)

# Print the length of one array element in bytes
print(my_array.itemsize)

# Print the total consumed bytes by `my_array`'s elements
print(my_array.nbytes)

# Initialize `x`
x = np.ones((3,4))

# Check shape of `x`
print(x.shape)

# Initialize `y`
y = np.ones((3,4))

# Check shape of `y`
print(y.shape)

# Add `x` and `y`
z = x + y
print(z)
print('-' * 5)


# PENJUMLAHAN
# Import `numpy` as `np`
import numpy as np

# Initialize `x` and `y`
x = np.ones((3,4))
y = np.random.random((5,1,4))

# Add `x` and `y`
x + y

# PENJUMLAHAN BEDA DIMENSI
# Import `numpy` as `np`
import numpy as np

# Initialize `x` and `y`
x = np.ones((3,4))
y = np.ones((3,1))

# Add `x` and `y`
z = x - y
print(z)
print('beda-'*4)

print(np.sqrt(z))

import matplotlib.pyplot as plt
print(sandy)
x = sandy[0:]
print('x'*4)
print(x)
print('x'*4)

from pandas import Series
from matplotlib import pyplot
series = Series.from_csv('data.txt')
pyplot.plot(series)
pyplot.show()

#DJANGO APP
fig = Figure()
canvas = FigureCanvas(fig)
response = HttpResponse( content_type = 'image/png')
canvas.print_png(response)