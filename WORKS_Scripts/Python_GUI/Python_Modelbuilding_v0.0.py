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

        self.panel = None
        self.panel2 = None
        self.InitUI()
        self.Centre()

    def InitUI(self):

        panel = wx.Panel(self)
        self.panel = panel

        sizer = wx.GridBagSizer(5, 5)
        self.sizer = sizer

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

        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('/home/jun_jiang/Documents/Latex_art_beamer/Presentation_Beamer/Figures/BCC_logo-2.jpg'))
        sizer.Add(icon, pos=(2, 1), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,
            border=1)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(3, 0), span=(1, 5),
            flag=wx.EXPAND|wx.BOTTOM, border=10)

        self.text2 = wx.StaticText(panel, label="Model_Creative")
        sizer.Add(self.text2, pos=(4, 1), flag=wx.TOP|wx.CENTER|wx.BOTTOM,
            border=15)

        self.text_num = wx.StaticText(panel, label="Tot_Num")
        sizer.Add(self.text_num, pos=(5, 0), flag=wx.LEFT, border=10)

        list = [str(i+1) for i in range(5)]
#        print(list)
        self.ch = wx.ComboBox(panel, value ='1', choices= list, style=wx.CB_SIMPLE, name = "Num_of_Ele")
        sizer.Add(self.ch, pos=(5,2) , span=(1,1), flag=wx.TOP|wx.RIGHT)

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
        sizer.Add(boxsizer, pos=(6, 0), span=(1, 5),
            flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)
        self.boxsizer =boxsizer

        self.checkcell = False
        self.prime_cell = []
        self.Bind(wx.EVT_CHECKBOX, self.setcell)
        button_Genatom = wx.Button(panel, label='Gen_Post')
        sizer.Add(button_Genatom, pos=(8, 0), flag=wx.LEFT, border=10)
        self.button_Genatom = button_Genatom

        self.addatom_pos = []
        self.Bind(wx.EVT_BUTTON, self.setposition_atoms, button_Genatom)

        button2 = wx.Button(panel, label='Help')
        sizer.Add(button2, pos=(10, 0), flag=wx.LEFT, border=10)

        button3 = wx.Button(panel, label="Ok")
        sizer.Add(button3, pos=(10, 3))

        button4 = wx.Button(panel, label="Cancel")
        sizer.Add(button4, pos=(10, 4), span=(1, 1),
                flag=wx.BOTTOM|wx.RIGHT, border=10)

        sizer.AddGrowableCol(2)

        panel.SetSizer(sizer)
        sizer.Fit(self)
        
        self.Bind(wx.EVT_BUTTON, self.printout, button3)
        self.Bind(wx.EVT_BUTTON, self.clear, button4)

    def printout(self, event):

        if self.Fileload:
           print(self.file)
        else:

           print(self.Element_Name.GetValue())

           atom_positions = []
           k = int(self.addatom)

           for i in range(k):

                pos_ix = float(self.addatom_pos[3*i+0].GetValue())
                pos_iy = float(self.addatom_pos[3*i+1].GetValue())
                pos_iz = float(self.addatom_pos[3*i+2].GetValue())
                pos = (pos_ix, pos_iy, pos_iz)

                atom_positions.append(pos)

           print(atom_positions)
           if (self.celladd):
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

           exit()

    def clear(self,event):
        exit()


    def setposition_atoms(self, event):

        self.Fileload = False
        self.Centre()

#        self.panel.Hide()

        panel2 = wx.Panel(self)
        self.panel2 = panel2

        sizer2 = wx.GridBagSizer(5, 5)
#        sizer2 = wx.GridSizer(rows=4, cols=4, vgap=5, hgap=5) 
        self.sizer2 = sizer2

        self.text3 = wx.StaticText(panel2, label="Elements")
        sizer2.Add(self.text3, pos=(1, 0), flag=wx.LEFT|wx.BOTTOM, border=10)
 
        self.Element_Name = wx.TextCtrl(panel2)
#        sizer.Add(Element_Name, pos=(5, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)
        sizer2.Add(self.Element_Name, pos=(1, 1), span=(1, 1), flag=wx.TOP|wx.EXPAND)

        k = int(self.ch.GetValue())
        print(k)
        self.addatom = k
