import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

from mpl_toolkits.mplot3d import Axes3D

img = mpimg.imread('/home/jun-jiang/Documents/Latex_Beamer/Figures/Zhu-Liu.jpg')
#print(img)   # Importing image data into Numpy arrays

# imgplot = plt.imshow(img)  #Plotting numpy arrays as images

lum_img = img[:, :, 0] # Applying pseudocolor schemes to image plots
# plt.imshow(lum_img)
# plt.imshow(lum_img, cmap="hot")

# imgplot = plt.imshow(lum_img)
# imgplot.set_cmap('nipy_spectral')


# plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')  # Examining a specific data range

# imgplot = plt.imshow(lum_img, clim=(0.0, 0.7)) #

#fig = plt.figure()
#ax = fig.add_subplot(1, 2, 1)
#imgplot = plt.imshow(lum_img)
#ax.set_title('Before')
#plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')
#ax = fig.add_subplot(1, 2, 2)
#imgplot = plt.imshow(lum_img)
#imgplot.set_clim(0.0, 0.7)
#ax.set_title('After')
#plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')

# Array Interpolation schemes

# img = Image.open('/home/jun-jiang/Documents/Latex_Beamer/Figures/Wang_Shoujing.jpg')
# img.thumbnail((64, 64), Image.ANTIALIAS)  # resizes image in-place
#imgplot = plt.imshow(img)
# imgplot = plt.imshow(img, interpolation="nearest")
# imgplot = plt.imshow(img, interpolation="bicubic")
#plt.plot([1, 2, 3, 4])
#plt.ylabel('some numbers')

# 定义坐标轴
fig = plt.figure()
ax1 = plt.axes(projection = '3d')
# ax = fig.add_subplot(111,projection = '3d') # 这种方法可以画多个子图

# 利用三维轴方法
# ax2 = Axes3D(fig)

# plt.colorbar()  # Color scale reference

# 定义三维数据
xx = np.arange(-5,5,0.1)
yy = np.arange(-5,5,0.1)
X, Y = np.meshgrid(xx, yy)
Z = np.sin(X)+np.cos(Y)

# 作图
ax1.plot_surface(X,Y,Z, cmap='rainbow')
ax1.plot_surface(X,Y,Z, rstride = 1, cstride = 1, cmap='rainbow') # row和cloum_stride 为横竖方向的绘图采样步长，越小绘图越精细
# ax1.contour(X,Y,Z, zdim='z', offset=-2, cmap='rainbow') # 等高线图，要设置offset,为Z的最小值
plt.show()
