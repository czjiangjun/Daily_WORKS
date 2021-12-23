import os
import shutil
import tarfile
import linecache
import subprocess 
import time
import copy 

import math
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
#逐个添加文件打包，未打包空子目录。可过滤文件。
#如果只打包不压缩，将"w:gz"参数改为"w:"或"w"即可。
def Read_Position(File):
    file = open(File, encoding = 'utf-8')
    readline = linecache.getline(File,1).replace('\n', '').strip(' ').split('=')
    readline = [j for j in readline if j !='']
    Alloy_orig = readline[1].strip(' ')

    readline = linecache.getline(File,2).replace('\n', '').strip(' ').split('=')
    readline = [j for j in readline if j !='']
    Alloy = readline[1].strip(' ')

    readline = linecache.getline(File,3).replace('\n', '').strip(' ').split('=')
    readline = [j for j in readline if j !='']
    Binding = readline[1].strip(' ')

    readline = linecache.getline(File,4).replace('\n', '').strip(' ').split('=')
    readline = [j for j in readline if j !='']
    Object_Path = readline[1].strip(' ')

    readline = linecache.getline(File,5).replace('\n', '').strip(' ').split(' ')
    Alloy_elem_num = int(readline[0])

    Position = {}
    for i in range(Alloy_elem_num):
        position_i = []
        readline = linecache.getline(File,i+6).replace('\n', '').strip(' ').split(':')
        readline = [j for j in readline if j !='']
        text = readline[1].strip(' ').split(',')
        position_i = [int(j) for j in text if j !='']
        xx = {readline[0].strip(' '):position_i}
        Position.update(xx)
#    print(Alloy_orig)
#    print(Position)
#    exit(0)
    return Alloy_orig, Alloy, Binding, Object_Path, Position

def READ_POSCAR(POSCAR_File):
    Info = []
    Compound_Name = linecache.getline(POSCAR_File, 1).replace('\n', '')
#    print (Compound_Name)
    Info.append(Compound_Name)
    # READ_Scale   %line_2
    scale = linecache.getline(POSCAR_File, 2).replace('\n', '').strip(' ').split(' ')
#    print (scale)
    Info.append(float(scale[0]))
    # READ_Bravais   %line_3-5
    Bravais = []
    for i in range(3):
        Bravais_i = linecache.getline(POSCAR_File, i+3).replace('\n', '').strip(' ').split(' ')
        Bravais_i = [j for j in Bravais_i if j !='']
#        print (Bravais_i)
        for j in Bravais_i: 
            Bravais.append(float(j))

    # READ_Element_and_Num   %line_6-7
    elem_tot = 0
    elem_ind = {}
    elements_num = {}
    elements = linecache.getline(POSCAR_File, 6).replace('\n', '').strip(' ').split(' ')
    elements = [i for i in elements if i !='']
    elem_num = linecache.getline(POSCAR_File, 7).replace('\n', '').strip(' ').split(' ')
    elem_num = [i for i in elem_num if i !='']
#    print(len(elem_num))
    for i in range(len(elem_num)):
        elem_tot = elem_tot+int(elem_num[i])
        xx = {elements[i]: elem_tot}
        elem_ind.update(xx)
        yy = {elements[i]: int(elem_num[i])}
        elements_num.update(yy)
#    print(elem_tot)

    # READ_Select_and_Dynamic   %line_8-9
#    Compound_Select = ''
    Compound_Dynamics = ''
    Compound_read = linecache.getline(POSCAR_File, 8).replace('\n', '').strip(' ').split(' ')
    list = Compound_read[0]
#    print(list[0])
    if (list[0] == 'S' or list[0] == 's'):
        Compound_Select = Compound_read[0]
        Info.append(Compound_Select)
        Compound_read = linecache.getline(POSCAR_File, 9).replace('\n', '').strip(' ').split(' ')
        Compound_Dynamics = Compound_read[0]
        Info.append(Compound_Dynamics)
        linenum = 10
    else:
        Compound_Select = 'Select'
        Info.append(Compound_Select)
        Compound_Dynamics = Compound_read[0]
        Info.append(Compound_Dynamics)
        linenum = 9

    # READ_Position   %line_10
    position = {}
    k = 0
    for i in elements_num.keys():
#        print(i)
        position_element = []
        for j in range(int(elements_num.get(i))):
            k = k+1 
#            print (k)
            position_i = linecache.getline(POSCAR_File, k+linenum-1).replace('\n', '').strip(' ').split(' ')
            position_i = [l for l in position_i if l !='']
            position_element.append(position_i)
        xx = {i: position_element}
        position.update(xx)

    return Info, Bravais, elements_num, position

def Find_Position(Index, element_num, Position):
    k = 0
    for i in element_num.keys():
        l = 0
        for j in range(int(element_num.get(i))):
            k = k+1
            if (int(Index) == k): 
               Position_i = Position.get(i)[l]
               element_i = i
            l = l+1
#    print(Position_i)
    return element_i, Position_i

def Replace_Element(ele_replace, POSCAR_orig, POSCAR, POSCAR_File):
    Info, Brava, element_num, Pos = READ_POSCAR (POSCAR)
    Info_orig, Brava_orig, element_num_orig, Pos_orig = READ_POSCAR (POSCAR_orig)
    
#    print(Pos)
#    print(element_num_orig)

    ComName = ''
    element_new ={}

#    elem_tot_i = 0
#    print(element_num)
    for i in ele_replace.keys():
