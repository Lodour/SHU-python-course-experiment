#coding:utf-8
# -*- coding : gbk -*-

import time
import random
import math
import collections
import os

#1列表例示
##[10, 20, 30, 40]
##['crunchy frog', 'ram bladder', 'lark vomit']
##['spam', 2.0, 5, [10, 20]]
##[['file1', 200,7], ['file2', 260,9]]

#2列表创建
##a_list = ['a', 'b', 'mpilgrim', 'z', 'example']
##a_list = [] 
##a_list = list((3,5,7,9,11))
##list(range(1,10,2))
##list('hello world')
##x = list() 

#3Xrange
def func1():
    import time
    start = time.time()
    for j in range(100000000):
        1+1
    print time.time()-start
    start = time.time()
    for j in xrange(100000000):
        1+1
    print time.time()-start

#4增加列表元素
# +
def func11():
    aList = [3,4,5]
    print aList
    print id(aList)
    aList = aList + [7]
    print aList
    print id(aList)
    # append
    aList.append(9)
    print aList
    print id(aList)
    
#比较
def func2():
    import time
    result = []
    start = time.time()
    for i in range(10000):
        result = result + [i]
    print(len(result), ',', time.time()-start)
    result = []
    start = time.time()
    for i in range(10000):
        result.append(i)
    print(len(result), ',', time.time()-start)
    
#关于序列修改的内存变化
def func21():
    a = [1,2,3]
    print id(a)
    a = [1,2]
    print id(a)
    a = [1,2,4]
    b = [1,2,3]
    print a == b
    print id(a) == id(b)
    print id(a[0]) == id(b[0])
    a = [1,2,3]
    print id(a)
    a.append(4)
    print id(a)
    a.remove(3)
    print a
    print id(a)
    a[0] = 5
    print a
    print id(a)
    #extend
    a.extend([7,8,9])
    print a
    print id(a)
    a.extend([11,13])
    print a
    a.extend((15,17))
    print a
    #list
    a.insert(3,6)
    print a

#时间消耗比较
def Insert():
    a = []
    for i in range(10000):
        a.insert(0, i)
def Append():
    a = []
    for i in range(10000):
        a.append(i)
def func3():
    start = time.time()
    for i in range(10):
        Insert()
    print 'Insert:', time.time()-start
    start = time.time()
    for i in range(10):
        Append()
    print 'Append:', time.time()-start
    
# *
def func31():
    aList = [3,5,7]
    bList = aList
    print id(aList)
    print id(bList)
    aList = aList*3
    print aList
    print bList
    print id(aList)
    print id(bList)
    # *实质
    x = [[None] * 2] * 3
    print x
    x[0][0] = 5
    print x
    x = [[1,2,3]]*3
    x[0][0] = 10
    print x

#5删除
#del
def func41():
    a_list = [3,5,7,9,11]
    del a_list[1]
    print a_list
    #pop
    a_list = list((3,5,7,9,11))
    a_list.pop()
    print a_list
    a_list.pop(1)
    print a_list
    #remove
    a_list = [3,5,7,9,7,11]
    a_list.remove(7)
    print a_list
    
#remove 循环
def func4(x):
    print x
    for i in x:
        if i == 1:
            x.remove(i)
    print x
###修正
#1
def func5(x):
    print x
    for i in x[::]:
        if i == 1:
            x.remove(i)
    print x
#2
def func6(x):
    print x
    for i in range(len(x)-1,-1,-1):
        if x[i]==1:
            del x[i]
            #x.remove(x[i]) 
    print x

#6访问计数
def func61(aList):
    #下标
    print aList[3]
    aList[3] = 5.5
    print aList
    print aList[15]
    #index
    print aList
    print aList.index(7)
##    print aList.index(100)
    #计数
    print aList
    print aList.count(7)
    print aList.count(0)
    print aList.count(8)

#7成员
def func62():
    aList=[3, 4, 5, 5.5, 7, 9, 11, 13, 15, 17]
    print 3 in aList
    print 18 in aList
    bList = [[1], [2], [3]]
    print 3 in bList
    print 3 not in bList
    print [3] in bList
    aList = [3, 5, 7, 9, 11]
    bList = ['a', 'b', 'c', 'd']
    print (3, 'a') in zip(aList, bList)
    print zip(aList, bList)
    for a, b in zip(aList, bList):
        print(a, b)

