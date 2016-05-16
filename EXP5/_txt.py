# coding=utf-8
import re


def getSingleWords(file):
    res = []
    for line in file:
        find = re.findall(r'\d、(.*?)\(', line.strip())
        if len(find) > 0:
            res.append(find[0].replace(' ', ''))
    return res


def getChineseText(file):
    res, cur, vis = [], u'', set()
    for line in file:
        line = line.strip().decode('utf-8')
        if len(line) <= 2 or re.findall(ur'\w', line):
            continue
        hui = re.findall(ur'^第(.*)回', line[:5])
        cur += line
        if hui and not hui[0] in vis:
            vis.add(hui[0])
            res.append(cur)
            cur = u''
    res.append(cur)
    return res[1:]


if __name__ == '__main__':
    with open('_shici.txt', 'r') as f:
        listShici = getSingleWords(f)
    with open('_xuci.txt', 'r') as f:
        listXuci = getSingleWords(f)
    words = listShici + listXuci

    with open('dreamofredmaison.txt', 'r') as f:
        text = getChineseText(f)

    res = dict()
    for word in words:
        res[word.decode('utf-8')] = 0

    with open('_result.txt', 'w') as f:
        for hui in range(1, 120):
            txt = text[hui]
            for word in txt:
                if word in res:
                    res[word] += 1
        tot = sum([res[word] for word in res])
        for i in res:
            res[i] = 1.0 * res[i] / tot
            f.write('[%s] %.5lf\n' % (i.encode('gbk'), res[i]))
