#-*- coding:utf-8 -*-
from tkinter import *
from tkinter import ttk
import threading
import time
from win10toast import ToastNotifier

class MyThread(threading.Thread):
    def __init__(self, func, *args):
        super().__init__()
        
        self.func = func
        self.args = args
        
        self.setDaemon(True)
        self.start()  # 在这里开始
        
    def run(self):
        self.func(*self.args)

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    #设置窗口
    def set_init_window(self): 
        self.init_window_name.title("久坐提醒小助手")
        self.init_window_name.geometry('500x300')

        Label(self.init_window_name, text='请在下面输入必要的信息以启动程序', font=('Arial', 15)).pack()

        frm = Frame(self.init_window_name)

        #left
        frm_L = Frame(frm)
        Label(frm_L, text='您的昵称', font=('Arial', 15)).pack(side=TOP)
        Label(frm_L, text='重复次数', font=('Arial', 15)).pack(side=TOP)
        Label(frm_L, text='间隔时间（分钟）', font=('Arial', 15)).pack(side=TOP)
        frm_L.pack(side=LEFT)

        #right
        frm_R = Frame(frm)
        self.text1 = Text(frm_R,font=('Arial', 15),width=11,height=1)
        self.text1.pack(side=TOP)
        self.cmb1 = ttk.Combobox(frm_R, value=('1','2','3','4','5','6','7','8','9','10'), font=('Arial', 15),width=10,height=1)
        self.cmb1.pack(side=TOP)
        self.cmb2 = ttk.Combobox(frm_R, value=('10','20','30','40','50','60'), font=('Arial', 15),width=10,height=1)
        self.cmb2.pack(side=TOP)
        frm_R.pack(side=RIGHT) 
        frm.pack()

        Button(self.init_window_name, text="开始运行", command = lambda: MyThread(self.youshouldrest)).pack()

        self.log_data_Text = Text(self.init_window_name, width=60, height=9)  # 日志框
        self.log_data_Text.pack()

    def youshouldrest(self):
        self.name = self.text1.get(1.0,END).strip().replace("\n","")
        self.times = int(self.cmb1.get())
        self.second = int(self.cmb2.get())
        self.log_data_Text.insert(1.0,'开始运行程序'+'\n')
        toaster = ToastNotifier()
        for i in range(self.times):
            time.sleep(self.second*60)
            toaster.show_toast('Hello,'+self.name,'It\'s time to rest.Go!Go!Go!',duration=10)

def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()