#8切片
#取值
def func63():
    aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
    print aList[::]
    print aList[::-1]
    print aList[::2]
    print aList[1::2]
    print aList[3::]
    print aList[3:6]
    print aList[3:6:1]
    print aList[0:100:1]
    print aList[100:]
    #修改内容
    aList = [3, 5, 7]
    print aList[len(aList):]
    aList[len(aList):] = [9]
    print aList
    aList[:3] = [1, 2, 3]
    print aList
    aList[:3] = []
    print aList
    aList = list(range(10))
    print aList
    aList[::2] = [0]*(len(aList)//2)
    print aList
    #删除元素
    aList = [3,5,7,9,11]
    del aList[:3]
    print aList
    #返回浅拷贝
    ##正常赋值
    aList = [3, 5, 7]
    bList = aList #bList与aList指向同一个内存
    print bList
    bList[1] = 8
    print aList
    print aList == bList
    print aList is bList
    print id(aList) 
    print id(bList)
    ##浅复制
    aList = [3, 5, 7]
    bList = aList[::] #浅复制
    print aList == bList
    print aList is bList
    print id(aList) == id(bList)
    bList[1] = 8
    print bList
    print aList
    print aList == bList
    print aList is bList
    print id(aList)
    print id(bList)

#8排序
def funcsort():
    #sort
    aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
    random.shuffle(aList)
    print aList
    aList.sort()
    print aList
    aList.sort(reverse = True)
    print aList
    aList.sort(key = lambda x:len(str(x)))
    print aList
    #sorted
    sorted(aList)
    print aList
    sorted(aList,reverse = True)
    print aList
    #reverse
    aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
    aList.reverse()
    print aList
    #reversed
    aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
    newList = reversed(aList)
    print newList
    print list(newList)
    for i in newList:
        print i,
    newList = reversed(aList)
    for i in newList:
        print i,

#9序列内置函数
def funcin():
    #cmp
    print  (1, 2, 3) < (1, 2, 4)
    print cmp((1, 2, 3) , (1, 2, 4))
    print [1, 2, 3] < [1, 2, 4]
    print cmp([1, 2, 3] , [1, 2, 4])
    print 'ABC' < 'C' < 'Pascal' < 'Python'
    print cmp( 'Pascal', 'Python')
    print (1, 2, 3, 4) < (1, 2, 4)
    print cmp((1, 2, 3, 4),(1, 2, 4))
    print (1, 2) < (1, 2, -1)
    print cmp((1, 2), (1, 2, -1))
    print (1, 2, 3) == (1.0, 2.0, 3.0)
    print cmp((1, 2, 3), (1.0, 2.0, 3.0))
    print (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)
    print cmp('a', 'A')
    print 'a'>'A'
    #zip
    aList = [1,2,3]
    bList = [4,5,6]
    cList = [7,8,9]
    dList = zip(aList, bList, cList)
    print dList
    #enumerate
    for item in enumerate(dList):
        print item

#10列表推导式
def funclg():
    #定义
    aList = []
    for x in range(10):
        aList.append(x*x)
    print aList
    #相当于
    bList = [x*x for x in range(10)]
    print bList
    #功能
    ##实现嵌套列表的平铺
    vec = [[1,2,3], [4,5,6], [7,8,9]] 
    print [num for elem in vec for num in elem] 
    ##列出当前文件夹下所有Python源文件
    print [filename for filename in os.listdir('.') if filename.endswith('.py')]
    ##过滤不符合条件的元素
    aList = [-1,-4,6,7.5,-2.3,9,-11]
    print [i for i in aList if i>0]
    
#应用例示
##统计成绩
def lgdemo1():
    scores = {"Zhang San": 45, "Li Si": 78, "Wang Wu": 40, "Zhou Liu": 96, "Zhao Qi": 65, "Sun Ba": 90, "Zheng Jiu": 78, "Wu Shi": 99, "Dong Shiyi": 60}
    highest = max(scores.values())
    lowest = min(scores.values())
    print highest
    print lowest
    average = sum(scores.values())*1.0/len(scores)
    print average
    highestPerson = [name for name, score in scores.items() if score == highest]
    print highestPerson
#在列表推导式中使用多个循环，实现多序列元素的任意组合，并且可以结合条件语句过滤特定元素
def lgdemo2():
    print [(x, y) for x in range(3) for y in range(3)]
    print [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
#矩阵转置
def lgdemo3():
    matrix = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] 
    print matrix
    print [[row[i] for row in matrix] for i in range(4)] 
#使用函数或复杂表达式
def f(v):
    if v%2 == 0:
        v = v**2
    else:
        v = v+1
    return v
def lgdemo4():
    print([f(v) for v in [2, 3, 4, -1] if v>0])
    #相当于
    print([v**2 if v%2 == 0 else v+1 for v in [2, 3, 4, -1] if v>0])
def lgdemo5():
    #文件对象迭代 
    fp = open('123.txt', 'r')
    print([line for line in fp]) 
    fp.close()
def lgdemo6():
    #生成100以内的所有素数
    print  [ p for p in range(2, 100) if 0 not in [ p% d for d in range(2, int(math.sqrt(p))+1)] ]

#11元组
def tp1():
    #创建删除
    a_tuple = ('a', )
    print a_tuple
    a_tuple = ('a', 'b', 'mpilgrim', 'z', 'example')
    print a_tuple
    a=3
    print a
    a=3,
    print a
    x = () #空元组
    print x
    print tuple('abcdefg')
    aList=[-1, -4, 6, 7.5, -2.3, 9, -11]
    print tuple(aList)
    s = tuple() #空元组
    print s
    
def tp2():
    #序列解包
    ##多变量赋值
    v_tuple = (False, 3.5, 'exp')
    (x, y, z) = v_tuple
    a=[1,2,3]
    b,c,d=a
    s={'a':1,'b':2,'c':3}
    b,c,d=s
    print b
    print c
    print d

def tp3():
    ##序列遍历
    keys=['a','b','c','d']
    values=[1,2,3,4]
    for k,v in zip(keys,values):
        print k,v
    aList = [1,2,3]
    bList = [4,5,6]
    cList = [7,8,9]
    dList = zip(aList, bList, cList)
    for index, value in enumerate(dList):
        print index, ':', value

def tp4():
    #生成器推导式
    g=((i+2)**2 for i in range(10))
    print g
    tuple(g)
    g=((i+2)**2 for i in range(10))
    print g.next()

#12字典
def dc1():
    ##创建删除
    #赋值
    a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}
    print a_dict
    x = {} #空字典
    print x
    #已有数据
    keys=['a','b','c','d']
    values=[1,2,3,4]
    dictionary=dict(zip(keys,values))
    print dictionary
    x = dict() #空字典
    print x
    #dict
    d=dict(name='Dong',age=37)
    print d
    #给定键
    adict=dict.fromkeys(['name','age','sex'])
    print adict

