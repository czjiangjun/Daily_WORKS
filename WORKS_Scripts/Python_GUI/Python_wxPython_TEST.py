#!/usr/bin/env ~/.local/bin/python3

"""
ZetCode wxPython tutorial

In this example we create a new class layout
with wx.GridBagSizer.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):

        panel = wx.Panel(self)

        sizer = wx.GridBagSizer(5, 5)

        text1 = wx.StaticText(panel, label="Model_From_File")
        sizer.Add(text1, pos=(1, 0), flag=wx.TOP|wx.LEFT, border=10)

        combo = wx.ComboBox(panel)
        sizer.Add(combo, pos=(1, 1), span=(1, 3),
            flag=wx.TOP|wx.EXPAND, border=5)

        button1 = wx.Button(panel, label="Browse...")
        sizer.Add(button1, pos=(1, 4), flag=wx.TOP|wx.RIGHT, border=5)

        text2 = wx.StaticText(panel, label="Model_Creative")
        sizer.Add(text2, pos=(3, 0), flag=wx.TOP|wx.CENTER|wx.BOTTOM,
            border=15)

        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('exec.png'))
        sizer.Add(icon, pos=(3, 4), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,
            border=5)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(4, 0), span=(1, 5),
            flag=wx.EXPAND|wx.BOTTOM, border=10)

        sb = wx.StaticBox(panel, label="Optional Attributes")

#        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
        boxsizer.Add(wx.CheckBox(panel, label="Atoms_Model"),
            flag=wx.LEFT|wx.TOP, border=5)
        self.cb2 = boxsizer.Add(wx.CheckBox(panel, label="Cell_Model"),
            flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="Surface_Model"),
            flag=wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(boxsizer, pos=(2, 0), span=(1, 5),
            flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)

        text3 = wx.StaticText(panel, label="Elements")
        sizer.Add(text3, pos=(5, 0), flag=wx.LEFT, border=10)

        Element_Name = wx.TextCtrl(panel)
        sizer.Add(Element_Name, pos=(5, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)
        self.Elements = Element_Name

        list = [str(i) for i in range(100)]
#        print(list)
        ch = wx.ComboBox(panel, value ='', choices= list, style=wx.CB_SORT)

        text4 = wx.StaticText(panel, label="Atom_Position:")
        sizer.Add(text4, pos=(6, 0), flag=wx.LEFT|wx.TOP, border=5)

        tc2 = wx.TextCtrl(panel)
        sizer.Add(tc2, pos=(6, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
            border=8)
        tc3 = wx.TextCtrl(panel)
        sizer.Add(tc3, pos=(6, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
            border=8)
        tc4 = wx.TextCtrl(panel)
        sizer.Add(tc4, pos=(6, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
            border=8)


#        self.Bind(wx.EVT_CHECKBOX, self.setcell)
        text_Cell = wx.StaticText(panel, label="Cell_parameter")
        sizer.Add(text_Cell, pos=(7, 0), flag=wx.LEFT|wx.TOP, border=10)

        text_x_vector = wx.StaticText(panel, label="x_vector:")
        sizer.Add(text_x_vector, pos=(8, 0), flag=wx.LEFT|wx.TOP, border=5)

        tc_xx = wx.TextCtrl(panel)
        sizer.Add(tc_xx, pos=(8, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
            border=8)
        tc_xy = wx.TextCtrl(panel)
        sizer.Add(tc_xy, pos=(8, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
            border=8)
        tc_xz = wx.TextCtrl(panel)
        sizer.Add(tc_xz, pos=(8, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
            border=8)

        text_y_vector = wx.StaticText(panel, label="y_vector:")
        sizer.Add(text_y_vector, pos=(9, 0), flag=wx.LEFT|wx.TOP, border=5)

        tc_yx = wx.TextCtrl(panel)
        sizer.Add(tc_yx, pos=(9, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
            border=8)
        tc_yy = wx.TextCtrl(panel)
        sizer.Add(tc_yy, pos=(9, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
            border=8)
        tc_yz = wx.TextCtrl(panel)
        sizer.Add(tc_yz, pos=(9, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
            border=8)

        text_z_vector = wx.StaticText(panel, label="z_vector:")
        sizer.Add(text_z_vector, pos=(10, 0), flag=wx.LEFT|wx.TOP, border=5)

        tc_zx = wx.TextCtrl(panel)
        sizer.Add(tc_zx, pos=(10, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
            border=8)
        tc_zy = wx.TextCtrl(panel)
        sizer.Add(tc_zy, pos=(10, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
            border=8)
        tc_zz = wx.TextCtrl(panel)
        sizer.Add(tc_zz, pos=(10, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
            border=8)

        self.tc_xx = tc_xx
        self.tc_xy = tc_xy
        self.tc_xz = tc_xz
        self.tc_yx = tc_yx
        self.tc_yy = tc_yy
        self.tc_yz = tc_yz
        self.tc_zx = tc_zx
        self.tc_zy = tc_zy
        self.tc_zz = tc_zz

#        button1 = wx.Button(panel, label="Browse...")
#        sizer.Add(button1, pos=(3, 4), flag=wx.TOP|wx.RIGHT, border=5)

        button2 = wx.Button(panel, label='Help')
        sizer.Add(button2, pos=(11, 0), flag=wx.LEFT, border=10)

        button3 = wx.Button(panel, label="Ok")
        sizer.Add(button3, pos=(11, 3))

        button4 = wx.Button(panel, label="Cancel")
        sizer.Add(button4, pos=(11, 4), span=(1, 1),
            flag=wx.BOTTOM|wx.RIGHT, border=10)

        sizer.AddGrowableCol(2)

        panel.SetSizer(sizer)
        sizer.Fit(self)
        
        print('TEST')
        self.Bind(wx.EVT_BUTTON, self.printout, button3)
        self.Bind(wx.EVT_BUTTON, self.clear, button4)

    def printout(self, event):
        prime_cell = []

        x_x = float(self.tc_xx.GetValue())
        x_y = float(self.tc_xy.GetValue())
        x_z = float(self.tc_xz.GetValue())
        x_vector = (x_x,x_y,x_z)
        prime_cell.append(x_vector)
        y_x = float(self.tc_xx.GetValue())
        y_y = float(self.tc_xy.GetValue())
        y_z = float(self.tc_xz.GetValue())
        y_vector = (y_x,y_y,y_z)
        prime_cell.append(y_vector)
        z_x = float(self.tc_xx.GetValue())
        z_y = float(self.tc_xy.GetValue())
        z_z = float(self.tc_xz.GetValue())
        z_vector = (z_x,z_y,z_z)
        prime_cell.append(z_vector)

        print(self.Elements.GetValue())
        print(prime_cell)
        exit()
        return

    def clear(self,event):
        exit()

#    def setcell(self, event):

#        panel = wx.Panel(self)

#        sizer = wx.GridBagSizer(5, 5)

#        text_Cell = wx.StaticText(panel, label="Cell_parameter")
#        sizer.Add(text_Cell, pos=(7, 0), flag=wx.LEFT|wx.TOP, border=10)

#        text_x_vector = wx.StaticText(panel, label="x_vector:")
#        sizer.Add(text_x_vector, pos=(8, 0), flag=wx.LEFT|wx.TOP, border=5)

#        tc_xx = wx.TextCtrl(panel)
#        sizer.Add(tc_xx, pos=(8, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
#            border=8)
#        tc_xy = wx.TextCtrl(panel)
#        sizer.Add(tc_xy, pos=(8, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
#            border=8)
#        tc_xz = wx.TextCtrl(panel)
#        sizer.Add(tc_xz, pos=(8, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
#            border=8)

#        text_y_vector = wx.StaticText(panel, label="y_vector:")
#        sizer.Add(text_y_vector, pos=(9, 0), flag=wx.LEFT|wx.TOP, border=5)

#        tc_yx = wx.TextCtrl(panel)
#        sizer.Add(tc_yx, pos=(9, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
#            border=8)
#        tc_yy = wx.TextCtrl(panel)
#        sizer.Add(tc_yy, pos=(9, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
#            border=8)
#        tc_yz = wx.TextCtrl(panel)
#        sizer.Add(tc_yz, pos=(9, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
#            border=8)

#        text_z_vector = wx.StaticText(panel, label="z_vector:")
#        sizer.Add(text_z_vector, pos=(10, 0), flag=wx.LEFT|wx.TOP, border=5)

#        tc_zx = wx.TextCtrl(panel)
#        sizer.Add(tc_zx, pos=(10, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
#            border=8)
#        tc_zy = wx.TextCtrl(panel)
#        sizer.Add(tc_zy, pos=(10, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
#            border=8)
#        tc_zz = wx.TextCtrl(panel)
#        sizer.Add(tc_zz, pos=(10, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
#            border=8)
#
#        self.tc_xx = tc_xx
#        self.tc_xy = tc_xy
#        self.tc_xz = tc_xz
#        self.tc_yx = tc_yx
#        self.tc_yy = tc_yy
#        self.tc_yz = tc_yz
#        self.tc_zx = tc_zx
#        self.tc_zy = tc_zy
#        self.tc_zz = tc_zz
#        return

def main():

    app = wx.App()
    ex = Example(None, title="Model_Creative_TEST")
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
