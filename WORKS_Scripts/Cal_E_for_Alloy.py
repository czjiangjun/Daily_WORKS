import os
import shutil
import subprocess 
import linecache
import time
 
import xlwt
import xlrd
import pymysql

import matplotlib.pyplot as plt   # 导入模块 matplotlib.pyplot，并简写成 plt
import numpy as np                # 导入模块 numpy，并简写成 np

start_time = time.time()
# 需要被复制的文件夹
 
#old_path = r'D:\zjf_workspace\001-地标、利器、服饰\004文本\json1'
#new_path = r'D:\zjf_workspace\001-地标、利器、服饰\004文本\json'

#all_list = os.listdir(old_path)
#for i in all_list:
# print(i)
# name, suffix = i.rsplit('.txt')
# name = name.replace('.','')
# old_name = old_path + '/' + i
# new_name = new_path + '/' + name + ".json"
# shutil.copyfile(old_name, new_name)
 
#print(len(all_list))
#print(all_list)



#current_path = os.getcwd()
#print(current_path)

#project_name = 'project'

#current_path = current_path[:current_path.find(project_name) + len(project_name)]


#os.chdir(current_path)

#print(os.getcwd())

#val = os.system('ls -al')
#print val

def Element_Num(file_name):
#    POS_file = open(file_name, 'r')
    Element_num = {}
    line_Element = os.popen('sed -n {}p {}'.format(6, file_name)).read().replace('\n', '')
#    line_Element = linecache.getline(file_name,6)
    Element = line_Element.strip().split(' ')
    for i in Element:
        if i =='':
            Element.remove(i)
    line_num = os.popen('sed -n {}p {}'.format(7, file_name)).read().replace('\n', '')
#    line_num = linecache.getline(file_name,7)
    Num = line_num.strip().split(' ')
    j = 0
    for i in Num:
        if i =='':
            Num.remove(i)
#        print(Element[j],Num[j])
        Element_num.update({Element[j]:int(Num[j])})
        j = j+1
#    print(Element_num)
    return Element_num, Element

def Format_Ene(Ele_num,Ele_ene,Ele, Etot):
    E_sum = 0.0
    for i in Ele:
#        print(i)
#        print( Ele_ene.get(i))
#        print( Ele_num.get(i))
        E_sum = E_sum + Ele_ene.get(i)*Ele_num.get(i)
#    print(E_sum)
    Formation = round(float(Etot)-E_sum,4)
    return Formation

def Bond_Ene(Ele_num,Ele_ene,Ele, E_alloy, E_orig):
    E_delt =  E_alloy - E_orig 
    sum_orig = 0.0
    sum_elem = 0.0
    Ni_Num_orig = 336
    Al_Num_orig = 56
    for i in Ele:
        if (i == 'Ni'):
            sum_orig = sum_orig + Ni_Num_orig*Ele_ene.get(i)
        if (i == 'Al'):
            sum_orig = sum_orig + Al_Num_orig*Ele_ene.get(i)
#        print(i)
        sum_elem = sum_elem + Ele_ene.get(i)*Ele_num.get(i)
    delt_E = E_delt - (sum_elem - sum_orig)
#    print(E_sum)
    BondEne = round(float(delt_E),4)
    return BondEne

def Bind_Ene(local_path, Binding_Info, Alloy, E_alloy):
    Binding_File = os.path.join(local_path, Binding_Info)
#    print(Binding_File)
#    file = open(Binding_File, encoding = 'utf-8')

    readline = linecache.getline(Binding_File,3).replace('\n', '').strip(' ').split('=')
    readline = [j for j in readline if j !='']
    Binding = readline[1].strip(' ')
 #   print(Binding)
    readline = linecache.getline(Binding_File,4).replace('\n', '').strip(' ').split(' ')
    Alloy_elem_num = int(readline[0])

    Position = {}
    for i in range(Alloy_elem_num):
        position_i = []
        readline = linecache.getline(Binding_File,i+5).replace('\n', '').strip(' ').split(':')
        readline = [j for j in readline if j !='']
        text = readline[1].strip(' ').split(',')
        position_i = [int(j) for j in text if j !='']
        xx = {readline[0].strip(' '):len(position_i)}
        Position.update(xx)
#    print(Alloy_orig)
#    print(Position)
#    exit(0)
#    current_path = os.path.join(local_path,Binding)
    E_bind = {}
    list_atom = list(Position.keys())
    list_atom_ENE = list(Position.values())
    E_atom_Binding = 'E_atom_Binding'+'_'+Alloy+'.txt'

    Binding_name = os.path.join(local_path, Binding, E_atom_Binding)
    Binding_atom_file = open(Binding_name, 'w')

    for i in list_atom:
        Atom_i = 'Atom_' + i +'/OUTCAR'
        Binding_atom = os.path.join(local_path, Binding, Atom_i)
        grep_command = 'grep "sigma" ' + Binding_atom + ' | tail -1 '
        OUTCAR_ENE = os.popen(grep_command).readlines()[0].split(' ')[-1]
        E_atom_replace = float(OUTCAR_ENE.replace('\n',''))
        E_atom_bing = (E_alloy - E_atom_replace)/int(Position[i])
        xx = {i:E_atom_bing}
        E_bind.update(xx)
