#coding:utf-8
## -*- coding : gbk -*-
#计算文本文件中最长行的长度
#方法一：
f=open('d:\\test.txt','r')
allLineLens=[len(line.strip()) for line in f]
f.close()
longest=max(allLineLens)
print longest

#方法二：
f=open('d:\\test.txt','r')
longest=max(len(line.strip()) for line in f)
f.close()
print longest

#比较两个文本文件是否相同
import difflib
A=file('c:\\dir.txt','r')
B=file('c:\\dir1.txt','r')
contextA=A.read()
contextB=B.read()
s=difflib.SequenceMatcher(lambda x:x=="",contextA,contextB)
result=s.get_opcodes()
for tag,i1,i2,j1,j2 in result:
    print("%s contextA[%d:%d]=%s contextB[%d:%d]=%s"%\
          (tag,i1,i2, contextA [i1:i2],j1,j2, contextB[j1:j2]))





