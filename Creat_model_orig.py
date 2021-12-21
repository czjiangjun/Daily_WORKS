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

def Replace_Element(ele_replace, POSCAR_orig, POSCAR_File):
    Info_orig, Brava_orig, element_num_orig, Pos_orig = READ_POSCAR (POSCAR_orig)
    
#    print(Pos)
#    print(element_num_orig)

    ComName = ''
    element_num ={}
    Pos_add = {}

    elem_tot_i = 0
#    print(element_num)
    for i in ele_replace.keys():
        element_num_i = len(ele_replace.get(i))
        xx = {i:element_num_i}
        element_num.update(xx)
        Positions_i = []

        for num_remove in ele_replace.get(i):
            element_orig, Position_i = Find_Position(num_remove, element_num_orig, Pos_orig)
            if (len(Position_i) >3):
                Position_i[-1] = element_orig + ' --> ' + i
            Pos_orig.get(element_orig).remove(Position_i)

#            print (Pos_orig)

            Positions_i.append(Position_i)
            element_num_orig[element_orig] = element_num_orig[element_orig]-1
            
        xx = {i:Positions_i}
        Pos_add.update(xx)
    element_num_orig.update(element_num)
    Pos_orig.update(Pos_add)
#    print (element_num_orig)

#            for k in Pos.get(i):
#              t1 = abs(float(k[0]) - float(Position_i[0]))
#              t2 = abs(float(k[1]) - float(Position_i[1]))
#              t3 = abs(float(k[2]) - float(Position_i[2]))
#              delt = t1*t1+t2*t2+t3*t3
#              if delt <= 0.0001: 
#                 Pos.get(i).remove(k)
#                 Pos.get(element_orig).append(k)

    elements = {}
    for i in element_num_orig.keys():
        if element_num_orig[i] != 0 :
            xx = {i:element_num_orig[i]}
            elements.update(xx)
            ComName = ComName + i + '_'+str(element_num_orig[i])
    Info_orig[0] = ComName
#    print(ComName)
#    exit(0)

    with open(POSCAR_File,'w') as file:
         file.write(Info_orig[0]+'\n')
         file.write(str(Info_orig[1])+'\n')
         for i in range(3):
             for j in range(3):
                 file.write(str(Brava_orig[3*i+j])+ '     ')
             file.write('\n')
         for i in element_num_orig.keys(): 
            file.write(i + '  ')
         file.write('\n')
         for i in element_num_orig.keys(): 
             file.write(str(element_num_orig[i])+' ')
         file.write('\n')
         file.write(Info_orig[2]+'\n')
         file.write(Info_orig[3]+'\n')
#         exit(0)
         for i in element_num_orig.keys():
             for j in Pos_orig.get(i):
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

POSCAR_orig_path = '/media/Windows/WORKS/2021-05/POSCAR_392_orig'
VASP_path = ['1-Relax_Step1','1-Relax_Step2','1-Relax_Step3','2-Static']

# locate_path = '/media/Windows/WORKS/2021-05/pos_9yuan/2021-09-06'
# locate_path = '/media/Windows/WORKS/2021-05/pos_9yuan/2021-07-27'
locate_path = '/media/Windows/WORKS/2021-05/pos_9_2021-11'

replace_position = {'Ta':[2,4,5,7,8,81,17,20], 'Re':[148]}

object_path = ['9-p02_TEST']
# object_path = ['6-p05', '6-p12', '6-p18', '9-p05', '9-p10', '9-p11', '9-p12', '9-p13', '9-p18']
#object_path = ['6-p02', '6-p05_2', '6-p08', '6-p10', '6-p11', '6-p12_2', '6-p18_2', '6-p19', '9-p02', '9-p08', '9-p19']
# object_path = ['6-p02_test']

POSCAR_replace_file = locate_path +'/'+ 'POSCAR'+'_'+object_path[0]

Replace_Element(replace_position, POSCAR_orig_path, POSCAR_replace_file)
# exit (0)

for j in VASP_path:
    current_path = os.path.join(locate_path,'Model-2021-12-21', object_path[0], j)
#        current_path=locate_path+'/'+'Model-2021-09-06'+'/'+i+'/'+j
#        print(current_path)
#        exit()
    if not(os.path.exists(current_path)):
         os.makedirs(current_path)
    os.chdir(current_path)
    if (j == VASP_path[0]):
        shutil.copyfile(POSCAR_replace_file, 'POSCAR')
        elements = linecache.getline(POSCAR_replace_file, 6)
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
#       exit()
    KPOINTS_orig = os.path.join(locate_path, 'KPOINTS_'+j)
#        KPOINTS_orig = locate_path + '/'+'KPOINTS_'+j
    shutil.copyfile(INCAR_orig, 'INCAR')
    shutil.copyfile(KPOINTS_orig, 'KPOINTS')
        
current_path = os.path.join(locate_path,'Model-2021-12-21', object_path[0])
os.chdir(current_path)
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
