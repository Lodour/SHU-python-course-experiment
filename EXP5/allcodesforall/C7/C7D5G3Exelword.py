#coding:utf-8
## -*- coding : gbk -*-

##使用xlwt写入Excel文件
from xlwt import *
book = Workbook()
sheet1 = book.add_sheet("First")
al=Alignment()
al.horz=Alignment.HORZ_CENTER
al.vert=Alignment.VERT_CENTER
borders=Borders()
borders.bottom=Borders.THICK
style=XFStyle()
style.alignment=al
style.borders=borders
row0=sheet1.row(0)
row0.write(0,'test',style=style)
book.save(r'd:\test.xls')

##使用xlrd读取Excel文件
import xlrd
book = xlrd.open_workbook(r'd:\test.xls')
sheet1 = book.sheet_by_name('First')
row0 = sheet1.row(0)
print row0[0]
print row0[0].value

##使用Pywin32操作Excel文件
xlApp = win32com.client.Dispatch('Excel.Application')  #打开EXCEL
xlBook = xlApp.Workbooks.Open('D:\\1.xls')  
xlSht = xlBook.Worksheets('sheet1') 
aaa = xlSht.Cells(1,2).Value 
xlSht.Cells(2,3).Value = aaa 
xlBook.Close(SaveChanges=1) 
del xlApp 

##检查word文档的连续重复字
import sys
from win32com import client
#filename = sys.argv[1]
filename = r'c:\test.doc'
word = client.Dispatch('Word.Application')
#newdoc = word.Documents.Add()
doc = word.Documents.Open(filename)
content = str(doc.Content)
doc.Close()
#newdoc.Close()
word.Quit()
repeatedWords = []
lens = len(content)
for i in range(lens-2):
    ch = content[i]
    ch1 = content[i+1]
    ch2 = content[i+2]
    if (u'\u4e00'<=ch<=u'\u9fa5' or ch in ('，', '。', '、')):
        if ch==ch1 and ch+ch1 not in repeatedWords:
            print(ch+ch1)
            repeatedWords.append(ch+ch1)
        elif ch==ch2 and ch+ch1+ch2 not in repeatedWords:
            print(ch+ch1+ch2)
            repeatedWords.append(ch+ch1+ch2)

