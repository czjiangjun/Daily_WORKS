#!/usr/bin/env ~/.local/bin/python3
#-*- coding:utf-8 -*-
import os
import wx

# WXPython的helloWord版本
# class MyApp(wx.App):
#     def OnInit(self):  #初始化接口，子类覆盖父类的方法
#         frame=wx.Frame(parent=None,title="hello wxpython")  #新建框架
#         frame.Show()  #显示
#         return True

# wxPython添加按钮
# class MyApp(wx.App):
#     def OnInit(self):  #初始化接口，子类覆盖父类的方法
#         frame=wx.Frame(parent=None,title="hello wxpython")  #新建框架
#         panel=wx.Panel(frame,-1)     #生成面板
#         button=wx.Button(panel,-1,'hello',pos=(50,50))   #确定按钮位置

#         frame.Show()  #显示
#         return True

# wxPython添加按钮的监听
# class MyApp(wx.App):
#     def OnInit(self):  #初始化接口，子类覆盖父类的方法
#         frame=wx.Frame(parent=None,title="hello wxpython")  #新建框架
#         panel=wx.Panel(frame,-1)     #生成面板
#         button=wx.Button(panel,-1,'hello',pos=(50,50))   #确定按钮位置
#         self.button1=button
#         self.Bind(wx.EVT_BUTTON,  #绑定事件，如果是按钮被点击
#                   self.OnButton1, #激发的按钮事件
#                   self.button1)   #激发的按钮
#         frame.Show()  #显示
#         return True

#     def OnButton1(self,event):  #事件的激发函数
#         self.button1.SetLabel("ni")

# wxPython添加标签和输入框
# class MyApp(wx.App):
#     def OnInit(self):  # 初始化接口，子类覆盖父类的方法
#         frame = wx.Frame(parent=None, title="hello wxpython")  # 新建框架
#         panel = wx.Panel(frame, -1)  # 生成面板
#         label1=wx.StaticText(panel,-1,"MutilLine",pos=(20,30))  #标签
#         text1=wx.TextCtrl(panel,-1,pos=(10,30),size=(180,30),   #输入框
#                            style=wx.TE_MULTILINE)
#         button = wx.Button(panel, -1, 'hello', pos=(50, 50))  # 确定按钮位置
#         frame.Show()  # 显示
#         return True

# 将事件监听和按钮绑定
class MyApp(wx.App):
    def OnInit(self):  # 初始化接口，子类覆盖父类的方法
        frame = wx.Frame(parent=None, title="hello wxpython")  # 新建框架
        panel = wx.Panel(frame, -1)  # 生成面板
        label1=wx.StaticText(panel,-1,"cmd tools",pos=(10,10))  #标签
        text1=wx.TextCtrl(panel,-1,pos=(10,150),size=(180,30),   #输入框
                           style=wx.TE_MULTILINE)
        button = wx.Button(panel,-1, 'run', pos=(10, 50))  # 确定按钮位置
        self.text1=text1          #方便跨函数调用
        self.button1 = button
        self.Bind(wx.EVT_BUTTON,  # 绑定事件，如果是按钮被点击
                  self.OnButton1,  # 激发的按钮事件
                  self.button1)  # 激发的按钮
        frame.Show()  # 显示
        return True

    def OnButton1(self,event):  #事件的激发函数
        self.button1.SetLabel("ni")
        print(self.text1.GetValue())  #获取到输入的信息

# wxPython制作一个登录界面
class MyApp(wx.App):
    def OnInit(self):  # 初始化接口，子类覆盖父类的方法
        frame = wx.Frame(parent=None, title="用户登录")  # 新建框架
        panel = wx.Panel(frame, -1)  # 生成面板
        label1=wx.StaticText(panel,-1,"user",pos=(10,10))  #标签
        text1=wx.TextCtrl(panel,-1,pos=(80,10),size=(180,30),   #输入框
                           style=wx.TE_MULTILINE)
        label2 = wx.StaticText(panel, -1, "password", pos=(10, 60))  # 标签
        text2 = wx.TextCtrl(panel, -1, pos=(80, 60), size=(180, 30),  # 输入框
                            style=wx.TE_MULTILINE)

        button1 = wx.Button(panel,-1, 'login', pos=(80, 110))  # 确定按钮位置
        button2 = wx.Button(panel, -1, 'clear', pos=(180, 110))  # 确定按钮位置

        self.text1 = text1          # 方便跨函数调用
        self.text2 = text2          # 方便跨函数调用
        self.button1 = button1      # 方便跨函数调用
        self.button2 = button2      # 方便跨函数调用

        self.Bind(wx.EVT_BUTTON,  # 绑定事件，如果是按钮被点击
                  self.login,  # 激发的按钮事件
                  self.button1)  # 激发的按钮
        self.Bind(wx.EVT_BUTTON,  # 绑定事件，如果是按钮被点击
                  self.clear,  # 激发的按钮事件
                  self.button2)  # 激发的按钮

        frame.Show()  # 显示
        return True

    #def OnButton1(self,event):  #事件的激发函数
        #self.button1.SetLabel("ni")
        #print(self.text1.GetValue())  #获取到输入的信息
    def login(self,event):      #事件的激发函数
        user = self.text1.GetValue()  #获取用户名
        password = self.text2.GetValue()  #获取密码
        if user == "leo" and password == "123456":
            wx.MessageBox("OK","info",wx.OK|wx.ICON_INFORMATION)
        else:
            wx.MessageBox("NO", "info", wx.OK|wx.ICON_INFORMATION)
    def clear(self,event):
        pass

app=MyApp()      #启动
app.MainLoop()   #进入消息循环
