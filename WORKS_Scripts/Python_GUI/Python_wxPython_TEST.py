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
        self.panel = panel

        panel2 = wx.Panel(self)
        self.panel2 = panel2

        sizer = wx.GridBagSizer(5, 5)
        self.sizer = sizer

#        self.panel2 = panel
#        self.sizer2 = sizer

        text1 = wx.StaticText(panel, label="Model_From_File")
        sizer.Add(text1, pos=(1, 0), flag=wx.TOP|wx.LEFT, border=10)

        combo = wx.ComboBox(panel)
        self.combo = combo
        sizer.Add(combo, pos=(1, 1), span=(1, 3),
            flag=wx.TOP|wx.EXPAND, border=5)
        self.list_path = []

        button1 = wx.Button(panel, label="Browse...")
        sizer.Add(button1, pos=(1, 4), flag=wx.TOP|wx.RIGHT, border=5)

        self.Fileload = False
        self.Bind(wx.EVT_BUTTON, self.load, button1)
#        print(self.load)

        text2 = wx.StaticText(panel, label="Model_Creative")
        sizer.Add(text2, pos=(2, 0), flag=wx.TOP|wx.CENTER|wx.BOTTOM,
            border=15)

        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('/home/jun_jiang/Documents/Latex_art_beamer/Presentation_Beamer/Figures/BCC_logo-2.jpg'))
#        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('/home/jun_jiang/Documents/Latex_Beamer/Figures/BCC_logo-2.jpg'))
        sizer.Add(icon, pos=(2, 1), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,
            border=1)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(3, 0), span=(1, 5),
            flag=wx.EXPAND|wx.BOTTOM, border=10)

        sb = wx.StaticBox(panel, label="Optional Attributes")

#        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
#        boxsizer.Add(wx.CheckBox(panel, label="Atoms_Model"),
#            flag=wx.LEFT|wx.TOP, border=5)
        self.cellgen = wx.CheckBox(panel, label="Cell_Model")
        self.cb2 = boxsizer.Add(self.cellgen,
            flag=wx.LEFT, border=5)
#        boxsizer.Add(wx.CheckBox(panel, label="Surface_Model"),
#            flag=wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(boxsizer, pos=(4, 0), span=(1, 5),
            flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)

        self.checkcell = True
        self.prime_cell = []
        self.Bind(wx.EVT_CHECKBOX, self.setcell)

        text3 = wx.StaticText(panel, label="Elements")
        sizer.Add(text3, pos=(9, 0), flag=wx.LEFT, border=10)

        Element_Name = wx.TextCtrl(panel)
#        sizer.Add(Element_Name, pos=(5, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)
        sizer.Add(Element_Name, pos=(9, 1), span=(1, 1), flag=wx.TOP)
        self.Elements = Element_Name

        text_num = wx.StaticText(panel, label="Tot_Num")
        sizer.Add(text_num, pos=(9, 2), flag=wx.LEFT, border=10)

        list = [str(i+1) for i in range(5)]
#        print(list)
        self.ch = wx.ComboBox(panel, pos=(400, 360), value ='1', choices= list, style=wx.CB_SIMPLE, name = "Num_of_Ele")
#        sizer.Add(ch,  )
        button_Genatom = wx.Button(panel, label='Gen_Post')
        sizer.Add(button_Genatom, pos=(9, 3), flag=wx.LEFT, border=10)

        self.addatom_pos = []
        self.Bind(wx.EVT_BUTTON, self.setposition_atoms, button_Genatom)

        self.addatom = False

#        text5 = wx.StaticText(panel, label="Atom_Position:")
#        sizer.Add(text5, pos=(10, 0), flag=wx.LEFT|wx.TOP, border=5)

