# coding=utf-8


# 返回strsrc轮转n个字符后得到的字符串
def rotateWord(strsrc, n):
    L = len(strsrc)
    return ''.join([strsrc[(i + n) % L] for i in range(L)])


# 判断word是否含有regex中的禁止字母
def avoids(word, regex):
    return [i for i in word if i in regex] != []


# 判断word是否仅由regex中字母组成
def useonly(word, regex):
    return [i for i in word if not i in regex] == []


# 判断word是否包含了regex中所有字母至少一个
def useall(word, regex):
    return len([i for i in regex if i in word]) == len(regex)


# 判断word中是否没有字母e
def hasnoe(word):
    return not 'e' in word


# 判断一个英语单词中的字母是否符合字母表序
def isabecedarian(word):
    return word == ''.join(sorted(word))


# *4(4)
def OutputAllVowelWords(li):
    return filter(lambda x: useall(x, 'aeiou'), li)


# *4(5)
def OutputRateOfWordsWithoutE(li):
    return 100.0 * len(filter(lambda x: hasnoe(x), li)) / len(li)


# *4(6)
def OutputAllAbecedarianWords(li):
    return filter(lambda x: isabecedarian(x), li)


if __name__ == '__main__':

    print rotateWord('abcdef', 3)

    li = []
    with open('words.txt', 'r') as fin:
        li += [line.strip() for line in fin]
