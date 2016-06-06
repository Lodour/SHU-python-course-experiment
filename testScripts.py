# coding=utf-8
# from random import sample, shuffle
# from random import randint
# # from math import sqrt, factorial as f
# # from collections import Counter

# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.animation as animation


# def gcd(a, b):
#     return a if b == 0 else gcd(b, a % b)


# def square_root(n):
#     x, y = n - 0.5, 0
#     while True:
#         y = (x + n / x) / 2
#         if abs(x - y) < 0.000000001:
#             break
#         x = y
#     return y

		


# def sort(q):
# 	return q if len(q) <= 1 else sort([i for i in q[1:] if i < q[0]]) + [q[0]] + sort([i for i in q[1:] if i >= q[0]])
# a = sample(range(1000), 20)

# def main():
#  numframes = 100
#  numpoints = 10
#  color_data = np.random.random((numframes, numpoints))
#  x, y, c = np.random.random((3, numpoints))

#  fig = plt.figure()
#  scat = plt.scatter(x, y, c=c, s=100)

#  ani = animation.FuncAnimation(fig, update_plot, frames=xrange(numframes),
#          fargs=(color_data, scat))
#  plt.show()

# def update_plot(i, data, scat):
#  scat.set_array(data[i])
#  return scat,

# main()
# 5
# import types
# class vector():
#     def __init__(self, x=0, y=0, z=0):
#         for i in [x, y, z]:
#             if not type(i) in [types.IntType, types.FloatType]:
#                 print 'Vector must consists of numeric type.'
#                 return
#         self.x = x
#         self.y = y
#         self.z = z

#     def __add__(self, v):
#         x = self.x + v.x
#         y = self.y + v.y
#         z = self.z + v.z
#         return vector(x, y, z)

#     def __sub__(self, v):
#         x = self.x - v.x
#         y = self.y - v.y
#         z = self.z - v.z
#         return vector(x, y, z)

#     def __mul__(self, t):
#         x = self.x * t
#         y = self.y * t
#         z = self.z * t
#         return vector(x, y, z)

#     def __div__(self, t):
#         x = 1.0 * self.x / t
#         y = 1.0 * self.y / t
#         z = 1.0 * self.z / t
#         return vector(x, y, z)

#     def __str__(self):
#         return '(%.2f, %.2f, %.2f)' % (self.x, self.y, self.z)

# import types
# class Person(object):

#     def __init__(self, name='', age=20, sex='man'):
#         self.setName(name)
#         self.setAge(age)
#         self.setSex(sex)

#     def setName(self, name):
#         if type(name) != types.StringType:
#             print 'name must be string.'
#             return
#         self.__name = name

#     def setAge(self, age):
#         if type(age) != types.IntType:
#             print 'age must be integer.'
#             return
#         self.__age = age

#     def setSex(self, sex):
#         if not sex in ('man', 'woman'):
#             print 'sex must be "man" or "woman"'
#             return
#         self.__sex = sex

#     def show(self):
#         print self.__name
#         print self.__age
#         print self.__sex

# class Student(Person):
#     def __init__(self, name='', age=20, sex='man', major='Computer'):
#         super(Student, self).__init__(name, age, sex)
#         self.setMajor(major)

#     def setMajor(self, major):
#         if type(major) != types.StringType:
#             print 'major must be string.'
#             return
#         self.__major = major

#     def show(self):
#         # super(Student, self).show()
#         Person.show(self)
#         print self.__major

# if __name__ == '__main__':
#     me = Student('Roll')
#     me.show()
# 4
# a = ['123   ',' dafsdf 's)) for i in a))

# print re.sub(r'\bi\b', 'I', s)
# s = 'I am a aIm, aIIm aiiIi. I i ii IiIi iIi'
# print re.sub(r'\BI\B', 'i', s)
# s = 'This is is a a desk desk.'
# print re.sub(r'\b([a-zA-Z]+)(\s+\1){1}\b', r'\1', s)
# s = 'a bb, ccc, ddd eee ffff ggg, hhh'
# print re.findall(r'\b[a-zA-Z]{3}\b', s)

# 3.1
# def demo(newitem, old_list=[]):
#     print id(old_list)
#     # if old_list is None:
#     #     old_list = []
#     old_list.append(newitem)
#     return old_list

# print demo('5', [1, 2, 3, 4])
# print demo('aaa', ['a', 'b'])
# print demo('a')
# print demo('b')
# print demo('c')
# print demo('d')

