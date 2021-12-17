import os
import shutil
import tarfile
import linecache
import subprocess 
import time

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
def READ_POSCAR(POSCAR_File):
    # READ_Name   %line_1
    Compound_Name = linecache.getline(POSCAR_File, 1).replace('\n', '').strip(' ').split(' ')
#    print (Compound_Name)
    # READ_Scale   %line_2
    scale = linecache.getline(POSCAR_File, 2).replace('\n', '').strip(' ').split(' ')
#    print (scale)
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
    elements = linecache.getline(POSCAR_File, 6).replace('\n', '').strip(' ').split(' ')
    elements = [i for i in elements if i !='']
    elem_num = linecache.getline(POSCAR_File, 7).replace('\n', '').strip(' ').split(' ')
    elem_num = [int(i) for i in elem_num if i !='']
#    print(len(elem_num))
    for i in range(len(elem_num)):
        xx = {elements[i]: int(elem_num[i])}
        elem_ind.update(xx)
        elem_tot = elem_tot+int(elem_num[i])
#    print(elem_tot)

    # READ_Select_and_Dynamic   %line_8-9
#    Compound_Select = ''
    Compound_Dynamics = ''
    Compound_read = linecache.getline(POSCAR_File, 8).replace('\n', '').strip(' ').split(' ')
    list = Compound_read[0]
#    print(list[0])
    if (list[0] == 'S' or list[0] == 's'):
        Compound_Select = Compound_read[0]
        Compound_read = linecache.getline(POSCAR_File, 9).replace('\n', '').strip(' ').split(' ')
        Compound_Dynamics = Compound_read[0]
        linenum = 10
    else:
        Compound_Dynamics = Compound_read[0]
        linenum = 9

    # READ_Position   %line_10
    position = []
    for i in range(elem_tot):
        position_i = linecache.getline(POSCAR_File, i+linenum).replace('\n', '').strip(' ').split(' ')
        position.append([j for j in position_i if j !=''])

    return scale, Bravais, elements, elem_num, elem_tot, Compound_Select, Compound_Dynamics, position

def Devide_Positions(Index, Position, Position_orig):
    Position_i = []
    for i in Index:
        Position_ele = Position_orig[int(i)-1]
#        print(Position_ele)
        Position.remove(Position_ele) 
        Position_i.append(Position_ele)
    return  Position, Position_i

def Replace_Element(ele_add, ele_replace, POSCAR, POSCAR_File):
    sca, Brava, element, elem_num, elem_tot, Comp_S, Comp_D, Pos = READ_POSCAR (POSCAR)

    ComName = ''
    replace =[]
    elem_ind = {}
    elem_tot_i = 0

    for i in range(len(element)):
        elem_tot_i = elem_tot_i +elem_num[i]
        xx = {element[i]:elem_tot_i}
        elem_ind.update(xx)
#    print(elem_ind)

    for i in ele_replace:
        num_add = ele_replace.get(i)
        for j in num_add:
            replace.append(int(j))
#    print(replace)

    for i in replace:
        for j in range(len(element)):
            ind_0 = elem_ind.get(element[j])-elem_num[j]
            ind_1 = elem_ind.get(element[j])
            if (i < ind_1 and i >= ind_0):
                elem_num[j] = elem_num[j]-1
#    print(elem_num)

    element_add = ele_add.keys()
    for i in element_add:
        element.append(i)
#    print(element)
    for i in ele_add:
        elem_num.append(ele_add.get(i))

#        print(elem_num)
    for i in range(len(element)):
        ComName = ComName + element[i]+'_'+str(elem_num[i])
#    print(ComName)
    Pos_i = Pos
    for i in ele_replace:
       Index = ele_replace.get(i)
       Pos_i, Pos_rem = Devide_Positions(Index, Pos_i, Pos)
#       print(Pos_i)
#       print(Pos_rem)
#       exit(0)
    Position = Pos_i+Pos_rem
    Position = np.array(Position)

#    print(Position)
#    exit(0)
    with open(POSCAR_File,'w') as file:
         file.write(ComName+'\n')
         file.write(sca[0]+'\n')
         for i in range(3):
             for j in range(3):
                 file.write(str(Brava[3*i+j])+ '     ')
             file.write('\n')
         for i in range(len(element)): 
            file.write(element[i]+' ')
         file.write('\n')
         for i in range(len(elem_num)): 
             file.write(str(elem_num[i])+' ')
         file.write('\n')
         file.write(Comp_S+'\n')
         file.write(Comp_D+'\n')
         for i in range(elem_tot):
             for j in range(len(Position[i][:])):
                 file.write(str(Position[i][j])+ '     ')
                 print(Position[i][j])
             file.write('\n')

    return

