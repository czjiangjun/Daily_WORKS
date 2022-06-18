import wx
import pymysql,time,threading
from MySQL import Make_bill,function
class Withdrawal1(wx.App):
  def doClose(self,j):
    time.sleep(j)
    self.frame.Close()
  def __init__(self,YuanZhangH):
    self.YuanZhangH=YuanZhangH
    wx.App.__init__(self)
    self.frame = wx.Frame(parent=None,title='取 款',size=(535,450),style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX )
    panel=wx.Panel(self.frame,-1)
    label_pass = wx.StaticText(panel,-1,"取款金额:", pos=(80,200))
    #style 为设置输入
    self.JinE = wx.TextCtrl(panel,-1, size=(250,35), pos=(140,190))
    self.QueDing_button = wx.Button(panel, -1, "确    认", size=(80,60), pos=(120,280))
    self.QuXiao_button     = wx.Button(panel, -1, "反    回", size=(80, 60), pos=(340,280))
    self.QueDing_button.SetBackgroundColour('#0a74f7')
    self.QuXiao_button.SetBackgroundColour('#0a74f7')
    self.Bind(wx.EVT_BUTTON, self.QuK, self.QueDing_button)
    self.Bind(wx.EVT_BUTTON, self.QU, self.QuXiao_button)  #通过一个按钮触发界面跳转
    self.frame.Center()
    self.frame.Show(True)
  def QuK(self, event):
    pass
  def QU(self, event):
    t = threading.Thread(target=self.doClose, args=(0.05,))
    t.start()              #通过threading和doClose函数关闭界面
    jie = function.Jiemian(self.YuanZhangH) #打开新界面  
    jie.MainLoop()
