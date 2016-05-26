# coding=utf-8

# 将文本分解成单词列表
import random


def make_word_list(path):
    word_list = []
    fin = open(path)
    for line in fin:
        word = line.strip()
        words = word.split()
        for i in words:
            word_list.append(i)
    return word_list
f = make_word_list("emma.txt")
# print f[0]
# print f[1]
# n阶马尔可夫分析


def marco(n, f):
    res = {}
    for i in range(len(f) - 2 * n):
        keystr = []
        for j in range(0, n):
            keystr.append(f[i + j])
        key = ' '.join(keystr)
        appendres = []
        for k in range(n, 2 * n):
            appendres.append(f[i + k])
        appendress = ' '.join(appendres)
        res.setdefault(key, []).append(appendress)  # 列表实现一键多值
    # print res
    return res
a = marco(1, f)
# print a
# 生成句子


def creat(marcof, m):
    length = len(marcof)
    keys = marcof.keys()
    key = keys[random.randint(0, length)]
    result = ''
    for i in range(0, m):
        mres = []
        while 1:
            reslist = marcof[key]
            randomnumber = random.randint(0, len(reslist) - 1)
            key = reslist[randomnumber]
            # print key
            mres.append(key)
            if key[-1] == '.' or key[-1] == '?' or key[-1] == '!':
                break
        results = ' '.join(mres)  # 当前句
        results = results.capitalize()  # 当前句首字母大写
        result += results  # 将当前结果添加进最终结果
        # print result
    return result  # 打印最后结果
print creat(a, 1)  # 第二个参数为生成几个句子。
