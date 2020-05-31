# -*- coding: utf-8 -*-
"""
Created on Sun May 31 20:00:30 2020

@author: jocam
"""

import cv2
import numpy as np
import os

def int_to_bin(rgb):

    r, g, b = rgb
    return ('{0:08b}'.format(r),
            '{0:08b}'.format(g),
            '{0:08b}'.format(b))

def unmerge_rgb(rgb):
    r, g, b = rgb
    rgb = (r[4:] + '0000',
           g[4:] + '0000',
           b[4:] + '0000')
    return rgb

def bin_to_int(rgb):
    r, g, b = rgb
    return (int(r, 2),
            int(g, 2),
            int(b, 2))

def get_size():
    width = img[-1][-1][0]*255 + img[-1][-1][1]
    height = img[-1][-2][0]*255 + img[-1][-2][1]
    return width, height

def get_image(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".png") or file.endswith(".jpg"):
                return path+file

i = j = 0

img = cv2.imread(get_image('ImageToDecode/'),1)

width, height = get_size()   

newImg = np.zeros((width,height,3), dtype=int)


ratio = (len(img)*len(img[0])) // (width*height)

for row in range(width):
    for col in range(height):
        rgb1 = int_to_bin(img[i][j])
        
        rgb = unmerge_rgb(rgb1)
        
        newImg[row][col] = bin_to_int(rgb)
        
        j += ratio
        if j >= len(img[0]):
            j = 0
            i += 1

cv2.imwrite('reveal.png',newImg)