#        if (not self.addatom):
        for i in range(k):
               self.addatom_pos.append (0)
               self.addatom_pos.append (0)
               self.addatom_pos.append (0)
               j = i+2

               pos_vector = wx.StaticText(panel2, label="Atom_%d_position:"%(i+1))
               sizer2.Add(pos_vector, pos=(j+1, 0), flag=wx.LEFT|wx.BOTTOM, border=5)
 
               pos_x = wx.TextCtrl(panel2)
               sizer2.Add(pos_x, pos=(j+1, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
                    border=8)
               pos_y = wx.TextCtrl(panel2)
               sizer2.Add(pos_y, pos=(j+1, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
                    border=8)
               pos_z = wx.TextCtrl(panel2)
               sizer2.Add(pos_z, pos=(j+1, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
                    border=8)
               self.addatom_pos[3*i+0] = pos_x
               self.addatom_pos[3*i+1] = pos_y
               self.addatom_pos[3*i+2] = pos_z


#           panel2.Refresh()
        if ( self.checkcell):
           self.celladd = self.checkcell

           text_Cell = wx.StaticText(self.panel2, label="Cell_parameter")
           self.sizer2.Add(text_Cell, pos=(j+2, 0), flag=wx.LEFT|wx.TOP, border=10)
           self.text = text_Cell

           text_x_vector = wx.StaticText(self.panel2, label="x_vector:")
           self.sizer2.Add(text_x_vector, pos=(j+3, 0), flag=wx.LEFT|wx.TOP, border=5)
           self.x_vector = text_x_vector 

           self.tc_xx = wx.TextCtrl(self.panel2)
           self.sizer2.Add(self.tc_xx, pos=(j+3, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
                border=8)
           self.tc_xy = wx.TextCtrl(self.panel2)
           self.sizer2.Add(self.tc_xy, pos=(j+3, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
                border=8)
           self.tc_xz = wx.TextCtrl(self.panel2)
           self.sizer2.Add(self.tc_xz, pos=(j+3, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
                border=8)

           text_y_vector = wx.StaticText(self.panel2, label="y_vector:")
           self.sizer2.Add(text_y_vector, pos=(j+4, 0), flag=wx.LEFT|wx.TOP, border=5)
           self.y_vector = text_y_vector 

           self.tc_yx = wx.TextCtrl(self.panel2)
           self.sizer2.Add(self.tc_yx, pos=(j+4, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
                border=8)
           self.tc_yy = wx.TextCtrl(self.panel2)
           self.sizer2.Add(self.tc_yy, pos=(j+4, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
                border=8)
           self.tc_yz = wx.TextCtrl(self.panel2)
           self.sizer2.Add(self.tc_yz, pos=(j+4, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
                border=8)

           text_z_vector = wx.StaticText(self.panel2, label="z_vector:")
           self.sizer2.Add(text_z_vector, pos=(j+5, 0), flag=wx.LEFT|wx.TOP, border=5)
           self.z_vector = text_z_vector 

           self.tc_zx = wx.TextCtrl(self.panel2)
           self.sizer2.Add(self.tc_zx, pos=(j+5, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
                border=8)
           self.tc_zy = wx.TextCtrl(self.panel2)
           self.sizer2.Add(self.tc_zy, pos=(j+5, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
                border=8)
           self.tc_zz = wx.TextCtrl(self.panel2)
           self.sizer2.Add(self.tc_zz, pos=(j+5, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
                border=8)

        else:
           self.celladd = False
           pass

        button5 = wx.Button(panel2, label='Help')
        sizer2.Add(button5, pos=(j+7, 0), flag=wx.LEFT, border=10)

        button6 = wx.Button(panel2, label="Ok")
        sizer2.Add(button6, pos=(j+7, 3))

        button7 = wx.Button(panel2, label="Cancel")
        sizer2.Add(button7, pos=(j+7, 4), span=(1, 1),
                flag=wx.BOTTOM|wx.RIGHT, border=10)

        self.panel.Destroy()
        sizer2.AddGrowableCol(2)

        panel2.SetSizer(sizer2)
        sizer2.Fit(self)
        
        print('TEST')
        self.Bind(wx.EVT_BUTTON, self.printout, button6)
        self.Bind(wx.EVT_BUTTON, self.clear, button7)
#        exit()

        return 

    def setcell(self, event):

       if (self.cellgen.GetValue()):
           self.checkcell = True
       else:
           self.checkcell = False

#        panel = wx.Panel(self)

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

        self.text2.Hide()
        self.text3.Hide()
        self.Element_Name.Hide()
        self.ch.Hide()
        self.text_num.Hide()
        self.button_Genatom.Hide()
        self.cellgen.Hide()
        
        return True
        
#    def   save(envent):
#        file = open(fileName.GetValue(), 'w')
#        file.write(fileContent.GetValue())
#        file.close()

class App(wx.App):
    def __init__(self):
        wx.App.__init__(self)

    def OnInit(self):
        self.frame = Example(None, title="Model_Creative_TEST")
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

def main():

    app = App()
#    ex = Example(None, title="Model_Creative_TEST")
#    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
