#coding:utf-8
## -*- coding : gbk -*-

from math import pi as PI
import types
import collections
import random
import math
import fractions


#继承Python内置异常类来实现自定义的异常类
#eg1
class ShortInputException(Exception):
    '''自定义的异常类。'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast 

def func1():
    try:
        s = raw_input('请输入 --> ')
        if len(s) < 3:
            raise ShortInputException(len(s), 3)
    except EOFError: 		
        print(u'你输入了一个结束标记EOF')
    except ShortInputException, x:				
        print(u'ShortInputException: 输入的长度是 %d, 长度至少应是 %d' % (x.length, x.atleast))
    else:
        print(u'没有异常发生.')

#eg2
class MyError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)

def func2():
    try:
        raise MyError(2*2)
    except MyError as e:
        print('My exception occurred, value:', e.value)
    raise MyError('oops!')

#多个异常
class Error(Exception):
    pass
class InputError(Error):
    """Exception raised for errors in the input.
    Attributes:
        expression -- input expression in which the error occurred  message
        -- explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not allowed.
    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """
    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

def func3():
    try:
        a = input('ErrorType 2/3:')
        if a==2:
            raise InputError(2*2,'multuplier')
        if a==3:
            raise TransitionError(2*2,2+2,'multuplier and add')
    except InputError as e:
        print(e.expression, e.message) 
    except TransitionError as e:
        print(e.previous, e.next, e.message)

def func4():
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("That was no valid number.  Try again...")

def func5():
    try:
        raise Exception('spam', 'eggs')
    except Exception as inst:
        print(type(inst))    # the exception instance
        print(inst.args)     # arguments stored in .args
        print(inst)          # __str__ allows args to be printed directly,
                                 # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)

def func6():
    try:
        x=input('请输入被除数: ')
        y=input('请输入除数: ')
        z=float(x) / y
    except ZeroDivisionError:
        print u'除数不能为零'
    except TypeError:
        print u'被除数和除数应为数值类型'
    except NameError:
        print u'变量不存在'
    else:
        print x, '/', y, '=', z

def func7():
    import sys
    try:
        f = open('data.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def func8():
    import sys
    try:
        f = open('data.txt')
        s = f.readline()
        i = int(s.strip())
    except (OSError, ValueError,RuntimeError, NameError):
        pass

def func9():
    try:
        assert 1 == 2 , "1 is not equal 2!"
    except AssertionError, reason:
        print "%s:%s"%(reason.__class__.__name__, reason)

def func10():
    with open('sample2.txt') as f:
        for line in f:
            print line

    
def main():
    pass

main()
