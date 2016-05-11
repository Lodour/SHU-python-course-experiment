# coding=utf-8


# 4(1)
def rotateWord(strsrc, n):
    L = len(strsrc)
    return ''.join([strsrc[(i + n) % L] for i in range(L)])


# 4(2)
def avoids(word, regex):
    return [i for i in word if i in regex] != []


# 4(3)
def useonly(word, regex):
    return [i for i in word if not i in regex] == []


# 4(4)
def useall(word, regex):
    return len([i for i in regex if i in word]) == len(regex)


# 4(5)
# 返回word中是否没有字母e
def hasnoe(word):
    return not 'e' in word


# 4(6)
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
