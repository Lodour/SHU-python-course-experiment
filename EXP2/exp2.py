# coding=utf-8
from time import time
from decimal import getcontext, Decimal
from math import sqrt, pi
from collections import Counter


def EXP2_3_1():

    # 输出math中的pi值
    print pi

    # 该函数f返回x的阶乘
    f = lambda x: reduce(lambda x, y: x * y, range(1, x + 1)) if x else 1

    # 设置浮点数精度15位, 计算精度MAX_K
    getcontext().prec, MAX_K = 100, 100

    # 计算过程
    m = Decimal(2 * sqrt(2)) / Decimal(9801)
    ans = 0
    for k in range(0, MAX_K):
        a = f(4 * k)
        b = 1103 + 26390 * k
        c = f(k)**4
        d = 396**(4 * k)
        ans = ans + Decimal(a * b) / Decimal(c * d)
    ans *= m

    # 输出计算结果
    print Decimal(1) / Decimal(ans)


def EXP2_4():

    # 二分查找
    def find(string, lis):
        left, right = 0, len(lis)
        while left + 1 < right:
            middle = left + right >> 1
            if string < lis[middle]:
                right = middle
            else:
                left = middle
        return left if lis[left] == string else -1

    # 输入单词
    with open('words.txt', 'r') as f:
        words = [line.strip() for line in f]
        f.close()

    # 排序
    words = sorted(words)

    # 对每个词的反向单词进行二分查找
    print '二分查找...',

    # res记录结果 start记录时间
    res, start = [], time()

    # 对于每个单词
    for word in words:

        # 计算反向
        word_reversed = word[::-1]

        # 若 原单词 >= 反向单词 , 则已经查询过
        if word < word_reversed:
            p = find(word_reversed, words)

            # 若找到
            if p != -1:
                res.append((word, words[p]))

    # 输出结果
    print '%d : 用时 %.6lf 秒' % (len(res), time() - start)
    print res

    # 顺序查找
    print '顺序查找...'

    # res保存结果 start记录时间 cnt记录进度
    res, start, cnt = [], time(), 0

    # 对于每个单词
    for word in words:

        # 计算反向
        word_reversed = word[::-1]

        # 若 原单词 >= 反向单词 , 则已经查询过
        if word < word_reversed and word_reversed in words:

            # 添加结果
            res.append((word, word_reversed))

        # 更新进度
        cnt += 1
        if cnt % 5000 == 0:
            print '已完成% .2lf%% , 用时% .6lf 秒 ...' % (100.0 * cnt / len(words), time() - start)

    # 输出结果
    print '顺序查找... %d : 用时 %.6lf 秒' % (len(res), time() - start)


def EXP2_5():

    # 单词文件
    f, d = open('work.txt', 'r'), Counter()

    # 读入单词
    for line in f:
        # 转换为小写
        line = line.lower()

        # 除去该行中所有符号
        for i in """,./<>?;':"[]}{-=_+)(*&^%$#@!~`""":
            line = line.replace(i, '')

        # 按空格分词
        L = line.strip().split(' ')

        # 遍历当前行的所有单词
        for i in L:

            # 统计个数
            if i:
                d[i] += 1

    # 输出
    res = []
    for i in d:
        res.append((d[i], i))
    res.sort(reverse=True)
    for i in res:
        print i[1].ljust(10), i[0]

    # 关闭文件
    f.close()


if __name__ == '__main__':
    EXP2_3_1()
    # EXP2_4()
    # EXP2_5()
