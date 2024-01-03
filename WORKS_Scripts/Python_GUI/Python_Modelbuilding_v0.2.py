#!/usr/bin/env ~/.local/bin/python3

"""
ZetCode wxPython tutorial

In this example we create a new class layout
with wx.GridBagSizer.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import os
import subprocess
import shutil

import time
 
import wx
import wx.lib.scrolledpanel as scrolled
#import MgO_Bandstructure

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.panel = None
        self.panel1 = None
        self.panel2 = None
        self.InitUI()
        self.Centre()

    def InitUI(self):

        def FigSize(pic, width,hight):
#            p = wx.Image(pic, wx.BITMAP_TYPE_PNG).ConvertToBitmap()  # import Fig
#            p = wx.Image(pic).ConvertToBitmap()  # import Fig
#            img = p.ConvertToImage()
#            bmg = img.Scale(width, hight)

            bmg = wx.Image(pic).Scale(width, hight)  # import Fig
            return wx.Bitmap(bmg)

        panel = wx.Panel(self)
        self.panel = panel

        sizer = wx.GridBagSizer(5, 5)
        self.sizer = sizer

#        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('/home/jun_jiang/Documents/Latex_art_beamer/Presentation_Beamer/Figures/BCC_logo-2.jpg'))
#        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('/home/jun-jiang/Documents/Latex_Beamer/Figures/BCC_logo-2.jpg'))
#        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('/home/jun-jiang/Downloads/791763113.jpg').ConvertToImage().Scale(200,200))
#        icon = wx.StaticBitmap(panel, wx.ID_ANY, FigSize('/home/jiangjun/Documents/Latex_Beamer/Figures/Logo_BCC-BCU.png', 410, 200))
        icon = wx.StaticBitmap(panel, wx.ID_ANY, FigSize('/home/jun-jiang/Documents/Latex_Beamer/Figures/Logo_BCC-BCU.png', 410, 200))
        sizer.Add(icon, pos=(1, 2), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,
            border=1)

        text1 = wx.StaticText(panel, label="Model_From_File")
        sizer.Add(text1, pos=(2, 0), flag=wx.TOP|wx.LEFT, border=10)

        combo = wx.ComboBox(panel)
        self.combo = combo
        sizer.Add(combo, pos=(2, 1), span=(1, 3),
            flag=wx.TOP|wx.EXPAND, border=5)
        self.list_path = []

        button1 = wx.Button(panel, label="Browse...")
        sizer.Add(button1, pos=(2, 4), flag=wx.TOP|wx.RIGHT, border=5)

        self.Fileload = False
        self.Bind(wx.EVT_BUTTON, self.load, button1)
#        print(self.load)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(3, 0), span=(1, 5),
            flag=wx.EXPAND|wx.BOTTOM, border=10)

        self.type_num = wx.StaticText(panel, label="Types_of_Elements = ")
        sizer.Add(self.type_num, pos=(5, 0), flag=wx.LEFT, border=10)

        list = [str(i+1) for i in range(10)]
#        print(list)
        self.ch = wx.ComboBox(panel, value ='1', choices= list, style=wx.CB_SIMPLE, name = "Num_of_Ele")
        sizer.Add(self.ch, pos=(5,2) , span=(1,1), flag=wx.TOP|wx.RIGHT)

        button_Genatom = wx.Button(panel, label='Model_Building')
        sizer.Add(button_Genatom, pos=(5, 3), flag=wx.LEFT, border=10)
        self.button_Genatom = button_Genatom

        self.Bind(wx.EVT_BUTTON, self.Get_atoms_num, button_Genatom)

        button2 = wx.Button(panel, label='Help')
        sizer.Add(button2, pos=(7, 0), flag=wx.LEFT, border=10)

        button3 = wx.Button(panel, label="Ok")
        sizer.Add(button3, pos=(7, 3))

        button4 = wx.Button(panel, label="Cancel")
        sizer.Add(button4, pos=(7, 4), span=(1, 1),
                flag=wx.BOTTOM|wx.RIGHT, border=10)

        sizer.AddGrowableCol(2)

        panel.SetSizer(sizer)
        sizer.Fit(self)
        
        self.Bind(wx.EVT_BUTTON, self.printout, button3)
        self.Bind(wx.EVT_BUTTON, self.clear, button4)
        return

    def Get_atoms_num(self, event):

        self.Fileload = False
        self.Centre()

#        self.panel.Hide()

        panel1 = wx.Panel(self)
        self.panel1 = panel1

        sizer1 = wx.GridBagSizer(5, 5)
#        sizer2 = wx.GridSizer(rows=4, cols=4, vgap=5, hgap=5) 
        self.sizer1 = sizer1


        type_nums = int(self.ch.GetValue())

        self.text2 = wx.StaticText(panel1, label="Model_Creative")
        sizer1.Add(self.text2, pos=(1, 2), flag=wx.TOP|wx.CENTER|wx.BOTTOM,
            border=15)

#        print(type_nums)
        self.types = type_nums

        self.ele_i = []
        self.num_i = []
        for i in range(type_nums):
            self.ele_i.append('')
            self.num_i.append(0)

        for i in range(type_nums):
            text3 = wx.StaticText(panel1, label="Element : ")
            sizer1.Add(text3, pos=(3+i, 0), flag=wx.LEFT|wx.BOTTOM, border=10)
 
            Element_Name = wx.TextCtrl(panel1)
#            sizer.Add(Element_Name, pos=(5, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)
            sizer1.Add(Element_Name, pos=(3+i, 1), span=(1, 1), flag=wx.TOP|wx.EXPAND, border=10)

            text4 = wx.StaticText(panel1, label="Number =")
            sizer1.Add(text4, pos=(3+i, 3), flag=wx.RIGHT|wx.BOTTOM, border=10)
 
            Element_Number = wx.TextCtrl(panel1)
#            sizer.Add(Element_Name, pos=(5, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)
            sizer1.Add(Element_Number, pos=(3+i, 4), span=(1, 1), flag=wx.EXPAND|wx.RIGHT, border=10)

            self.ele_i[i] = Element_Name
            self.num_i[i] = Element_Number
            

        sb = wx.StaticBox(panel1, label="Optional Attributes")

#        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
        self.cellgen = wx.CheckBox(panel1, label="Cell_Model")
        self.cb2 = boxsizer.Add(self.cellgen,
            flag=wx.LEFT, border=5)
        self.dyn_sel = wx.CheckBox(panel1, label="Dynamic Select")
        self.sd = boxsizer.Add(self.dyn_sel,
            flag=wx.LEFT|wx.TOP, border=5)
#        boxsizer.Add(wx.CheckBox(panel, label="Surface_Model"),
#            flag=wx.LEFT|wx.BOTTOM, border=5)
        sizer1.Add(boxsizer, pos=(i+4, 0), span=(1, 5),
            flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)
        self.boxsizer = boxsizer

        self.checkcell = False
        self.checkdyn  = False
        self.prime_cell = []
        self.Bind(wx.EVT_CHECKBOX, self.setcell)

        self.addatom_pos = []

        button_POSCAR = wx.Button(panel1, label='Gen_Post')
        sizer1.Add(button_POSCAR, pos=(i+6, 3), flag=wx.LEFT, border=10)
        self.button_POSCA = button_POSCAR

        self.panel.Destroy()
        sizer1.AddGrowableCol(2)

        panel1.SetSizer(sizer1)
        sizer1.Fit(self)
        
#        print('TEST1')
#        self.Bind(wx.EVT_BUTTON, self.Get_atoms_num, button_Genatom)
        self.Bind(wx.EVT_BUTTON, self.setposition_atoms, button_POSCAR)
        return

    def printout(self, event):

        if self.Fileload:
           print(self.file)
        else:

#           print(self.Model_Name)

           atom_positions = []
           atom_positions_all = []
           k = int(self.addatom)

           for i in range(k):

                if (not self.checkdyn):
                    pos_ix = float(self.addatom_pos[3*i+0].GetValue())
                    pos_iy = float(self.addatom_pos[3*i+1].GetValue())
                    pos_iz = float(self.addatom_pos[3*i+2].GetValue())
                    pos = (pos_ix, pos_iy, pos_iz)
                    atom_positions.append(pos)

                else:
                    pos_ix = float(self.addatom_pos[6*i+0].GetValue())
                    pos_iy = float(self.addatom_pos[6*i+1].GetValue())
                    pos_iz = float(self.addatom_pos[6*i+2].GetValue())
                    pos = (pos_ix, pos_iy, pos_iz)
#                    print(i,self.addatom_pos[6*i+3].GetValue(),self.addatom_pos[6*i+4].GetValue(),self.addatom_pos[6*i+5].GetValue())
                    if (self.addatom_pos[6*i+3].GetValue()):
                        check_x = 'T'
                    else:
                        check_x = 'F'
                    if (self.addatom_pos[6*i+4].GetValue()):
                        check_y = 'T'
                    else:
                        check_y = 'F'
                    if (self.addatom_pos[6*i+5].GetValue()):
                        check_z = 'T'
                    else:
                        check_z = 'F'

                    pos_dyn = (check_x, check_y, check_z)
                    pos_info = pos + pos_dyn
                    atom_positions_all.append(pos_info)

           if (not self.checkdyn):
               self.atom_positions = atom_positions
           else:
               self.atom_positions = atom_positions_all

#           print(self.prime_cell,)
           if (self.celladd):
#               param_x = float(self.param_x.GetValue())
#               param_y = float(self.param_y.GetValue())
#               param_z = float(self.param_z.GetValue())
#               self.param = (param_x, param_y, param_z)
               param = float(self.param.GetValue())
               self.parameter = (param)

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

#               print (self.elements, self.numbers)
#               print(self.prime_cell)

#       self.save_POSCAR()
        self.save_ATOMATE2()
        return True

    def clear(self,event):
        exit()


    def setposition_atoms(self, event):

        self.Fileload = False
        self.Centre()

#        self.panel.Hide()
#        self.panel.Hide()
#        self.scroller = wx.ScrolledWindow(self, -1)
#        self.scroller.SetScrollbars(0, 1, 0, 1200, noRefresh=False)
#        self.scroller.SetScrollRate(0, 10)
#        self.pnl = pnl = wx.Panel(self.scroller)
        panel2 = scrolled.ScrolledPanel(self, wx.ID_ANY, size=((400, 300)), style=wx.SUNKEN_BORDER)
        panel2.SetupScrolling()


#        panel2 = wx.Panel(self)
        self.panel2 = panel2

        sizer2 = wx.GridBagSizer(5, 5)
#        sizer2 = wx.GridSizer(rows=4, cols=4, vgap=5, hgap=5) 
        self.sizer2 = sizer2

        self.elements = []
        self.numbers = []
        self.Model_Name = ''
        elements_list = []
        for i in range(self.types):
            self.elements.append(self.ele_i[i].GetValue())
            self.numbers.append(abs(int(self.num_i[i].GetValue())))
            if (abs(int(self.num_i[i].GetValue())) == 1):
                self.Model_Name = self.Model_Name+self.ele_i[i].GetValue()
            elif (abs(int(self.num_i[i].GetValue())) == 0):
                self.Model_Name = self.Model_Name
            else:
                self.Model_Name = self.Model_Name+self.ele_i[i].GetValue()+str(abs(int(self.num_i[i].GetValue())))
            for j in range(abs(int(self.num_i[i].GetValue()))):
                elements_list.append(self.ele_i[i].GetValue())

        self.tot_num = sum(self.numbers)

#        self.text3 = wx.StaticText(panel2, label="Elements")
#        sizer2.Add(self.text3, pos=(1, 0), flag=wx.LEFT|wx.BOTTOM, border=10)
 
#        self.Model_Name = wx.TextCtrl(panel2)
#        sizer.Add(Model_Name, pos=(5, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)
#        sizer2.Add(self.Model_Name, pos=(1, 1), span=(1, 1), flag=wx.TOP|wx.EXPAND)

        k = self.tot_num
#        print(k)
        self.addatom = k
#        if (not self.addatom):
        for i in range(k):
               self.addatom_pos.append(0)
               self.addatom_pos.append(0)
               self.addatom_pos.append(0)
               if (self.checkdyn):
                  self.addatom_pos.append('')
                  self.addatom_pos.append('')
                  self.addatom_pos.append('')
               j = i

               pos_vector = wx.StaticText(panel2, label="Atom_%d ( %s ) position:"%((i+1), elements_list[i]))
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

               if (not self.checkdyn):
                  self.addatom_pos[3*i+0] = pos_x
                  self.addatom_pos[3*i+1] = pos_y
                  self.addatom_pos[3*i+2] = pos_z

#                  self.dyn_xbool = 'F'
#                  self.dyn_ybool = 'F'
#                  self.dyn_zbool = 'F'
               else:
                  self.addatom_pos[6*i+0] = pos_x
                  self.addatom_pos[6*i+1] = pos_y
                  self.addatom_pos[6*i+2] = pos_z

                  sc = wx.StaticBox(panel2, label="Optional Choice")
                  checkboxsizer = wx.StaticBoxSizer(sc, wx.HORIZONTAL)
                  self.dyn_x = wx.CheckBox(panel2, label="Dynamic_x")
                  self.check_x = checkboxsizer.Add(self.dyn_x, flag=wx.LEFT, border=5)

                  self.dyn_y = wx.CheckBox(panel2, label="Dynamic_y")
                  self.check_y = checkboxsizer.Add(self.dyn_y, flag=wx.LEFT, border=5)

                  self.dyn_z = wx.CheckBox(panel2, label="Dynamic_z")
                  self.check_z = checkboxsizer.Add(self.dyn_z, flag=wx.LEFT, border=5)

                  sizer2.Add(checkboxsizer, pos=(j+1, 4), span=(1, 5),
                         flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)
                  self.checkboxsizer = checkboxsizer

                  self.addatom_pos[6*i+3] = self.dyn_x
                  self.addatom_pos[6*i+4] = self.dyn_y
                  self.addatom_pos[6*i+5] = self.dyn_z

                  self.Bind(wx.EVT_CHECKBOX, self.check_celldyn)


#           panel2.Refresh()
        if ( self.checkcell):
           self.celladd = self.checkcell
           line = wx.StaticLine(panel2)
           sizer2.Add(line, pos=(j+2, 0), span=(1, 10),
                      flag=wx.EXPAND|wx.BOTTOM, border=10)


           text_Cell = wx.StaticText(self.panel2, label="Cell_parameter:")
           self.sizer2.Add(text_Cell, pos=(j+3, 0), flag=wx.LEFT|wx.TOP, border=10)
           self.text = text_Cell

           self.param = wx.TextCtrl(self.panel2)
           self.sizer2.Add(self.param, pos=(j+3, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
                border=8)
#           self.sizer2.Add(self.param_x, pos=(j+3, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
#                border=8)
#           self.param_y = wx.TextCtrl(self.panel2)
#           self.sizer2.Add(self.param_y, pos=(j+3, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
#                border=8)
#           self.param_z = wx.TextCtrl(self.panel2)
#           self.sizer2.Add(self.param_z, pos=(j+3, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
#                border=8)

           text_x_vector = wx.StaticText(self.panel2, label=" x_vector:")
           self.sizer2.Add(text_x_vector, pos=(j+4, 0), flag=wx.LEFT|wx.TOP, border=5)
           self.x_vector = text_x_vector 

           self.tc_xx = wx.TextCtrl(self.panel2)
           self.sizer2.Add(self.tc_xx, pos=(j+4, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
                border=8)
           self.tc_xy = wx.TextCtrl(self.panel2)
           self.sizer2.Add(self.tc_xy, pos=(j+4, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
                border=8)
           self.tc_xz = wx.TextCtrl(self.panel2)
           self.sizer2.Add(self.tc_xz, pos=(j+4, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
                border=8)

           text_y_vector = wx.StaticText(self.panel2, label=" y_vector:")
           self.sizer2.Add(text_y_vector, pos=(j+5, 0), flag=wx.LEFT|wx.TOP, border=5)
           self.y_vector = text_y_vector 

           self.tc_yx = wx.TextCtrl(self.panel2)
           self.sizer2.Add(self.tc_yx, pos=(j+5, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
                border=8)
           self.tc_yy = wx.TextCtrl(self.panel2)
           self.sizer2.Add(self.tc_yy, pos=(j+5, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
                border=8)
           self.tc_yz = wx.TextCtrl(self.panel2)
           self.sizer2.Add(self.tc_yz, pos=(j+5, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
                border=8)

           text_z_vector = wx.StaticText(self.panel2, label=" z_vector:")
           self.sizer2.Add(text_z_vector, pos=(j+6, 0), flag=wx.LEFT|wx.TOP, border=5)
           self.z_vector = text_z_vector 

           self.tc_zx = wx.TextCtrl(self.panel2)
           self.sizer2.Add(self.tc_zx, pos=(j+6, 1), span=(1, 1), flag=wx.TOP|wx.LEFT,
                border=8)
           self.tc_zy = wx.TextCtrl(self.panel2)
           self.sizer2.Add(self.tc_zy, pos=(j+6, 2), span=(1, 1), flag=wx.TOP|wx.ALIGN_CENTER,
                border=8)
           self.tc_zz = wx.TextCtrl(self.panel2)
           self.sizer2.Add(self.tc_zz, pos=(j+6, 3), span=(1, 1), flag=wx.TOP|wx.RIGHT,
                border=8)

        else:
           self.celladd = False
           pass

        button5 = wx.Button(panel2, label='Help')
        sizer2.Add(button5, pos=(j+8, 0), flag=wx.LEFT, border=10)

        button6 = wx.Button(panel2, label="Ok")
        sizer2.Add(button6, pos=(j+8, 3))

        button7 = wx.Button(panel2, label="Cancel")
        sizer2.Add(button7, pos=(j+8, 4), span=(1, 1),
                flag=wx.BOTTOM|wx.RIGHT, border=10)

        self.panel1.Destroy()
        sizer2.AddGrowableCol(2)

        panel2.SetSizer(sizer2)
        sizer2.Fit(self)
        
#        print('TEST2')
        self.Bind(wx.EVT_BUTTON, self.printout, button6)
#        self.Bind(wx.EVT_BUTTON, self.clear, button7)
#        time.sleep(5)
#        exit()

        return 

    def setcell(self, event):

       if (self.cellgen.GetValue()):
           self.checkcell = True
       else:
           self.checkcell = False

       if (self.dyn_sel.GetValue()):
           self.checkdyn = True
       else:
           self.checkdyn = False
#        panel = wx.Panel(self)

    def check_celldyn(self, event):
        pass
#        if (self.dyn_x.GetValue()):
#            self.dyn_xbool = 'T'
#        else:
#            self.dyn_xbool = 'F'
#
#        if (self.dyn_y.GetValue()):
#            self.dyn_ybool = 'T'
#        else: 
#            self.dyn_ybool = 'F'
#
#        if (self.dyn_z.GetValue()):
#            self.dyn_zbool = 'T'
#        else:
#            self.dyn_zbool = 'F'

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

        self.type_num.Hide()
#        self.text3.Hide()
#        self.Model_Name.Hide()
        self.ch.Hide()
#        self.text_num.Hide()
        self.button_Genatom.Hide()
#        self.cellgen.Hide()
        
        return True
        
    def save_POSCAR(self):

        file = open('POSCAR', 'w')
        Model_Name = self.Model_Name+"\n"
        file.writelines(Model_Name)

#        parameter_i = ''
#        for i in self.param:
#            parameter_i = parameter_i + str(i) + ' '
#        file.writelines(parameter_i + '\n')
        parameter = str(self.parameter)
        file.writelines(parameter + '\n')

        for i in range(3):
            prime_cell_i = ''
            for j in self.prime_cell[i]:
                prime_cell_i = prime_cell_i + str(j) + '  '
            file.writelines(prime_cell_i+'\n')
                       
        element_i = ''
        for i in self.elements:
            element_i = element_i + i + ' '
        file.writelines(element_i + '\n')
        number_i = ''
        for i in self.numbers:
            number_i = number_i +str(i) + ' '
        file.write(number_i+ '\n')
        if (self.checkdyn):
            file.writelines('Selective dynamics\n')
        file.writelines('Cartesian\n')
        for i in range(self.tot_num):
            position_i = ''
            for j in self.atom_positions[i]:
                position_i = position_i + str(j) + ' '
            file.write(position_i+'\n')
        file.close()
        return


    def save_ATOMATE2(self):

#        Model_Name = self.Model_Name+"-ATOMATE2_Relax2.py"
        Model_Name = "ATOMATE2_Relax2.py"

        file = open(Model_Name, 'w')

        import_module="from atomate2.vasp.flows.core import RelaxBandStructureMaker\nfrom jobflow import run_locally \nfrom pymatgen.core import Structure \n\n# construct a Model structure "

        Model_structure=self.Model_Name+"_structure"+"=Structure("
#        print(Model_structure)

        lattice ="     lattice=["#+self.prime_cell[1]+"],["+self.prime_cell[2]+"],["+self.prime_cell[3]+"]]"
        for i in range(3):
#            prime_cell_i = ''

            lattice=lattice +"["
            k = 0
            for j in self.prime_cell[i]:
                k = k+1
#                prime_cell_i = prime_cell_i + str(j) + '  '
                lattice=lattice + str(j)
                if k < len(self.prime_cell[i]):
                    lattice=lattice+", "
#            file.writelines(prime_cell_i+'\n')
            if i<2:
                lattice=lattice+"], "
            else:
                lattice=lattice+"]"
        lattice=lattice+"],"
#        print(lattice)

        elements ="     species=[" 
        k=0
        for i in self.elements:
            k=k+1
            if k<len(self.elements):
                elements = elements + '"'+i + '", '
            else:
                elements = elements + '"'+i +'"'
        elements=elements+"],"
#        print(elements)

        positions ="     coords=["
        for i in range(self.tot_num):

            positions = positions+"["
            k = 0
#            position_i = ''

            for j in self.atom_positions[i]:
                k = k+1
                positions=positions+str(j)
                if k< len(self.atom_positions[i]):
                    positions=positions+", "
#                position_i = position_i + str(j) + ' '
            if i< self.tot_num-1:
                positions=positions+"], "
            else:
                positions=positions+"]"

        positions=positions+"],"
#        print(positions)

        run_command=")\n\n# make a band structure flow to optimise the structure and obtain the band structure\nbandstructure_flow = RelaxBandStructureMaker().make("+self.Model_Name+"_structure)\n\n# run the job\nrun_locally(bandstructure_flow, create_folders=True) "

        file.writelines(import_module + '\n')

        file.writelines(Model_structure+'\n')

        file.writelines(lattice+'\n')
        file.writelines(elements+'\n')
        file.write(positions+'\n')

        file.writelines(run_command + '\n')

#        parameter_i = ''
#        for i in self.param:
#            parameter_i = parameter_i + str(i) + ' '
#        file.writelines(parameter_i + '\n')
#        parameter = str(self.param)
#        file.writelines(parameter + '\n')
#
#        for i in range(3):
#            prime_cell_i = ''
#            for j in self.prime_cell[i]:
#                prime_cell_i = prime_cell_i + str(j) + '  '
#            file.writelines(prime_cell_i+'\n')
#                       
#        element_i = ''
#        for i in self.elements:
#            element_i = element_i + i + ' '
#        file.writelines(element_i + '\n')
#        number_i = ''
#        for i in self.numbers:
#            number_i = number_i +str(i) + ' '
#        file.write(number_i+ '\n')
#        if (self.checkdyn):
#            file.writelines('Selective dynamics\n')
#        file.writelines('Cartesian\n')

#        for i in range(self.tot_num):
#            position_i = ''
#            for j in self.atom_positions[i]:
#                position_i = position_i + str(j) + ' '
#            file.write(position_i+'\n')
        file.close()
        self.Close()
        shutil.copy(Model_Name, self.Model_Name+"_Atomate2.py")
#        exit()
        return
#



class App(wx.App):
#    def __init__(self):
#        wx.App.__init__(self)

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
    time.sleep(5)
#    execu_file = self.Model_Name+"-ATOMATE2_Relax2"
    execu_file = "ATOMATE2_Relax2.py"
#        subprocess.call(["python3", execu_file])
    os.system("python3 "+execu_file)
    time.sleep(10)
    os.remove(execu_file)
#    MgO_Bandstructure.main()

if __name__ == '__main__':
    main()
