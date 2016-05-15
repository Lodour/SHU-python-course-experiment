#coding:utf-8
## -*- coding : gbk -*-

import Tkinter as tkinter
import tkMessageBox as tkm

def login():                #登录按钮事件处理函数
    name = entryName.get()  #获取用户名
    pwd = entryPwd.get()    #获取密码
    if name=='admin' and pwd=='123456':
        tkm.showinfo(title='Python tkinter',
                                    message='OK')
    else:
        tkm.showerror('Python tkinter',
                                     message='Error')

def cancel():
    varName.set('')         #清空用户输入的用户名和密码
    varPwd.set('')

root = tkinter.Tk(screenName='User login',        #创建应用程序窗口
                  baseName='Dong Fuguo')
varName = tkinter.StringVar()
varName.set('')
varPwd = tkinter.StringVar()
varPwd.set('')

labelName = tkinter.Label(root, text='User Name:', #创建标签
                          justify=tkinter.RIGHT,
                          width=80)
labelName.place(x=10, y=5, width=80, height=20)    #将标签放到窗口上

entryName = tkinter.Entry(root, width=80,          #创建文本框
                          textvariable=varName)    #同时设置关联的变量
entryName.place(x=100, y=5, width=80, height=20)

labelPwd = tkinter.Label(root, text='User    Pwd:',
                         justify=tkinter.RIGHT,
                         width=80)
labelPwd.place(x=10, y=30, width=80, height=20)

entryPwd = tkinter.Entry(root, show='*',           #创建密码文本框
                         width=80,
                         textvariable=varPwd)
entryPwd.place(x=100, y=30, width=80, height=20)

buttonOk = tkinter.Button(root, text='Login',      #创建按钮组件
                          command=login)           #同时设置按钮事件处理函数
buttonOk.place(x=30, y=70, width=50, height=20)

buttonCancel = tkinter.Button(root, text='Cancel', command=cancel)
buttonCancel.place(x=90, y=70, width=50, height=20)


root.mainloop()          #启动消息循环