def dc2():
    ##元素读取
    #下标
    aDict={'name':'Dong', 'sex':'male', 'age':37}
    print aDict['name']
#    print aDict['tel']
    #get
    print(aDict.get('address'))
    print(aDict.get('address', 'SDIBT'))
    aDict['score'] = aDict.get('score',[])
    aDict['score'].append(98)
    aDict['score'].append(97)
    print aDict
    #items,keys,values
    aDict={'name':'Dong', 'sex':'male', 'age':37}
    for item in aDict.items():
        print item	
    for key in aDict:
        print key	
    for key, value in aDict.items():
        print key, value	
    print aDict.keys()
    print aDict.values()

def dc3():
    ##添加修改
    #添加1
    aDict={'name':'Dong', 'sex':'male', 'age':37}
    aDict['age'] = 38
    print aDict
    aDict['address'] = 'SDIBT'
    print aDict
    #添加2
    aDict.items()
    aDict.update({'a':'a','b':'b'})
    print aDict
    
##应用
#生成包含1000个字符的随机字符串统计字符出现次数。
#method1
def func7():
    import string
    import random
    x = string.digits #+ string.ascii_letters + string.punctuation
    print x
    y = [random.choice(x) for i in range(1000)]
    print y
    z = ''.join(y)
    print z
    d = dict()
    for ch in z:
        d[ch] = d.get(ch, 0) + 1
    print d
    
#method2
def func8():
    import string
    import random
    x = string.digits
    y = [random.choice(x) for i in range(1000)]
    z = ''.join(y)
    from collections import defaultdict
    frequences = defaultdict(int)
    print frequences
    for item in z:
        frequences[item] += 1
    print frequences.items()
    
#method3
def func9():
    import string
    import random
    x = string.digits
    y = [random.choice(x) for i in range(1000)]
    z = ''.join(y)
    from collections import Counter
    frequences = Counter(z)
    print frequences.items()
    print frequences.most_common(1)
    print frequences.most_common(3)
    
#Counter词频统计
def wdfunc():
    from collections import Counter 
    cnt = Counter()
    for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
        cnt[word] += 1
    print cnt

def dcdemo1():
    #有序字典
    ##无序例
    x = dict() 
    x['a'] = 3
    x['b'] = 5
    x['c'] = 8
    print x
    ##有序例
    x = collections.OrderedDict() 
    x['a'] = 3
    x['b'] = 5
    x['c'] = 8
    print x

def dcg():
    #字典推导式
    s = {x:x.strip() for x in ('  he  ', 'she    ', '    I')}
    print s
    for k, v in s.items():
        print(k, ':', v)

