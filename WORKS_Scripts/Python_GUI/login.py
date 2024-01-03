import wx
import wx.xrc
import sys
import AtomateTest

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"高通量材料计算系统", pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 247 ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.staticText001 = wx.StaticText( self, wx.ID_ANY, u"登录系统", wx.DefaultPosition, wx.Size( 200,50 ), 0 )
		self.staticText001.Wrap( -1 )

		self.staticText001.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )
		self.staticText001.SetForegroundColour( wx.Colour( 7, 84, 177 ) )

		bSizer5.Add( self.staticText001, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"账号：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		wSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER, 5 )


		bSizer5.Add( wSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer3 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"密码：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		wSizer3.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		wSizer3.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_CENTER, 5 )


		bSizer5.Add( wSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer4 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"登录", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer4.Add( self.m_button2, 0, wx.ALL, 5 )


		bSizer5.Add( wSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		wSizer6 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer6.Add( self.m_button4, 0, wx.ALL, 5 )


		bSizer5.Add( wSizer6, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.Login )
		self.m_button4.Bind( wx.EVT_BUTTON, self.Quit )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Login( self, event ):
		if self.m_textCtrl1.GetValue() == "123456" and self.m_textCtrl2.GetValue() == "abc123":
			self.Destroy()
#                       AtomateTest.main()
			event.Skip()
		else:
			wx.MessageBox("用户名或密码错误","提示信息", wx.OK | wx.ICON_INFORMATION)

	def Quit( self, event ):
		sys.exit()

class mainApp(wx.App):
	def OnInit(self):
		self.SetAppName(u"zzz")
		self.Frame = MyFrame1(None)
		self.Frame.Show()
		return True

if __name__ == "__main__":
	app = mainApp(redirect=True)
	app.MainLoop()
	AtomateTest.main()

