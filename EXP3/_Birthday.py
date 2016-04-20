# coding=utf-8
from random import randint


# 随机产生一个生日
def another_birthday():

    # 1~12月的最大天数
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 随机产生月份
    month = randint(1, 12)

    # 随机产生日期
    day = randint(1, days[month])

    # 以元组返回生日
    return (month, day)


# 模拟n次
def sim(n=1000):
    # li保存已产生的生日 cnt保存出现相同生日的次数
    li, cnt = [], 0

    # 依次模拟n次
    for i in range(n):

        # 产生新生日
        bir = another_birthday()

        # 统计
        if bir in li:
            cnt += 1
        else:
            li.append(bir)

    # 输出模拟结果
    print u'模拟 %d 次，相同生日概率为 %.3lf' % (n, cnt * 1.0 / n)

if __name__ == '__main__':

    # 多次模拟
    for n in range(100, 2000, 100):
        sim(n)