def Check_Positions(position, elem_tot, position_list):
    Index = []
    for i in position:
        position_i = np.array(position[i])
        dist_min = 10000.0

        for j in range(elem_tot):
            position_j = np.array(position_list[j])
            dist = (position_i[0]-position_j[0])*(position_i[0]-position_j[0]) + \
                   (position_i[1]-position_j[1])*(position_i[1]-position_j[1]) + \
                   (position_i[2]-position_j[2])*(position_i[2]-position_j[2])

            if dist <= dist_min:
                dist_min = dist
        Index.append(j)
    return Index

#if __name__ == '__main__':
#    copyImg()
# exe_file = '/home/jun_jiang/Softs/Scrips/Structure_Energy'

# locate_path = '/media/Windows/WORKS/2021-05/pos_9yuan/2021-09-06'
POSCAR_orig_path = '/media/Windows/WORKS/2021-05/POSCAR_392_orig'
locate_path = '/media/Windows/WORKS/2021-05/pos_9yuan/2021-07-27'

replace_element = {'Ta':3, 'Re':1}
replace_position = {'Ta':[2,81,20], 'Re':[148]}
object_path = ['2-p05']
# object_path = ['6-p05', '6-p12', '6-p18', '9-p05', '9-p10', '9-p11', '9-p12', '9-p13', '9-p18']
#object_path = ['6-p02', '6-p05_2', '6-p08', '6-p10', '6-p11', '6-p12_2', '6-p18_2', '6-p19', '9-p02', '9-p08', '9-p19']
# object_path = ['6-p02_test']
VASP_path = ['1-Relax_Step1','1-Relax_Step2','1-Relax_Step3','2-Static']

POSCAR_replace_file = locate_path +'/'+ 'POSCAR'+'_'+object_path[0]

Replace_Element(replace_element, replace_position, POSCAR_orig_path, POSCAR_replace_file)
exit (0)
for i in object_path:
    POSCAR_orig = locate_path+'/'+'POSCAR_'+i

    for j in VASP_path:
        current_path = os.path.join(locate_path,'Model-2021-07-27',i,j)
#        current_path=locate_path+'/'+'Model-2021-07-27'+'/'+i+'/'+j
#        print(current_path)
#        exit()
        if not(os.path.exists(current_path)):
            os.makedirs(current_path)
        os.chdir(current_path)
        if (j == VASP_path[0]):
            shutil.copyfile(POSCAR_orig, 'POSCAR')
            elements = linecache.getline(POSCAR_orig, 6)
            print(elements)
#            exit()
            generate_potcar = 'pmg potcar -f PBE -s '+ (elements)
            os.system(generate_potcar)
#            exit()
        else:
            POTCAR_orig = '../1-Relax_Step1/POTCAR'
            shutil.copyfile(POTCAR_orig, 'POTCAR')
        INCAR_orig = os.path.join(locate_path, 'INCAR_'+j)
#        INCAR_orig = locate_path + '/'+'INCAR_'+j
#        print(INCAR_orig)
#        exit()
        KPOINTS_orig = os.path.join(locate_path, 'KPOINTS_'+j)
#        KPOINTS_orig = locate_path + '/'+'KPOINTS_'+j
        shutil.copyfile(INCAR_orig, 'INCAR')
        shutil.copyfile(KPOINTS_orig, 'KPOINTS')
        
os.chdir(locate_path)
#tar_gz_orig = locate_path+'/'+'Model-2021-09-06'
tar_gz_orig = 'Model-2021-07-27'
make_targz_one_by_one('2021-07-27.tar.gz', tar_gz_orig)
shutil.copyfile('2021-07-27.tar.gz','../2021-07-27.tar.gz')
#shutil.move('2021-07-27.tar.gz','../')

shutil.rmtree(tar_gz_orig)
os.remove('2021-07-27.tar.gz')

end_time = time.time()
print(end_time-start_time,'秒')
#    path2 = "C:\\Program Files\\MATLAB\\R2014b\\toolbox\\gatbx\\Test_fns\\" 
#   rename_func(path2)
