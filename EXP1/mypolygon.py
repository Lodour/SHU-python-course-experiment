# coding=utf-8
from swampy.TurtleWorld import *
from polygon import arc

def Heart(t, r):
    """
    t : Turtle
    r : Radius of the heart
    """
    # 防止溢出
    pu(t)
    fd(t, r * 2)
    pd(t)

    # 右边
    lt(t)
    arc(t, r, -180)
    arc(t, r * 2, -60)
    arc(t, r * 2, 60)

    # 左边
    lt(t, 180)
    arc(t, r * 2, 60)
    arc(t, r * 2, -60)
    arc(t, r, -180)
    lt(t, 90)


def Fractal(t, size, minsize):
    """
    t       : Turtle
    size    : Length of the longest edge
    rate    : LengthOfThisEdge / LengthOfNextEdge
    minsize : Length of the shortest edge
    """
    if size < minsize:
        fd(t, size)
        return
    newsize = size / 3
    Fractal(t, newsize, minsize)
    lt(t, 60)
    Fractal(t, newsize, minsize)
    rt(t, 120)
    Fractal(t, newsize, minsize)
    lt(t, 60)
    Fractal(t, newsize, minsize)


def Fractal2(t, size, rate, minsize):
    """
    t       : Turtle
    size    : Length of the longest edge
    rate    : LengthOfThisEdge / LengthOfNextEdge
    minsize : Length of the shortest edge
    """
    fd(t, size)
    if(size < minsize):
        return
    newsize = size / rate

    # 左边
    lt(t, 60)
    Fractal2(t, newsize, rate, minsize)

    # 左边还原
    pu(t)
    lt(t, 180)
    fd(t, newsize)
    lt(t, 60)
    pd(t)

    # 右边
    Fractal2(t, newsize, rate, minsize)

    # 右边还原
    pu(t)
    lt(t, 180)
    fd(t, newsize)
    rt(t, 120)
    pd(t)


def Snow(t, size, minsize):
    """
    t       : Turtle
    size    : Length of the longest edge
    minsize : Length of the shortest edge
    """
    for i in range(3):
        Fractal(t, size, minsize)
        rt(t, 120)


def Tree(t, size, rate, minsize):
    """
    t       : Turtle
    size    : Length of the longest edge
    rate    : LengthOfThisEdge / LengthOfNextEdge
    minsize : Length of the shortest edge
    """
    if rate < 1.0:
        print 'rate must be greater than 1.0'
        return
    # 避免出界
    pu(t)
    fd(t, size)
    rt(t, 90)
    fd(t, size)
    lt(t, 90)
    pd(t)

    # 向上
    lt(t)
    Fractal2(t, size, rate, minsize)

    # 还原
    pu(t)
    lt(t, 180)
    fd(t, size)
    lt(t, 180)
    pd(t)


if __name__ == '__main__':
    world = TurtleWorld()
    bob = Turtle()
    bob.delay = 0.001

    Heart(bob, 20)
    # Snow(bob, 100, 4)
    # Tree(bob, 200, 1.8, 2)

    wait_for_user()
