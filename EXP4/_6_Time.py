# coding=utf-8


class Time():
    """Sample of Class Time"""

    # 构造函数 默认为00:00:00
    def __init__(self, hour=0, minute=0, second=0):
        self.hour   = hour
        self.minute = minute
        self.second = second

    # 字符串函数
    def __str__(self):
        args = (self.hour, self.minute, self.second)
        return '%02d:%02d:%02d' % args

    # 累加函数
    def __add__(self, another_time):
        s = self.time2int() + another_time.time2int()
        return Time(s / 3600 % 24, s % 3600 / 60, s % 60)

    # 时间转换为秒数
    def time2int(self):
        t1 = self.hour   * 3600
        t2 = self.minute * 60
        t3 = self.second * 1
        return t1 + t2 + t3

    # 输出时间
    def printtime(self):
        print str(self)

    # 判断先后
    def isafter(self, another_time):
        return self.time2int() > another_time.time2int()

    # 经过n秒
    def increment(self, n=0):
        s = self + Time(0, 0, n)

    # 判断合法
    def isvalid(self):
        return self.hour   in range(0, 25) \
           and self.minute in range(0, 61) \
           and self.second in range(0, 61)


if __name__ == '__main__':
    a = Time(8, 40, 55)
    b = Time(9, 32, 10)
    print a, b, a + b
    print a.time2int(), b.time2int()
    a.printtime()
    b.printtime()
    print a.isafter(b), b.isafter(a)
    print a.increment(b.time2int() - a.time2int())
    print Time(1, 2, 3).isvalid(), Time(25, 0, 0).isvalid()