#    print (E_bind)
        yy = i + '  :  ' + str(E_atom_bing) +'   eV'+'\n'
        Binding_atom_file.write(yy)
    Binding_atom_file.close()
    return # E_bind

def DOS_Data_get(DOS_file):
    file = open(DOS_file, 'r')
    line = file.readline()
    count = 0
    Num_step = 0
    DOS_tot_Energ = []
    DOS_tot_Data = []
    DOS_atom = []
    Num_atom = line.replace('\n', '').strip(' ').split(' ')[0]

#    print(Num_atom)
    for count in range(4):
        line = file.readline()
        if (count == 3):
            DOS_INFO = file.readline().replace('\n', '').strip(' ').split(' ')
            DOS_INFO = [i for i in DOS_INFO if i !='']
#            print(DOS_INFO)
            Num_step = int(DOS_INFO[2])
#    exit(0)    
    for count in range(Num_step):
            DOS_Data = file.readline().replace('\n', '').strip(' ').split(' ')
            DOS_Data = [i for i in DOS_Data if i !='']
#            print(DOS_Data)
            DOS_tot_Energ.append(float(DOS_Data[0]))
            DOS_tot_Data.append(float(DOS_Data[1]))
#    print(DOS_tot_Energ)
#    exit(0)    
    for i in range(int(Num_atom)): 
        file.readline().replace('\n', '').strip(' ').split(' ')
        DOS_atom.append([])
#        print(i)
        for count in range(Num_step):
            DOS_atom[i].append([])
            DOS_Data = file.readline().replace('\n', '').strip(' ').split(' ')
            DOS_Data = [k for k in DOS_Data if k !='']
            for k in DOS_Data[1:]:
                DOS_atom[i][count].append(float(k))
#        print(DOS_atom)
#            break
#        exit(0)    

#        line = file.readline()
    DOS_atom_Data = np.array(DOS_atom)
    return int(Num_atom), Num_step, DOS_tot_Energ, DOS_tot_Data, DOS_atom_Data

def Figure_DOS_product(x_data, y_data, label_ind, Fig_title):
#    plt.clf()  #clean figure 防止图片重叠
    plt.axis([-7.65,9.45, 0, 1500.0])
    plt.xlabel("Energy/ eV")
    plt.ylabel("DOS")

#    Fig_title = "Denesity_of_State_For_"+i
    plt.title(Fig_title)

    plt.plot(x_data, y_data, label = label_ind)
    plt.legend(loc='best') 

#    plt.savefig(Fig_save)
#    exit(0)
    return

#def objFileName():
#    fileNameList = r"D:\test\list.txt"
#    objNameList = []
#    for i in open(fileNameList, 'r'):
#        objNameList.append(i.replace('\n', ''))
#    return objNameList
# 
#def copyImg():
#    sourcePath = r'D:\test\A'
#    # 指定图片原始路径A
#    targetPath = r'D:\test\B'
#    # 指定图片存放目录B
#    for i in objFileName():
#        objName = i
#        shutil.copy(sourcePath + '/' + objName, targetPath + '/' + objName)
# 
#
#
#def rename_func(path):
#    for file in os.listdir(path):
#        fileNew = file.lower()
#        print("Old:", file, "New", fileNew)
#        if(fileNew != file):
#            os.rename(path + file, path + fileNew)
#
#
#if __name__ == '__main__':
#    copyImg()
# exe_file = '/home/jun_jiang/Softs/Scrips/Structure_Energy'
Element_ene = {'Ni': -5.5089028, 'Al': -3.7382060, 'Ta': -11.8587815, 'Cr': -9.5176370, 'Co': -7.1044055, 'Re': -12.3929130, 'Mo': -10.9439630, 'Ru': -9.2073525, 'W': -13.0068755}

# locate_path = '/media/Windows/WORKS/2021-05/pos_9yuan/2021-07-27'
# locate_path = '/media/Windows/WORKS/2021-05/pos_9_2021-11/Model-2021-11-16'
locate_path = '/media/Windows/WORKS/2021-05/pos_9_2021-11/Model-2021-12-02'
local_path = '/media/Windows/WORKS/2021-05/pos_9_2021-11'

