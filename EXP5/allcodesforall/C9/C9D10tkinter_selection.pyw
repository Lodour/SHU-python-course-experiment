#coding:utf-8
## -*- coding : gbk -*-
import Tkinter as tkinter
import tkMessageBox as tkm
import ttk

root = tkinter.Tk()
root.title('Selection widgets---by Dong Fuguo')   #窗口标题
root['height'] = 400                              #定义窗口大小
root['width'] = 320

varName = tkinter.StringVar()                     #与姓名关联的变量
varName.set('')

labelName = tkinter.Label(root, text='Name:',     #创建标签
                          justify=tkinter.RIGHT,
                          width=50)
labelName.place(x=10, y=5, width=50, height=20)   #将标签放到窗口上

entryName = tkinter.Entry(root, width=120,        #创建文本框
                          textvariable=varName)   #同时设置关联的变量
entryName.place(x=70, y=5, width=120, height=20)

labelGrade = tkinter.Label(root, text='Grade:',
                           justify=tkinter.RIGHT,
                           width=50)
labelGrade.place(x=10, y=40, width=50, height=20)

studentClasses = {'1':['1', '2', '3', '4'],       #模拟学生所在年级
                  '2':['1', '2'],                 #字典键为年级
                  '3':['1', '2', '3']}            #字典值为班级
comboGrade = ttk.Combobox(root,           #学生年级组合框
                                  values=tuple(studentClasses.keys()),
                                  width=50)
comboGrade.place(x=70, y=40, width=50, height=20)
def comboChange(event):                           #事件处理函数
    grade = comboGrade.get()
    if grade:                                     #动态改变组合框可选项
        comboClass["values"] = studentClasses.get(grade)
    else:
        comboClass.set([])
        
comboGrade.bind('<<ComboboxSelected>>', comboChange)#绑定组合框事件处理函数

labelClass = tkinter.Label(root, text='Class:',
                           justify=tkinter.RIGHT,
                           width=50)
labelClass.place(x=130, y=40, width=50, height=20)

comboClass = ttk.Combobox(root,           #学生年级组合框
                                  width=50)
comboClass.place(x=190, y=40, width=50, height=20)

labelSex = tkinter.Label(root, text='Sex:',       #性别
                         justify=tkinter.RIGHT,
                         width=50)
labelSex.place(x=10, y=70, width=50, height=20)

sex = tkinter.IntVar()                            #与性别关联的变量
sex.set(1)                                        #1:男；0:女，默认为男

radioMan = tkinter.Radiobutton(root,              #单选钮，男
                               variable=sex,
                               value=1,
                               text='Man')
radioMan.place(x=70, y=70, width=50, height=20)
radioWoman = tkinter.Radiobutton(root,            #单选钮，女
                               variable=sex,
                               value=0,
                               text='Woman')
radioWoman.place(x=130, y=70, width=70, height=20)

monitor = tkinter.IntVar()                        #与是否班长关联的变量
monitor.set(0)                                    #默认当前学生不是班长
checkMonitor = tkinter.Checkbutton(root,
                                   text='Is Monitor?',
                                   variable=monitor,
                                   onvalue=1,     #选中时变量值为1
                                   offvalue=0)    #未选中时变量值为0
checkMonitor.place(x=20, y=100, width=100, height=20)

def addInformation():                             #按钮事件处理函数
    result = 'Name:' + entryName.get()
    result = result + ';Grade:' + comboGrade.get()
    result = result + ';Class:' + comboClass.get()
    result = result + ';Sex:' + ('Man' if sex.get() else 'Woman')
    result = result + ';Monitor:' + ('Yes' if monitor.get() else 'No')
    listboxStudents.insert(0, result)
    
buttonAdd = tkinter.Button(root, text='Add',      #创建按钮组件
                           width=40,
                           command=addInformation)
buttonAdd.place(x=130, y=100, width=40, height=20)

def deleteSelection():
    selection = listboxStudents.curselection()
    if  not selection:
        tkm.showinfo(title='Information', message='No Selection')
    else:
        listboxStudents.delete(selection)
        
buttonDelete = tkinter.Button(root, text='DeleteSelection',
                           width=100,
                           command=deleteSelection)
buttonDelete.place(x=180, y=100, width=100, height=20)

listboxStudents = tkinter.Listbox(root, width=300)#创建列表框组件
listboxStudents.place(x=10, y=130, width=300, height=200)

root.mainloop()