#        tc2 = wx.TextCtrl(panel)
#        sizer.Add(tc2, pos=(10, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
#            border=8)
#        pos_x = float(tc2.GetValue())
#        tc3 = wx.TextCtrl(panel)
#        sizer.Add(tc3, pos=(10, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
#            border=8)
#        pos_y = float(tc3.GetValue())
#        tc4 = wx.TextCtrl(panel)
#        sizer.Add(tc4, pos=(10, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
#            border=8)
#        pos_z = float(tc4.GetValue())
#        post = (pos_x, pos_y, pos_z)
#        self.addatom.append(post)
#

        button2 = wx.Button(panel, label='Help')
        sizer.Add(button2, pos=(17, 0), flag=wx.LEFT, border=10)

        button3 = wx.Button(panel, label="Ok")
        sizer.Add(button3, pos=(17, 3))

        button4 = wx.Button(panel, label="Cancel")
        sizer.Add(button4, pos=(17, 4), span=(1, 1),
            flag=wx.BOTTOM|wx.RIGHT, border=10)

        sizer.AddGrowableCol(2)

        panel.SetSizer(sizer)
        sizer.Fit(self)
        
        print('TEST')

        self.Bind(wx.EVT_BUTTON, self.printout, button3)
        self.Bind(wx.EVT_BUTTON, self.clear, button4)