# 3.3
# from string import lowercase, uppercase, digits, punctuation
# def cal(s):
#     res = [0, 0, 0, 0]
#     for i in s:
#         for j in range(4):
#             if i in (lowercase, uppercase, digits, punctuation)[j]:
#                 res[j] += 1
#     return tuple(res)

# 3.5
# def cal(*args):
#   print max(args), sum(args)

# 3.6
# def cal(L):
#     return reduce(lambda x, y: x + y, L)

# 3.7
# from random import randint
# def Sorted(q):
#     return q if len(q) <= 1 else Sorted([i for i in q[1:] if i < q[0]]) + [q[0]] + Sorted([i for i in q[1:] if i >= q[0]])
# for i in range(100):
#   l = [randint(1,100000) for i in range(10000)]
#   if not Sorted(l) == sorted(l):
#       print l

# 2.2
# from collections import Counter
# cnt, a = Counter(), [randint(0, 100) for i in range(1000)]
# for i in a:
#   cnt[i] += 1
# for i in cnt:
#   print '%3d: %3d' % (i, cnt[i])

# 2.3
# a, l, r = input(), input(), input()
# print a[l:r + 1]

# 2.4
# a = dict()
# for i in range(100):
#   a[str(i)] = i
# while True:
#   key = raw_input()
#   print a[key] if key in a else u'您输入的键不存在！'

# 2.5
# from random import randint
# a = [randint(1, 100) for i in range(20)]
# print a
# a[:10] = sorted(a[:10])
# a[10:] = sorted(a[10:], reverse=True)
# print a

# u, me = 'v`sPIZ`|og', ''
# me = me.join([chr(ord(me) ^ 1013 % 95) for me in u])
# # print me
# print ''.join([chr(ord(me) ^ 1013 % 95) for me in 'v`sPIZ`|og'])
# print [i for i in range(2, 100) if [j for j in range(2, i) if i % j == 0] == []]
# def run(m, n):
#     print m,n
#     if m == 0:
#         return n + 1
#     if m > 0 and n == 0:
#         return run(m - 1, 1)
#     if m > 0 and n > 0:
#         return run(m - 1, run(m, n - 1))

# print run(4,2)

# def another_birthday():
#     days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     month = randint(1, 12)
#     day = randint(1, days[month])
#     return (month, day)


# def sim(n=1000):
#     li, cnt = [], 0
#     for i in range(n):
#         bir = another_birthday()
#         if bir in li:
#             cnt += 1
#         else:
#             li.append(bir)
#     print n, cnt * 1.0 / n

# sim()

# words = ['sprite', 'spite', 'spit', 'pit', 'it', 'i']
# yes, no = set(), set()

# # 判断s是否可缩减
# def solve(s):
#     if s in yes or (len(s) == 1 and s in words):
#         yes.add(s)
#         return True
#     if s in no or not s in words:
#         no.add(s)
#         return False
#     res = False
#     for i in range(len(s)):
#         if solve(s[0:i] + s[i + 1:]):
#             res = True
#     (no, yes)[res].add(s)
#     return res

# if __name__ == '__main__':
#     with

# # 1.2
# # a = sample(range(1, 101), 20)

# # 2.2
# from math import sqrt
# b = [x for x in range(2, 100) if not [y for y in xrange(
#     2, int(sqrt(x)) + 1) if x % y == 0]]

# # 2.3
# # cnt = Counter()
# # for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
# #     cnt[word] += 1
# # print cnt

# # 3.1
# # s, res = 0, 2 * sqrt(2) / 9801
# # for k in range(100):
# #     s += 10**20 * r(4 * k) * (1103 + 26390 * k) / (f(k)**4) / (396**(4 * k))
# # print res * s

# u = 'v`sPIZ`|og'
# print ''.join([chr(ord(me) ^ 1013 % 95) for me in u])
# from random import randint
# a = [randint(0, 100) for i in range(20)]
# a[::2] = sorted(a[::2], reverse=True)
# for i in range(len(a) - 1, -1, -1):
#     if a[i] % 2 == 1:
#         del a[i]
# a = filter(lambda x: x % 2 == 0, a)
# print a

# from random import *
# a = sample(range(100000, 1000001), 1000)
# for i in a:
#   if i == 0:
#       print 0, 0
#       continue
#   vis = [0] * 10
#   ii = 0
#   while 0 in vis:
#       ii += i
#       for j in map(int, str(ii)):
#           vis[int(j)] = 1
#   print i, ii


# def deco(func):
#     print("before myfunc() called.")
#     func()
#     print("  after myfunc() called.")
#     return func

# def myfunc():
#     print(" myfunc() called.")

# myfunc = deco(myfunc)

# myfunc()
# myfunc()
