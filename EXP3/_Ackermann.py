# coding=utf-8


# 计算Ackermann函数的值
def Ack(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return Ack(m - 1, 1)
    if m > 0 and n > 0:
        return Ack(m - 1, Ack(m, n - 1))

if __name__ == '__main__':
    print Ack(3, 4)