#        elem_tot_i = elem_tot_i +len(ele_replace.get(i))
#        xx = {element[i]:elem_tot_i}
        element_num[i] = element_num[i] - len(ele_replace.get(i))

        for num_remove in ele_replace.get(i):
            element_orig, Position_i = Find_Position(num_remove, element_num_orig, Pos_orig)
            for k in Pos.get(i):
              t1 = abs(float(k[0]) - float(Position_i[0]))
              t2 = abs(float(k[1]) - float(Position_i[1]))
              t3 = abs(float(k[2]) - float(Position_i[2]))
              delt = t1*t1+t2*t2+t3*t3
              if delt <= 0.0001: 
                 element_num[element_orig] = element_num[element_orig] + 1
                 Pos.get(i).remove(k)
                 chang = ' --> ' + element_orig
                 k.append(chang)
                 Pos.get(element_orig).append(k)
#              print(delt, num_remove, element_orig, element_num[element_orig])

    for i in element_num.keys():
        if element_num[i] != 0 :
            xx = {i:element_num[i]}
            element_new.update(xx)
            ComName = ComName + i + '_'+str(element_num[i])
    Info[0] = ComName
#    print(ComName)

    with open(POSCAR_File,'w') as file:
         file.write(Info[0]+'\n')
         file.write(str(Info[1])+'\n')
         for i in range(3):
             for j in range(3):
                 file.write(str(Brava[3*i+j])+ '     ')
             file.write('\n')
         for i in element_new.keys(): 
            file.write(i + '  ')
         file.write('\n')
         for i in element_new.keys(): 
             file.write(str(element_new[i])+' ')
         file.write('\n')
         file.write(Info[2]+'\n')
         file.write(Info[3]+'\n')
#         exit(0)
         for i in element_new.keys():
             for j in Pos.get(i):
                 for k in j:
                     file.write(k+ ' ')
                 file.write('\n')
#                 print(Position[i][j])
    return

def make_targz_one_by_one(output_filename, source_dir):
   tar = tarfile.open(output_filename,"w:gz")
   for root,dir,files in os.walk(source_dir):
      for file in files:
         pathfile = os.path.join(root, file)
         tar.add(pathfile)
   tar.close()

#if __name__ == '__main__':
#    copyImg()
# exe_file = '/home/jun_jiang/Softs/Scrips/Structure_Energy'

Position_File = '/media/Windows/WORKS/2021-05/pos_9_2021-11/Position_binding'
POSCAR_orig_path, Alloy, Binding, object_path, replace_position = Read_Position(Position_File)

locate_path = os.getcwd()
# locate_path = '/media/Windows/WORKS/2021-05/pos_9yuan/2021-07-27'
# locate_path = '/media/Windows/WORKS/2021-05/pos_9yuan/2021-09-06'

#replace_element = {'Ta':3, 'Re':1}
#replace_position = {'Ta':[9,11,28], 'Re':[148]}
# object_path = ['2-p05']
# object_path = ['6-p05', '6-p12', '6-p18', '9-p05', '9-p10', '9-p11', '9-p12', '9-p13', '9-p18']
#object_path = ['6-p02', '6-p05_2', '6-p08', '6-p10', '6-p11', '6-p12_2', '6-p18_2', '6-p19', '9-p02', '9-p08', '9-p19']
# object_path = ['6-p02_test']
VASP_path = ['1-Relax_Step1','1-Relax_Step2','1-Relax_Step3','2-Static']

POSCAR_replace_file = locate_path +'/'+ 'POSCAR'+'_'+object_path
# POSCAR_Alloy_file = locate_path +'/'+ Alloy + '/' +'2-Static' +'/' + 'POSCAR'
POSCAR_Alloy_file = locate_path +'/'+ Alloy + '/' +'1-Relax_Step1' +'/' + 'POSCAR'

# print(POSCAR_Alloy_file)
# exit(0)
Replace_Element(replace_position, POSCAR_orig_path, POSCAR_Alloy_file, POSCAR_replace_file)
# exit (0)

# for j in object_path
#    current_path = os.path.join(locate_path,Binding, j)
current_path = os.path.join(locate_path, Binding, object_path)
#        current_path=locate_path+'/'+'Model-2021-09-06'+'/'+i+'/'+j
#        print(current_path)
#        exit()
if not(os.path.exists(current_path)):
    os.makedirs(current_path)
os.chdir(current_path)
shutil.copyfile(POSCAR_replace_file, 'POSCAR')
elements = linecache.getline(POSCAR_replace_file, 6)
#        print(elements)
#            exit()
generate_potcar = 'pmg potcar -f PBE -s '+ (elements)
os.system(generate_potcar)
#            exit()
INCAR_orig = os.path.join(locate_path, 'INCAR_2-Static')
#        INCAR_orig = locate_path + '/'+'INCAR_'+j
#        print(INCAR_orig)
#       exit()
KPOINTS_orig = os.path.join(locate_path, 'KPOINTS_2-Static')
#        KPOINTS_orig = locate_path + '/'+'KPOINTS_'+j
shutil.copyfile(INCAR_orig, 'INCAR')
shutil.copyfile(KPOINTS_orig, 'KPOINTS')
        
# current_path = os.path.join(locate_path, Binding)
# os.chdir(current_path)
# tar_gz_orig = object_path+'.tar.gz'
# make_targz_one_by_one(tar_gz_orig, object_path)
# shutil.copyfile('2021-12-21.tar.gz','../2021-12-21.tar.gz')
# shutil.move('2021-07-27.tar.gz','../')

# shutil.rmtree(tar_gz_orig)
# os.remove('2021-12-21.tar.gz')
end_time = time.time()
print(end_time-start_time,'秒')
#    path2 = "C:\\Program Files\\MATLAB\\R2014b\\toolbox\\gatbx\\Test_fns\\" 
#   rename_func(path2)
