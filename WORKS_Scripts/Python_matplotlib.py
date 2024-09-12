#!/usr/bin/env python   
#!coding = utf-8
import os
import time
import random

# g = PyGnuplot.Gnuplot()   

import PyGnuplot as gp 
import numpy as np 

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D

# X=np.arange(10)
# Y=np.sin(X/(2*np.pi))
# Z=Y**2.0

# gp.s([X,Y,Z])

#gp.c('plot "tmp.dat" u 1:2 w lp')
#gp.c('replot "tmp.dat" u 1:3 w lp')
# gp.c('set encoding utf8')
# gp.c('set xlabel "x"')


# current_path = os.system("pwd")
# print(current_path)

class Fig_Draw:
      def __init__(self, name, file, labels, type = None, column = None, cure_type = None, marker= None):
          style = {1:'-',2:'-.',3:'--',4:'-._'}
          style_index = list(style.keys())
          style_line = list(style.values())

          self.name = name
          self.file = file
          self.column = [1,2]
          if not (column == None):
              self.column = column
          self.labels = ['X-label', 'Y-label']
          self.labels[0] = labels[0]
          self.labels[1] = labels[1]
#          print (self.labels)
          self.type = style_line[random.choice(style_index)-1]
          if not (type == None):
              self.type = type
          self.cure_type = cure_type
          self.marker = '+'
          if not (marker == None):
              self.marker = marker
          self.Data_XX=[]
          self.Data_YY=[]


      def Data(self, file):
          print (file)
          Data_File = open(file, 'r')
          num = 0
          for line in Data_File:
              Data = line.replace('\n', '').strip('').split(' ')
              Data = [i for i in Data if i !='']
#               print(Data[1])
              self.Data_XX.append(float(Data[self.column[0]-1]))
              self.Data_YY.append(float(Data[self.column[1]-1]))
              num = num + 1
#          print(Data_XX)
          return self.Data_XX, self.Data_YY

      def Fig(self, Data_XX, Data_YY):
#          Data_XX = self.Data_XX
#          Data_YY = self.Data_YY
          xmin = round(Data_XX[0])
          xmax = round(Data_XX[-1])
          xmin = xmin-0.05*(xmax-xmin)
          xmax = xmax+0.05*(xmax-xmin)
          ymin = round(min(Data_YY))
          ymax = round(max(Data_YY))
          ymin = ymin-0.05*(ymax-ymin)
          ymax = ymax+0.05*(ymax-ymin)

#          print(xmin, xmax)
#          print(ymin, ymax)
          plt.axis([xmin,xmax,ymin,ymax])
          plt.xlabel(self.labels[0])
          plt.ylabel(self.labels[1])

          # 设置x轴的标签为科学计数法
#          plt.xticks(Data_XX, fontsize=8, rotation=45)
          plt.xticks(fontsize=8, rotation=45)
          plt.yticks(Data_YY, fontsize=8, rotation=45)
          plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))

          plt.plot(Data_XX, Data_YY, label = self.name, ls = self.type, marker = self.marker)
#           plt.legend(loc='best') 
          plt.title(self.name)

          plt.savefig(self.name + ".png")
#          plt.savefig(self.name + ".pdf")
#          plt.savefig(self.name + ".eps")
          plt.show()
          return

#     
def main():

#    print(type)
#    style_type = {1:'-',2:'-.',3:'--',4:'-._'}
    Fig_Name = 'TEST'
    Data_File = '/home/jun-jiang/BCC/2023-NICE/Ni-CO2/C-O_H-E_1'
    labels = ['C-H/O-H','E-energy/eV']
    style_type = '-.'
#    column = [1,2]
    File_Draw = Fig_Draw(Fig_Name, Data_File, labels, style_type)
    XX, YY = File_Draw.Data(Data_File)
#    print (XX, YY)
    File_Draw.Fig(XX, YY)

if __name__ == '__main__':
    main()
    # print(__name__)

