# coding=utf-8


# 判断s是否可缩减
def solve(s):

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

        # 递归求解删除该字母后的单词
        if solve(s[0:i] + s[i + 1:]):

            # 若递归求解成功，记录为可缩减
            res = True

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
        f.close()

    # 假设最长可缩减单词为空
    res = ''

    # 对每个单词进行求解
    for word in words:

        # 当前单词可缩减，且更长时
        if solve(word) and len(res) < len(word):

            # 记录更优结果
            res = word

    # 输出结果
    print res, len(res)