# object_path = ['orig', '6-p05', '6-p12', '6-p18', '9-p05', '9-p10', '9-p11', '9-p12', '9-p13', '9-p18']
object_path = ['orig', '9-p08', '9-p15', '9-p16', '9-p17', '9-p18','9-p21', '9-p22']
lorbital = ['s', 'p_x', 'p_y', 'p_z', 'd_z^2', 'd_xy', 'd_x^2-y^2', 'd_xz', 'd_yz']
#object_path = ['6-p05']

E_name = 'E_tot.txt'
E_file = open(E_name, 'w')

Fermi_name = 'E_Fermi.txt'
Fermi_file = open(Fermi_name, 'w')

# j = 0
Energy = []
E_orig = []
for i in object_path:
#    local_file = os.path.join(locate_path,i,'2-Static/POSCAR')
    local_file = os.path.join(locate_path,i,'1-Relax_Step1/POSCAR')
    Element_Numer, Element = Element_Num(local_file)

    local_file = os.path.join(locate_path,i,'2-Static/OUTCAR')
    grep_command = 'grep "sigma" ' + local_file + ' | tail -1 '
    OUTCAR_ENE = os.popen(grep_command).readlines()[0].split(' ')[-1]
    E_tot = OUTCAR_ENE.replace('\n','')

# make data
    local_DOS_file = os.path.join(locate_path,i,'2-Static/DOSCAR')
    Num_atom, DOS_step, DOS_energy, DOS_tot, DOS_atom_data = DOS_Data_get(local_DOS_file)
    local_DOS_fig = os.path.join(locate_path,i,'2-Static/DOS_Fig.pdf')
#    print(DOS_energy)
#    print(DOS)


    plt.clf()  #clean figure 防止图片重叠
#    plt.axis([-7.65,9.45, 0, 1500.0])
#    plt.xlabel("Energy/ eV")
#    plt.ylabel("DOS")
#
    DOS_title = "Denesity_of_State_For_"+i
#    plt.title(DOS_title)

    label_ind = 'TOT_DOS'
    Figure_DOS_product(DOS_energy, DOS_tot, 'TOT_DOS', DOS_title)
#    plt.plot(DOS_energy, DOS_tot, label = 'Tot_DOS')
#    plt.legend(loc='best') 

    DOS_atom_t = np.sum(DOS_atom_data, axis = 0)
#    plt.clf()  #clean figure 防止图片重叠
    for l in range(len(lorbital)):
#        print(DOS_atom_t[:,l])
         Figure_DOS_product(DOS_energy, DOS_atom_t[:,l], lorbital[l], DOS_title)
#        plt.plot(DOS_energy, DOS_atom_t[:,l], label=i)
    plt.savefig(local_DOS_fig)
#    plt.show()

    Format_ENE = Format_Ene(Element_Numer, Element_ene, Element, OUTCAR_ENE)

    if (i == 'orig'):
        E_orig.append(E_tot)
#        FormE_orig.append(Format_ENE)
#        print(FormE_orig)
#    Bing_ENE = Bond_Ene(Element_Numer, Element_ene, Element, Format_ENE, float(FormE_orig[0]))
    Bing_ENE = Bond_Ene(Element_Numer, Element_ene, Element, float(E_tot), float(E_orig[0]))
#    print(OUTCAR_ENE)
#    exit(0)
    E_tot_Form = OUTCAR_ENE.replace('\n','') + '    '+str(Format_ENE) + '\n'
    E_file.write(E_tot_Form)

    grep_command = 'grep "E-fermi" ' + local_file + ' | tail -1 '
    FERMI_ENE = os.popen(grep_command).readlines()[0].split(':')[1].split('   ')[1]
    FERMI_mov = os.popen(grep_command).readlines()[0].split(':')[3].strip(' ')
#    print(FERMI_ENE)
#    print(FERMI_mov)
    Fermi_file.write(FERMI_ENE+'   '+FERMI_mov)
    FERMI_SHIFT = float(FERMI_ENE)+float(FERMI_mov)

    if (i != 'orig'):
        Position_binding = 'Position_binding_'+i
#        print(Position_binding)
#        exit(0)
        Bind_Ene(local_path, Position_binding, i, float(E_tot))
#    if(object_path.index(i) == 0):
#           grep_command = 'grep "sigma" ' + local_file + '| tail -1 > E_tot'
#    else:
#           grep_command = 'grep "sigma" ' + local_file + '| tail -1 >> E_tot'
#    print(grep_command)
#os.system('rm -rf *.txt')
    Energy_i = []
    Energy_i.append(E_tot)
    Energy_i.append(str(Format_ENE))
    Energy_i.append(FERMI_ENE)
    Energy_i.append(FERMI_SHIFT)
    Energy_i.append(Bing_ENE)
    Energy.append(Energy_i)
#    j=j+1

E_file.close()
Fermi_file.close()

#设置表格样式
def write_excel(filename, data):

    def set_style(name,height,bold=False):
        style = xlwt.XFStyle()

        """
           0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow,
           6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown),
           20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray
        """
