#coding:utf-8
## -*- coding : gbk -*-

#from __future__ import print_function
import os

#向文本文件中写入内容。
def func1():
    s= '文本文件的读取方法\n文本文件的写入方法\n'
    f=open('sample.txt', 'a+')
    f.write(s)
    f.close()

    #建议写法
    with open('sample.txt','a+') as f:
          f.write(s)

#读取并显示文本文件的前5个字节
def func2():
    f=open( 'sample.txt', 'r')
    s=f.read(5)   #读取文件的前5个字节
    f.close( )
    print('s=',s)
    print('字符串s的长度(字符个数)=', len(s))

#读取并显示文本文件所有行
def func3():
    #M1
    f=open('sample.txt', 'r')
    while True:
        line=f.readline()
        if line=='':
            break
        print line,
        #逗号不会产生换行符
        #但文件中有换行符，因此会换行
    f.close()
    #M2
    f=open('sample.txt', 'r')
    li=f.readlines()
    for line in li:
        print line,  
    f.close()


def func4():
    s = '上海大学SHU计算机学院CSDEPT'
    fp = open(r'E:\sample.txt', 'w')
    fp.write(s)
    fp.close()
    fp = open(r'E:\sample.txt', 'r')
    print(fp.read(3))
    fp.seek(3)
    print(fp.read(1))
    fp.seek(9)
    print(fp.read(2))
    fp.seek(15)
    print(fp.read(1))

##def func5():
##    with open('data.txt', 'r') as fp:
##        data = fp.readlines()
##    data = [int(line.stripe()) for line in data]
##    data.sort()
##    data = [str(i)+'\n' for i in data]
##    with open('data_asc.txt', 'w') as fp:
##        fp.writelines(data)

def func5():
    data = []
    with open('data.txt', 'r') as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            line = line.split()
            line = map(int, line)
            data.extend(line)
            
    data.sort()
    data = list(map(str, data))

    lines = []
    for index in range(0, len(data), 4):
        line = '    '.join(data[index:index+4])+'\n'
        lines.append(line)

    with open('data_asc1.txt', 'w') as fp:
        fp.writelines(lines)


def func6():
    filename = 'C7D1intergersort.py'
    with open(filename, 'r') as fp:
        lines = fp.readlines()
    lines = [line.rstrip()+' '*(100-len(line))+'#'+str(index)+'\n' for index, line in enumerate(lines)]
    with open(filename[:-3]+'_new.py', 'w') as fp:
        fp.writelines(lines)


def func7():
    import pickle
    f=open('sample_pickle.dat', 'wb')
    n=7
    i=13000000
    a=99.056
    s='中国人民123abc'
    lst=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    tu=(-5, 10, 8)
    coll={4, 5, 6}
    dic={'a':'apple', 'b':'banana', 'g':'grape', 'o':'orange'}
    try:
         pickle.dump(n, f)  #表示后面将要写入的数据个数
         pickle.dump(i, f)  #把整数i转换为字节串，并写入文件
         pickle.dump(a, f)
         pickle.dump(s, f)
         pickle.dump(lst, f)
         pickle.dump(tu, f)
         pickle.dump(coll, f)
         pickle.dump(dic, f)
    except:
        print '写文件异常!'  #如果写文件异常则跳到此处执行
    f.close( )

def func8():
    import pickle
    f=open('sample_pickle.dat', 'rb')
    n = pickle.load(f) #读出文件的数据个数
    i=0
    while i<n:
            x = pickle.load(f)
            print  x
            i=i+1
    f.close( )

def func9():
    import struct
    n=1300000000
    x=96.45
    b=True
    s='a1@中国'
    #把整数n、浮点数x、布尔对象b依次转换为字节串
    sn=struct.pack('if?', n, x, b)  
    f=open('sample_struct.dat', 'wb')
    f.write(sn)   #写入字节串 
    f.write(s)    #字符串可直接写入
    f.close( )

def func10():
    import struct
    f=open('sample_struct.dat', 'rb')
    sn=f.read(9)
    #从字节串sn中还原出1个整数、
    #1个浮点数和1个布尔值，并返回元组
    tu=struct.unpack('if?', sn) 
    print(tu)
    n=tu[0]
    x=tu[1]
    bl=tu[2]
    print 'n=', n
    print 'x=', x
    print 'bl=', bl
    s=f.read(9)
    f.close()
    print 's=', s

def func11():
    import os
    import os.path
    a=os.path.exists('sample1.txt')
    print a
    a=os.rename('sample.txt','sample1.txt')
    print a
    a=os.rename('sample1.txt','sample2.txt')       
    print a
    a=os.path.exists('sample.txt')
    print a
    a=os.path.exists('sample1.txt')
    print a
    a=os.path.exists('sample2.txt')
    print a
    #path='e:\\W7\\sample.txt'
    path = r'D:\AAATEA\R_springPYTHON2016\aENCRS\W7\sample.txt'
    print path
    a=os.path.dirname(path)
    print a
    a=os.path.split(path)
    print a
    a=os.path.splitdrive(path)
    print a
    a=os.path.splitext(path)
    print a
    
def func12():
    import os
    print os.getcwd() #返回当前工作目录
    print os.mkdir(os.getcwd()+'\\temp') #创建目录
    print os.chdir(os.getcwd()+'\\temp') #改变当前工作目录
    print os.getcwd()
    print os.mkdir(os.getcwd()+'\\test')
    print os.listdir('.')
    os.rmdir('test') #删除目录
    print os.listdir('.')

def visitDir1(path):
    if not os.path.isdir(path):
        print 'Error:"',path,'" is not a directory or does not exist.'
        return
    for lists in os.listdir(path): 
        sub_path = os.path.join(path, lists) 
        print sub_path 
        if os.path.isdir(sub_path):  
            visitDir1(sub_path) 

def visitDir2(path):
    if not os.path.isdir(path):
        print 'Error:"',path,'" is not a directory or does not exist.'
        return
    #os.walk返回一个元组，包括3个元素：
    #所有路径名、所有目录列表与文件列表
    list_dirs = os.walk(path)
    #遍历该元组的目录和文件信息
    for root, dirs, files in list_dirs:  
        for d in dirs: 
            #获取完整路径
            print os.path.join(root, d)   
        for f in files: 
            #获取文件绝对路径
            print os.path.join(root, f)   

def visitDir3(arg,dirname,names):
    for filepath in names:
        print os.path.join(dirname,filepath)


def func13():
    print('Recursion visit:\n')
    visitDir1('E:')
    print('os.walk visit:\n')
    visitDir2('E:')
    print('os.path.walk visit:\n')
    os.path.walk('E:',visitDir3,())

def delCertainFiles(directory,filetypes):
    for filename in os.listdir(directory):
        temp = os.path.join(directory, filename)       
        if os.path.isdir(temp):
            delCertainFiles(temp,filetypes)
        elif os.path.splitext(temp)[1] in filetypes: # check file extension name
            os.remove(temp)
            print(temp, ' deleted....')
def readFileTypes():
    filetypes = []
    with open('filetypes.txt', 'r') as fp:
        filetypes = fp.readlines()
    filetypes = [ext.strip() for ext in filetypes]
    return filetypes     
def func14():
    filetypes = readFileTypes()
    print(filetypes)
    delCertainFiles(os.getcwd(),filetypes)

def main():
    pass

main()
