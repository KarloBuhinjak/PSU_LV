


import matplotlib.pyplot as plt
import numpy as np
import skimage.io
img = skimage.io.imread('tiger.png', as_gray=True)


plt.figure(1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)

rows,cols=img.shape


for i in range(rows):
    for j in range(cols):
        img[i][j]+=45

plt.figure(2)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()