# 设置背景颜色
        pattern = xlwt.Pattern()
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = 7  # 背景颜色

# 设置边框
        borders = xlwt.Borders()
        borders.left = xlwt.Borders.THIN
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN

# 设置居中（左右上下居中）
        alignment = xlwt.Alignment()
        alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平方向
        alignment.vert = xlwt.Alignment.HORZ_CENTER  # 垂直方向
# 设置单元格对齐方式
# VERT_TOP       = 0x00    上端对齐
# VERT_CENTER    = 0x01    居中对齐（垂直方向上）
# VERT_BOTTOM    = 0x02    底端对齐
# HORZ_LEFT      = 0x01    左端对齐
# HORZ_CENTER    = 0x02    居中对齐（水平方向上）
# HORZ_RIGHT     = 0x03    右端对齐
#        alignment.horz = 0x02
#        alignment.vert = 0x01
# 设置自动换行
#       alignment.wrap = 1
        style.alignment = alignment

        font = xlwt.Font()
        font.name = name
        font.bold = bold
        font.color_index = 4
        font.height = height

        style.font = font

        return style

#获取字符串长度，一个中文的长度为2

    def len_byte(value):
       length = len(value)
       utf8_length = len(value.encode('utf-8'))
       length = (utf8_length - length)/2 + length
       return int(length)


    book = xlwt.Workbook()            #创建excel对象
    sheet = book.add_sheet('Alloy_Energy')  #添加一个表Sheet
    row0 = ["Alloy","E-tot (总能)","E-form (形成能)","E-fermi (Fermi能)","E-bond (键能)","E-struct (结构能)"]
#    row0 = ["Alloy","E-tot (总能)","E-form (形成能)","E-fermi (Fermi能)/(Fermi能-shift)","E-struct (结构能)"]
    colum0 = object_path
#   设置单元格宽度，sheet.col(0).width = 256 * num，设置第一列的宽度，num为字符的个数，256为单个字符的宽度
    sheet.col(0).width = 88*88
#    sheet.row(0).width = 33*33


    #写第一行
    for i in range(0,len(row0)):
        if( i<3 ):
            sheet.write_merge(0,1,i,i,row0[i],set_style('Times New Roman',320,True))
        elif(i==3):
            sheet.write_merge(0,0,i,i+1,row0[i],set_style('Times New Roman',320,True))
            sheet.write(1,i,"orig",set_style('Times New Roman',320,True))
            sheet.write(1,i+1,"shift",set_style('Times New Roman',320,True))
        else:
            sheet.write_merge(0,1,i+1,i+1,row0[i],set_style('Times New Roman',320,True))
#    sheet.write_merge(0,0,6,8,row0[4],set_style('Times New Roman',320,True))
#    sheet.write(0,9,row0[4],set_style('Times New Roman',320,True))
    #写第一列
    for i in range(0,len(colum0)):
	    sheet.write(i+2,0,colum0[i],set_style('Times New Roman',220,True))

    i = 1  #保存当前列
    for d in data: #取出data中的每一个元组存到表格的每一行
        for index in range(len(d)):   #将每一个元组中的每一个单元存到每一列
#            设置单元格宽度，sheet.col(0).width = 256 * num，设置第一列的宽度，num为字符的个数，256为单个字符的宽度
             sheet.col(i).width = 88*88
#             col_width = []
#             for k in range(len(d)):
#                for l in range(len(d)):
#                      if k == 1:
#                          col_width.append(len_byte(d[k][l]))
#                      else:
#                         if col_width[l] < len_byte(str(d[k][l])):
#                             col_width[l] = len_byte(d[k][k])
#            设置栏位宽度，栏位宽度小于10时候采用默认宽度

#             for j in range(len(col_width)):
#                if col_width[j] > 10:
#                    worksheet.col(j).width = 256*(col_width[j] +1)
#设置栏位高度
                # tall_style = xlwt.easyxf('font:height 720;') #设置字体高度
                # row0 = worksheet.row(0)
                # row0.set_style(tall_style)
             sheet.write(i+1,index+1,d[index],set_style('Times New Roman',320,True))
        i += 1



# 合并单元格，合并第2行到第4行的第4列到第5列
#    sheet.write_merge(2, 4, 4, 5, u'合并')

    book.save(filename) #保存excel

write_excel('Energy_test.xls', Energy)

# book = xlrd.open_workbook('Energy_test.xls')            #创建excel对象
# sheet = book.sheet_by_name('Alloy_Energy')  #添加一个表Sheet
# sheet.merged_cells(0,0,4,7)



end_time = time.time()
print(end_time-start_time,'秒')
#    path2 = "C:\\Program Files\\MATLAB\\R2014b\\toolbox\\gatbx\\Test_fns\\" 
#   rename_func(path2)
