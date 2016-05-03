# coding=utf-8
from time import time

# 判断s是否可缩减
def reduced(s):

    # 若s已经确认可缩减，或只剩一个字母且为'a'或'i'
    if s in yes or s in ('a', 'i'):

        # 此时不用继续求解 直接返回可缩减
        return True

    # 若s已经确认不可缩减，或确定s不在单词列表中
    if s in no or not s in words:

        # 此时不用继续求解 直接返回不可缩减
        return False

    # 假设s是不可缩减的
    res = False

    # 枚举s中每个字母
    for i in range(len(s)):

        # 删除该字母后的单词
        t = s[0:i] + s[i + 1:]

        # 递归求解
        if reduced(t):

            # 若递归求解成功，记录为可缩减
            res = True

            # 同时记录前驱单词
            reducedTo[s] = t

            # 停止求解该单词
            break

    # 根据结果，用集合记录可缩减或不可缩减的单词
    (no, yes)[res].add(s)

    # 返回结果
    return res


if __name__ == '__main__':

    # 集合words/yes/no 分别用于记录单词列表/可缩减单词/不可缩减单词
    words, yes, no = set(), set(), set()

    # 读取单词
    with open('words.txt', 'r') as f:
        for line in f:
            words.add(line.strip())

    # 假设最长可缩减单词为空
    res = ''

    # 记录前驱单词
    reducedTo = {}

    # 记录所有可能成为最长缩减单词的单词
    res_list = []

    # 对每个单词进行求解
    for word in words:

        # 若比已找到的最长单词要短，无需进行查找
        if len(word) < len(res):
            continue

        # 当前单词可缩减
        if reduced(word):

            # 记录可缩减单词
            res_list.append(word)

            # 记录更优结果
            if len(res) < len(word):
                res = word

    # 遍历所有的结果
    for word in res_list:

        # 若等于最大长度
        if len(word) == len(res) - 1:

            # 输出结果
            print len(word), word,

            # 输出缩减序列
            while word in reducedTo:
                print '->', reducedTo[word],
                word = reducedTo[word]
            print
