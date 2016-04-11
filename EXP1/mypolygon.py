# coding=utf-8
from swampy.TurtleWorld import *
from polygon import arc
from math import *


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
    """ Koch
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


def Fractal2(t, size, rate, angle, minsize):
    """ BinaryTree
    t       : Turtle
    size    : Length of the longest edge
    rate    : LengthOfThisEdge / LengthOfNextEdge
    angle   : Angle of each turn.
    minsize : Length of the shortest edge
    """
    fd(t, size)
    if(size < minsize):
        return
    newsize = size / rate

    # 左边
    lt(t, angle)
    Fractal2(t, newsize, rate, angle, minsize)

    # 左边还原
    pu(t)
    lt(t, 180)
    fd(t, newsize)
    lt(t, 180 - angle * 2)
    pd(t)

    # 右边
    Fractal2(t, newsize, rate, angle, minsize)

    # 右边还原
    pu(t)
    lt(t, 180)
    fd(t, newsize)
    rt(t, 180 - angle)
    pd(t)


# 0/1/2/3 right/down/left/up
def Fractal3_draw(t, nextdir, length):
    """ Draw a line towards #nextdir.
    length : Length of the line.
    """
    rt(t, (nextdir - PEANO_DIRECTION + 4) % 4 * 90)
    fd(t, length)
    return nextdir


def Fractal3(t, level, _dir, length):
    """ Peano
    t      : Turtle
    level  : level of the Peano Curve
    _dir   : PEANO_Direction of next recursion.
    length : Length of each edge.
    """
    global PEANO_DIRECTION
    if level == 1:
        newdir = [_dir ^ i for i in (2, 3, 0)]
        for i in range(3):
            PEANO_DIRECTION = Fractal3_draw(t, newdir[i], length)
    else:
        newdir1 = [_dir ^ i for i in (1, 0, 0, 3)]
        newdir2 = [_dir ^ i for i in (2, 3, 0)]
        for i in range(3):
            Fractal3(t, level - 1, newdir1[i], length)
            PEANO_DIRECTION = Fractal3_draw(t, newdir2[i], length)
        Fractal3(t, level - 1, newdir1[3], length)


def Snow(t, size, minsize):
    """ Snow Flake

    t       : Turtle
    size    : Length of the longest edge
    minsize : Length of the shortest edge
    """
    for i in range(3):
        Fractal(t, size, minsize)
        rt(t, 120)


def Tree(t, size, rate, angle, minsize):
    """
    t       : Turtle
    size    : Length of the longest edge
    rate    : LengthOfThisEdge / LengthOfNextEdge
    angle   : Angle of each turn.
    minsize : Length of the shortest edge
    """
    if rate < 1.0:
        print '[WARNING] Rate must be greater than 1.0'
        return
    # 避免出界
    pu(t)
    fd(t, size * 2)
    rt(t, 90)
    fd(t, size * 2)
    lt(t, 90)
    pd(t)

    # 向上
    lt(t)
    Fractal2(t, size, rate, angle, minsize)

    # 还原
    pu(t)
    lt(t, 180)
    fd(t, size)
    lt(t, 180)
    pd(t)


def Peano(t, level, length=10):
    """ Peano
    t      : Turtle
    level  : level of the Peano Curve
    length : Length of each edge.
    """
    lt(t)
    globals()['PEANO_DIRECTION'] = 3
    Fractal3(t, 5, PEANO_DIRECTION, length)


if __name__ == '__main__':
    world = TurtleWorld()
    bob = Turtle()
    bob.delay = 0.001

    Heart(bob, 50)

    # Snow(bob, 200, 4)

    # Tree(bob, 100, 2, 60, 5)

    # Tree(bob, 100, 1.7, 30, 5)

    # Tree(bob, 100, 1.4, 45, 4)

    # PEANO_DIRECTION = 0   # global var
    # Peano(bob, 3)

    wait_for_user()
