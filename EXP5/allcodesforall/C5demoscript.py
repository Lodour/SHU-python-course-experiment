#coding:utf-8
## -*- coding : gbk -*-

from __future__ import print_function
from math import pi as PI
import types
import collections
import random
import math
import fractions

def fib(n):
    a, b = 1, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print('\n')

def fib1(n):
    '''accept an integer n. return the numbers 
    less than n in Fibonacci sequence.'''
    a, b = 1, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print('\n')

def dm1(newitem,old_list=[]):
    old_list.append(newitem)
    return old_list

def dm2(newitem,old_list=None):
    if old_list is None:
        old_list=[]
    old_list.append(newitem)
    return old_list

#1
def CircleArea(r):
    if isinstance(r,int) or isinstance(r,float):
        #确保接收的参数为数值
        return PI*r*r
    else:
        print('You must give me an integer or float as radius.')

#2
def demo2(*para):
    avg = sum(para)/len(para) 
    g = [i for i in para if i>avg]
    return (avg,)+tuple(g)

#3
def demo3(s):
    result = [0,0]
    for ch in s:
        if 'a'<=ch<='z':
            result[1] += 1
        elif 'A'<=ch<='Z':
            result[0] += 1
    return result

#4
def demo4(lst,k):
    x = lst[:k]
    x.reverse()
    y = lst[k:]
    y.reverse()
    r = x+y
    r.reverse()
    return r

#5
def demo5():
    x = range(20)
    print(x)
    x = collections.deque(x)
    print(x)
    x.rotate(-3)
    print(x)
    x=list(x)
    print(x)
    
#6
def demo6(t):
    a, b = 1, 1
    while b<t:
        a, b = b, a+b
    else:
        return b

#7
def demo7(lst):
    m = min(lst)
    result = (m,)
    for index, value in enumerate(lst):
        if value==m:
            result = result+(index,)
    return result

#8
def demo8(t):
    print([1])
    print([1,1])
    line = [1,1]
    for i in range(2,t):
        r = []
        for j in range(0,len(line)-1):
            r.append(line[j]+line[j+1])
        line = [1]+r+[1]
        print(line)

#9
def IsPrime(n):
    m = int(math.sqrt(n))+1
    for i in range(2, m):
        if n%i==0:
            return False
    return True
def demo9(n):
    if isinstance(n,int) and n>0 and n%2==0:
        for i in range(3, int(n/2)+1):
            if IsPrime(i) and IsPrime(n-i):
                print(i, '+', n-i, '=', n)

#10
def demo10(m,n):
    if m>n:
        m, n = n, m
    p = m*n
    while m!=0:
        r = n%m
        n = m
        m = r
    return (int(p/n),n)

#生成器
def func1():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b

#嵌套定义
def linear(a, b):
    def result(x):
        return a * x + b
    return result

def main():
    fib(1000)
    x=input('demo:')
    fib1(1000)
    x=input('demo:')
    print(dm1('5',[1,2,3,4]))
    print(dm1('aaa',['a','b']))
    print(dm1('a'))   
    print(dm1('b'))
    x=input('demo:')
    print(dm2('5',[1,2,3,4]))
    print(dm2('aaa',['a','b']))
    print(dm2('a'))   
    print(dm2('b'))
    x=input('demo:')
    #1
    print(CircleArea(3))
    x=input('demo:')
    #2
    print(demo2(1,2,3,4))
    x=input('demo:')
    #3
    print(demo3('aaaabbbbC'))
    x=input('demo:')
    #4
    lst = list(range(1,21))
    print(lst)
    print(demo4(lst,5))
    x=input('demo:')
    #5
    demo5()
    x=input('demo:')
    #6
    print(demo6(50))
    x=input('demo:')
    #7
    x = [random.randint(1,20) for i in range(50)]
    print(x)
    print(demo7(x))
    x=input('demo:')
    #8
    demo8(10)
    x=input('demo:')
    #9
    demo9(60)
    x=input('demo:')
    #10
    print(demo10(20,30))
    x=input('demo:')
    print(fractions.gcd(36,39))
    print(fractions.gcd(20,30))
    print(30*20/fractions.gcd(20,30))
    x=input('demo:')
    
    #生成器
    x=input('demo:')
    #嵌套定义
    taxes = linear(0.3, 2)
    print(taxes(5))
    x=input('demo:')
    
main()
