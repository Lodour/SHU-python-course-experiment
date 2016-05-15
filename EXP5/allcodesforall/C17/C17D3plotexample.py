import numpy as np
import pylab as pl
t = np.arange(0.0, 2.0*np.pi, 0.01)
s = np.sin(t)
pl.figure(1)
ax1 = pl.subplot(1,3,1)
ax2 = pl.subplot(1,3,2)
ax3 = pl.subplot(1,3,3)

pl.sca(ax1)
pl.plot(t,s)
pl.xlabel('x')
pl.ylabel('y')
pl.title('sin')

pl.sca(ax2)
a = np.arange(0, 2.0*np.pi, 0.1)
b = np.cos(a)
pl.scatter(a,b)

pl.sca(ax3)
x = np.random.random(100)
y = np.random.random(100)
pl.scatter(x,y,s=x*500,c=u'r',marker=u'*')

pl.show()
