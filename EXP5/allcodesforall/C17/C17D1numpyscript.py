#coding:utf-8
## -*- coding : gbk -*-

import numpy as np

#数据生成
print "\ninitialize array and matrix"
a = np.array((1,2,3))
print a
b = np.array(([1,2,3],[4,5,6],[7,8,9]))
print b
x = np.linspace(0,5,11)
print x
y = np.logspace(0,10,11)
print y

#数组运算
print "\narray calcualtion"
a = a*2
print a
b = b/2.0
print b
b = b+b
print b
c = a*b
print c
print c/b

#矩阵运算
print "\nmatrix calculation"
b = np.array(([1,2,3],[4,5,6],[7,8,9]))
print b
print b.T
c = np.dot(a,a)
print c
c = np.dot(b,b.T)
print c
c = np.dot(a,b)
print c

#函数运算
print "\nmath function"
print np.sin(b)
print np.round(np.sin(b))

#数组元素访问
print "\nvisiting elements"
x = np.arange(0,100,10,dtype=np.float)
print x
index = np.random.randint(0,len(x),5)
print index
noise = np.random.standard_normal(5)*0.3
print noise
print x[index]
x[index] += noise
print x[index]

#统计运算
print "\nstat"
x = np.arange(0,10).reshape(2,5)
print x
print np.sum(x)
print np.sum(x,axis=0)
print np.sum(x,axis=1)
print np.average(x,axis=0)
print np.average(x,axis=1)
x = np.random.randint(0,10,size=(3,3))
print x
print np.std(x)
print np.std(x,axis=1)
print np.var(x)
print np.max(x)
print np.max(x,axis=1)

#排序
print "\nsort"
print x
print np.sort(x)
print np.sort(x,axis=0)

#特殊矩阵
print "\nspecial matrix"
print np.zeros((3,3))
print np.ones((3,3))
print np.identity(3)
print np.empty((3,3))

#改变矩阵尺寸
print "\nreshape"
a = np.arange(1,11,1)
print a
a.shape = 2,5
print a
a.shape = 5,-1#-1表示自动计算
print a
b = a.reshape(2,5)
print b

#Slice
print "\nslice"
a = np.arange(10)
print a
print a[::-1]
print a[::2]
print a[:5]
c = np.random.randint(0,10,size=(5,5))
print c
print c[0,3:5]
print c[0]
print c[2:5,2:5]

#BOOL
print "\nBOOL"
print c>5
print c[c>5]
print np.array([1,2,3]) < np.array([3,2,1])
print np.array([1,2,3]) ==np.array([3,2,1])

#Round
print "\nround"
x = np.random.rand(10)*50
print x
print np.array([t-int(t) for t in x])

#
print "\n"
a = np.arange(0,60,10).reshape(-1,1)
b = np.arange(0,6)
print a
print b
print a+b

#分段函数
print "\nPiecewise function"
x = np.random.randint(0,10,size=(1,10))
print x
print np.where(x<5,0,1)
print np.piecewise(x,[x>7,x<3],[lambda x:x*2,lambda x:x*3])

#频次计算
print "\nfrequency"
x = np.random.randint(0,10,10)
print x
print np.bincount(x)
print np.unique(x)

#加权平均
print "\nWeighted average"
x = np.random.randint(0,10,10)
print x
y = np.array([round(i,1) for i in list(np.random.random(10))])
print y
print np.sum(x*y)/np.sum(np.bincount(x))
