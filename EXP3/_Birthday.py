# coding=utf-8
from random import randint
from decimal import getcontext, Decimal
# import numpy as np
# import pylab as pl


# 随机产生一个生日
def new_birthday():

    # 1~12月的最大天数
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 随机产生月份
    month = randint(1, 12)

    # 随机产生日期
    day = randint(1, days[month])

    # 以元组返回生日
    return (month, day)


# 模拟n个人的情况
def sim(n):
    # s保存已产生的生日
    s = set()

    # 依次模拟n个人
    for i in xrange(n):

        # 产生新生日
        bir = new_birthday()

        # 统计
        if bir in s:
            return True
        else:
            s.add(bir)

    # 无相同生日
    return False


# 模拟t次n个人 返回概率
def multySim(n, t=1000):

    # 计算概率
    calP = 1.0
    for i in range(n):
        calP = Decimal(calP) * Decimal(366 - i) / Decimal(366)
    calP = Decimal(1 - calP).to_eng_string()

    # 模拟概率
    simP = 0
    for i in xrange(t):
        simP += sim(n)
    simP = 1.0 * simP / t

    # 返回
    return (calP, simP)


# 画图
def pic():
    print u'画图中...'

    # 横坐标X 纵坐标calY/simY表示计算/模拟概率
    X, calY, simY, res = [], [], [], 1

    # 只计算到70个人
    for i in range(71):
        X.append(i)
        calY.append(1 - res)
        simY.append(multySim(i))
        res *= (366.0 - i) / 366

    # 画图
    pl.plot(X, calY)
    pl.plot(X, simY)
    pl.show()


if __name__ == '__main__':

    # 设置浮点数精度位数
    getcontext().prec = 180

    # 对输入的人数n, 模拟1000次
    while True:
        n = input('Input amount of persons: ')
        res = multySim(n)
        print u'计算概率', res[0]
        print u'模拟概率', res[1]

    # 画图
    # pic()