#13集合
def stfunc1():        
    #赋值
    a={3,5}
    a.add(7)
    print a
    a_set=set(range(8,14))
    print a_set
    b_set=set([0,1,2,3,0,1,2,3,7,8])
    print b_set
    c_set = set() #空集合
    print c_set
    #删除
    a={1, 4, 2, 3}
    a.pop()
    print a
    a.pop()
    print a
    a.add(2)
    print a
    a.remove(3) #删除指定元素
    print a
#    a.pop(2) #pop()方法不接收参数
    #操作
    a_set.union(b_set)
    print a_set
    print b_set
    print a_set&b_set
    a_set.intersection(b_set)
    a_set.difference(b_set)
    a_set.symmetric_difference(b_set)
    print a_set^b_set

    listRandom = [random.choice(range(10000)) for i in range(100)]
    noRepeat = []
    for i in listRandom :
        if i not in noRepeat :
            noRepeat.append(i)
    len(listRandom)
    len(noRepeat)
    newSet = set(listRandom)
    s = {x.strip() for x in ('  he  ', 'she    ', '    I')}
    print s

def main():
    #list 
    x=input('xrange')
    func1()
    print('\n\n')
    x=input('list +')
    func11()
    print('\n\n')
    x=input('+ and method')
    func2()
    print('\n\n')
    x=input('memory of list')
    func21()
    print('\n\n')
    #时间消耗比较
    x=input('time consumption')
    func3()
    print('\n\n')
    x=input('list *')
    func31()
    print('\n\n')
    x=input('list delete')
    func41()
    print('\n\n')
    x=input('list loop')
    ###测试例
    x=input('RIGHT')
    x = [1,2,1,2,1,2,1,2,1]
    func4(x)
    print('\n\n')
    x=input('WRONG')
    x = [1,2,1,2,1,1,1]
    func4(x)    
    print('\n\n')
    ###测试例
    x=input('correct 1')
    x = [1,2,1,2,1,1,1]
    func5(x)
    print('\n\n')
    ###测试例
    x=input('correct 2')
    x = [1,2,1,2,1,1,1]
    func6(x)
    print('\n\n')
    #访问计数
    x=input('list count')
    func61([random.randint(1,20) for i in range(20)])
    print('\n\n')
    #7成员
    x=input('list member')
    func62()
    print('\n\n')
    #切片
    x=input('list slice')
    func63()
    print('\n\n')
    #排序
    x=input('list sorting')
    funcsort()
    print('\n\n')
    #序列内置函数
    x=input('list functions')
    funcin()
    print('\n\n')
    #列表推导式
    x=input('list generator')
    funclg()
    print('\n\n')
    #应用例示
    ##统计成绩
    x=input('demo1')
    lgdemo1()
    print('\n\n')
    #在列表推导式中使用多个循环，实现多序列元素的任意组合，并且可以结合条件语句过滤特定元素
    x=input('demo2')
    lgdemo2()
    print('\n\n')
    #矩阵转置
    x=input('demo3')
    lgdemo3()
    print('\n\n')
    #使用函数或复杂表达式
    x=input('demo4')
    lgdemo4()
    print('\n\n')
    #文件对象迭代
    x=input('demo5')
    lgdemo5()
    print('\n\n')
    #生成100以内的所有素数
    x=input('demo6')
    lgdemo6()
    print('\n\n')
    
    #元组
    ##创建删除
    x=input('tuple')
    tp1()
    print('\n\n')
    #序列解包
    x=input('tuple unpack')
    tp2()
    print('\n\n')
    ##序列遍历
    x=input('tuple visit')
    tp3()
    print('\n\n')
    #生成器推导式
    x=input('tuple generator')
    tp4()
    print('\n\n')
    
    #12字典
    ##创建删除
    x=input('dictionary')
    dc1()
    print('\n\n')
    ##元素读取
    x=input('dictionary reading')
    dc2()
    print('\n\n')
    ##添加修改
    x=input('dictionary revision')
    dc3()
    print('\n\n')
    ##应用
    #生成包含1000个字符的随机字符串统计字符出现次数。
    #method1
    x=input('dc demo1')
    func7()    
    print('\n\n')
    #method2
    x=input('dc demo2')
    func8()
    print('\n\n')
    #method3
    x=input('dc demo3')
    func9()
    print('\n\n')
    #Counter词频统计
    x=input('Counter')
    wdfunc()
    print('\n\n')
    #有序字典
    x=input('ordered dc')
    dcdemo1()
    print('\n\n')
    #字典推导式
    x=input('dc generator')
    dcg()
    print('\n\n')
    
    #13集合
    x=input('sets')
    stfunc1()
    print('\n\n')
    
main()
