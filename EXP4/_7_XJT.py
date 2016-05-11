# coding=utf-8
from random import sample, randint
import re


def foo1():
    """ 以下十五段，读俱同前：
    所怀至芳琴、河隔至刚亲、清流至伤仁、妙显至梁民、生感至望纯、
    清志至商秦、曲发至唐贞、贤惟至长身、微悯至霜新、故感至藏音、
    和咏至章臣、匹离至房人、贱为至墙春、阳熙至堂心、忧增至皇伦。 
    """
    def Next(dis):
        if dis[0] == 0:
            if dis[1] == 28:
                return (1, 28)
            return (0, dis[1] + 1)
        if dis[0] == 28:
            if dis[1] == 0:
                return (27, 0)
            return (28, dis[1] - 1)
        if dis[1] == 0:
            if dis[0] == 0:
                return (0, 1)
            return (dis[0] - 1, 0)
        if dis[1] == 28:
            if dis[0] == 28:
                return (28, 27)
            return (dis[0] + 1, 28)

    i, j = 0, 1
    cnt = 0
    out = ''
    while cnt != 112:
        out += txt[i][j * 3:j * 3 + 3]
        cnt += 1
        if cnt % 14 == 0:
            out += '。\n'
        elif cnt % 7 == 0:
            out += '，'
        if cnt % 28 == 0:
            out += '\n'
        i, j = Next((i, j))
    print out[:-1]


def dfs(x, y, cur=''):
    vis[x][y] = 1
    if len(res) >= 100000:
        return
    if len(cur) == 84:
        res.add(cur)
        return
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 29 and 0 <= ny < 29 and not vis[nx][ny]:
            dfs(nx, ny, cur + txt[x][y * 3:y * 3 + 3])
            vis[nx][ny] = 0


if __name__ == '__main__':

    # 读入文本数据
    txt, vis = [], []
    dx = (-1, -1, -1, 0, 0, 1, 1, 1)
    dy = (-1, 0, 1, -1, 1, -1, 0, 1)
    with open('_7_XJT.txt', 'r') as fin:
        txt += [line.strip() for line in fin]
        for i in range(len(txt)):
            vis += [[0] * len(txt)]

    foo1()

    for i in range(20):
        res = set()
        dfs(randint(0, 28), randint(0, 28))
        a = [i for i in res]

        def out(t=0):
            res = ''
            for i in range(84):
                res += a[t][i]
                if (i + 1) % 21 == 0:
                    if (i + 1) % 42 == 0:
                        res += '。\n'
                    else:
                        res += '，'
            print res[:-1]
            print

        # raw_input()
        out(randint(0, 100000))
