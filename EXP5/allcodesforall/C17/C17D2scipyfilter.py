#coding:utf-8
## -*- coding : gbk -*-
import random
import numpy as np
import scipy.signal as signal

print "\nExample 1"
x = np.arange(0,100,10)
random.shuffle(x)
print x
print signal.medfilt(x,3)

print "\nExample 2"
x = np.arange(0,2,0.1)
y = np.sin(x)
z = y.copy()
print '='*20
print 'y:'
print y
print '='*20
print 'before adding noise.z-y:'
print z-y
index = np.random.randint(0,len(x),20)
noise = np.random.standard_normal(20)*0.8
z[index]+=noise
print '='*20
print 'after adding noise.z-y:'
print z-y
result = signal.medfilt(z,3)
print '='*20
print 'after stripe 3 median filtering.z-y:'
print result-y
