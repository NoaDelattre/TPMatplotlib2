from pylab import *
def f(x):
    y=2
    return y

listex=[]
listey=[]

for i in range(0,8):
    x=2
    y=f(x)
    listex.append(x)
    listey.append(y)

plot(x,y,'--*')

show()