from pylab import *
def f(x):
    y = x**2
    return y
for i in range(-10,10):
    x=i
    plot(x,f(x),'*')
show()