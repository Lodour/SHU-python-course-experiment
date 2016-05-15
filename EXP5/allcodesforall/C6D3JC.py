# -*- coding:utf-8 -*-

class A():
       def __init__(self):
              self.__private()
              self.public()
       def __private(self):
              print '__private() method of A'
       def public(self):
              print 'public() method of A'

class B(A):
       def __private(self):
              print '__private() method of B'
       def public(self):
              print 'public() method of B'

if __name__ =='__main__':
    b = B() #自动调用从基类A继承的构造函数
    print '\n'.join(dir(b)) #查看对象b的成员
