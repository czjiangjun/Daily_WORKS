import os
import shutil
import subprocess 
import linecache
import time
 
import xlwt
import pymysql

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
        E_sum = E_sum+ Ele_ene.get(i)*Ele_num.get(i)
#    print(E_sum)
    Formation = float(Etot)-E_sum
    return Formation

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

locate_path = '/media/Windows/WORKS/2021-05/pos_9_2021-11/Model-2021-11-16'

object_path = ['6-p01', '6-p02', '6-p03', '9-p01', '9-p02', '9-p03', 'orig']
#object_path = ['6-p05']

E_name = 'E_tot.txt'
E_file = open(E_name, 'w')

Fermi_name = 'E_Fermi.txt'
Fermi_file = open(Fermi_name, 'w')

j = 0
Energy = []
for i in object_path:
#    local_file = os.path.join(locate_path,i,'2-Static/POSCAR')
    local_file = os.path.join(locate_path,i,'1-Relax_Step1/POSCAR')
    Element_Numer, Element = Element_Num(local_file)

    local_file = os.path.join(locate_path,i,'2-Static/OUTCAR')
    grep_command = 'grep "sigma" ' + local_file + ' | tail -1 '
    OUTCAR_ENE = os.popen(grep_command).readlines()[0].split(' ')[-1]
    E_tot = OUTCAR_ENE.replace('\n','')
    Format_ENE = Format_Ene(Element_Numer, Element_ene, Element, OUTCAR_ENE)
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
#    if(object_path.index(i) == 0):
#           grep_command = 'grep "sigma" ' + local_file + '| tail -1 > E_tot'
#    else:
#           grep_command = 'grep "sigma" ' + local_file + '| tail -1 >> E_tot'
#    print(grep_command)
#os.system('rm -rf *.txt')
    Energy_i = []
    Energy_i.append(str(E_tot))
    Energy_i.append(str(Format_ENE))
    Energy_i.append(FERMI_ENE)
    Energy.append(Energy_i)
    j=j+1

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
    row0 = ["Alloy","E-tot (总能)","E-form (形成能)","E-fermi (Fermi能)","E-struct (结构能)"]
    colum0 = object_path
#   设置单元格宽度，sheet.col(0).width = 256 * num，设置第一列的宽度，num为字符的个数，256为单个字符的宽度
    sheet.col(0).width = 88*88
#    sheet.row(0).width = 33*33


    #写第一行
    for i in range(0,len(row0)):
	    sheet.write(0,i,row0[i],set_style('Times New Roman',320,True))

    for i in range(0,len(colum0)):
	    sheet.write(i+1,0,colum0[i],set_style('Times New Roman',220,True))

    i = 1  #保存当前列
    for d in data: #取出data中的每一个元组存到表格的每一行
        for index in range(len(d)):   #将每一个元组中的每一个单元存到每一列
#            设置单元格宽度，sheet.col(0).width = 256 * num，设置第一列的宽度，num为字符的个数，256为单个字符的宽度
             sheet.col(i).width = 256*88
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
             sheet.write(i,index+1,d[index],set_style('Times New Roman',320,True))
        i += 1

# 合并单元格，合并第2行到第4行的第4列到第5列
#    sheet.write_merge(2, 4, 4, 5, u'合并')

    book.save(filename) #保存excel

write_excel('Energy_test.xls', Energy)

end_time = time.time()
print(end_time-start_time,'秒')
#    path2 = "C:\\Program Files\\MATLAB\\R2014b\\toolbox\\gatbx\\Test_fns\\" 
#   rename_func(path2)