#        exit()
    def printout(self, event):

        if self.Fileload:
           print(self.file)
        else:
           print(self.Elements.GetValue())

           if (self.addatom):
             atom_positions = []
             k = int(self.ch.GetValue())
             for i in range(k):

                pos_ix = float(self.addatom_pos[3*i+0].GetValue())
                pos_iy = float(self.addatom_pos[3*i+1].GetValue())
                pos_iz = float(self.addatom_pos[3*i+2].GetValue())
                pos = (pos_ix, pos_iy, pos_iz)

                atom_positions.append(pos)

           if (self.cellgen.GetValue()):
              x_x = float(self.tc_xx.GetValue())
              x_y = float(self.tc_xy.GetValue())
              x_z = float(self.tc_xz.GetValue())
              x_vector = (x_x,x_y,x_z)
              self.prime_cell.append(x_vector)
              y_x = float(self.tc_yx.GetValue())
              y_y = float(self.tc_yy.GetValue())
              y_z = float(self.tc_yz.GetValue())
              y_vector = (y_x,y_y,y_z)
              self.prime_cell.append(y_vector)
              z_x = float(self.tc_zx.GetValue())
              z_y = float(self.tc_zy.GetValue())
              z_z = float(self.tc_zz.GetValue())
              z_vector = (z_x,z_y,z_z)
              self.prime_cell.append(z_vector)

           print(self.prime_cell)
           print(atom_positions)
           exit()

    def clear(self,event):
        exit()


    def setposition_atoms(self, event):

        self.Fileload = False
        k = int(self.ch.GetValue())
        print(k)
        if (not self.addatom):
           for i in range(k):
               self.addatom_pos.append (0)
               self.addatom_pos.append (0)
               self.addatom_pos.append (0)
               j = 11+i

               pos_vector = wx.StaticText(self.panel, label="Atom_position:")
               self.sizer.Add(pos_vector, pos=(j, 0), flag=wx.LEFT|wx.TOP, border=5)
 
               pos_x = wx.TextCtrl(self.panel)
               self.sizer.Add(pos_x, pos=(j, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
                    border=8)
               pos_y = wx.TextCtrl(self.panel)
               self.sizer.Add(pos_y, pos=(j, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
                    border=8)
               pos_z = wx.TextCtrl(self.panel)
               self.sizer.Add(pos_z, pos=(j, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
                    border=8)
               self.addatom_pos[3*i+0] = pos_x
               self.addatom_pos[3*i+1] = pos_y
               self.addatom_pos[3*i+2] = pos_z

               self.addatom = True

        else:
            pass
        return

    def setcell(self, event):


        sizer2 = wx.GridBagSizer(5, 5)
        self.sizer2 = sizer2
        self.Fileload = False
        self.panel.Hide()
        if (self.cellgen.GetValue() and self.checkcell):

           text_Cell = wx.StaticText(self.panel2, label="Cell_parameter")
           self.sizer2.Add(text_Cell, pos=(1, 0), flag=wx.LEFT|wx.TOP, border=10)
           self.text = text_Cell

           text_x_vector = wx.StaticText(self.panel2, label="x_vector:")
           self.sizer2.Add(text_x_vector, pos=(2, 0), flag=wx.LEFT|wx.TOP, border=5)
           self.x_vector = text_x_vector 

           tc_xx = wx.TextCtrl(self.panel2)
           self.sizer2.Add(tc_xx, pos=(2, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
                border=8)
           tc_xy = wx.TextCtrl(self.panel2)
           self.sizer2.Add(tc_xy, pos=(2, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
                border=8)
           tc_xz = wx.TextCtrl(self.panel2)
           self.sizer2.Add(tc_xz, pos=(2, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
                border=8)

           text_y_vector = wx.StaticText(self.panel2, label="y_vector:")
           self.sizer2.Add(text_y_vector, pos=(3, 0), flag=wx.LEFT|wx.TOP, border=5)
           self.y_vector = text_y_vector 

           tc_yx = wx.TextCtrl(self.panel2)
           self.sizer2.Add(tc_yx, pos=(3, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
                border=8)
           tc_yy = wx.TextCtrl(self.panel2)
           self.sizer2.Add(tc_yy, pos=(3, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
                border=8)
           tc_yz = wx.TextCtrl(self.panel2)
           self.sizer2.Add(tc_yz, pos=(3, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
                border=8)

           text_z_vector = wx.StaticText(self.panel2, label="z_vector:")
           self.sizer2.Add(text_z_vector, pos=(4, 0), flag=wx.LEFT|wx.TOP, border=5)
           self.z_vector = text_z_vector 

           tc_zx = wx.TextCtrl(self.panel2)
           self.sizer2.Add(tc_zx, pos=(4, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
                border=8)
           tc_zy = wx.TextCtrl(self.panel2)
           self.sizer2.Add(tc_zy, pos=(4, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
                border=8)
           tc_zz = wx.TextCtrl(self.panel2)
           self.sizer2.Add(tc_zz, pos=(4, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
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

           self.checkcell = False
        elif (self.cellgen.GetValue() and (not self.checkcell)):
           self.text.Show()
           self.x_vector.Show()
           self.y_vector.Show()
           self.z_vector.Show()
           self.tc_xx.Show()
           self.tc_xy.Show()
           self.tc_xz.Show()
           self.tc_yx.Show()
           self.tc_yy.Show()
           self.tc_yz.Show()
           self.tc_zx.Show()
           self.tc_zy.Show()
           self.tc_zz.Show()
        elif (not self.cellgen.GetValue()) :
#           text_Cell = wx.StaticText(self.panel, label="Cell_parameter")
           self.text.Hide()
           self.x_vector.Hide()
           self.y_vector.Hide()
           self.z_vector.Hide()
           self.tc_xx.Hide()
           self.tc_xy.Hide()
           self.tc_xz.Hide()
           self.tc_yx.Hide()
           self.tc_yy.Hide()
           self.tc_yz.Hide()
           self.tc_zx.Hide()
           self.tc_zy.Hide()
           self.tc_zz.Hide()

           self.prime_cell = []
        else:
           pass
        return

    def load(self, event):
        dialog = wx.FileDialog(None, 'Select A File', style=wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.file = dialog.GetPath()
#            self.text.write(file.read())
#            file.close()
            self.list_path.append(self.file)
            self.combo.Hide()
            wx.ComboBox(self.panel, pos=(150, 30), value = self.file, style = wx.CB_DROPDOWN, 
                    choices = self.list_path, name = "Num_of_Ele", size=(400,30))
            self.Fileload = True
#            exit()

        dialog.Destroy()
#        path = fileName.GetValue()
#        with open(path, "r", encoding="utf-8") as f:
           # encoding 设置文件打开时指定为 utf-8 编码，避免写文件时出现编码错误
#           fileContent.SetValue(f.read())
#           file.close()
        return True
        
#    def   save(envent):
#        file = open(fileName.GetValue(), 'w')
#        file.write(fileContent.GetValue())
#        file.close()

def main():

    app = wx.App()
    ex = Example(None, title="Model_Creative_TEST")
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
