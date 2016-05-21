# coding=utf-8
import re
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import numpy as np
import matplotlib.pyplot as plt


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


def test(article, outfile):
    res = dict()
    for word in words:
        res[word.decode('utf-8')] = [0, 0]

    with open('%s.txt' % outfile, 'w') as f:
        for index, part in enumerate(article):
            for chapter in part:
                for word in chapter:
                    if word in res:
                        res[word][index] += 1
            tot = sum([res[word][index] for word in res])
            for i in res:
                res[i][index] = 1.0 * res[i][index] / tot
                f.write('[%s] %.5lf %.5lf\n' %
                        (i.encode('gbk'), res[i][0], res[i][1]))
    for i in res:
        res[i] = tuple(res[i])
    return res


def gen(labels):
    data = np.array([res[i] for i in labels])
    plt.subplots_adjust(bottom=0.1)
    plt.scatter(
        data[:, 0], data[:, 1], marker='o')
    for label, x, y in zip(labels, data[:, 0], data[:, 1]):
        plt.annotate(
            label,
            xy=(x, y), xytext=(-20, 20),
            textcoords='offset points', ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    plt.show()


class TxtMainWindow(QWidget):
    """主窗口"""

    def __init__(self):
        super(TxtMainWindow, self).__init__()
        self.cbs = []
        vbox = QVBoxLayout()
        for i in range(15):
            hbox = QHBoxLayout()
            for j in range(10):
                cnt = i * 10 + j
                cb = QCheckBox(words[cnt].decode('utf-8'))
                hbox.addWidget(cb)
                self.cbs.append(cb)
            vbox.addLayout(hbox)
        pbConfirm = QPushButton(u'确定')
        pbClear = QPushButton(u'清空')
        hbox = QHBoxLayout()
        hbox.addWidget(pbClear)
        hbox.addWidget(pbConfirm)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        pbConfirm.clicked.connect(self.confirm)
        pbClear.clicked.connect(self.clear)

    def confirm(self):
        g = []
        for i in range(len(self.cbs)):
            if self.cbs[i].isChecked():
                print words[i],
                g.append(words[i].decode('utf-8'))
        print
        gen(g)

    def clear(self):
        for i in self.cbs:
            i.setChecked(False)


if __name__ == '__main__':
    with open('_shici.txt', 'r') as f:
        listShici = getSingleWords(f)
    with open('_xuci.txt', 'r') as f:
        listXuci = getSingleWords(f)
    words = listShici + listXuci

    with open('dreamofredmaison.txt', 'r') as f:
        text = getChineseText(f)

    res = test((text[:80], text[-40:]), '_result')

    TxtAnalyse = QApplication(sys.argv)
    MainWindow = TxtMainWindow()
    MainWindow.show()
    TxtAnalyse.exec_()
