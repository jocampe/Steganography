# -*- coding: utf-8 -*-
"""
Created on Sun May 31 20:00:20 2020

@author: jocam
"""

import cv2
import os
import ctypes
import sys

def int_to_bin(rgb):
    r, g, b = rgb
    return ('{0:08b}'.format(r),
            '{0:08b}'.format(g),
            '{0:08b}'.format(b))

def merge_rgb(rgb1, rgb2):
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    rgb = (r1[:4] + r2[:4],
           g1[:4] + g2[:4],
           b1[:4] + b2[:4])
    return rgb

def bin_to_int(rgb):
    r, g, b = rgb
    return (int(r, 2),
            int(g, 2),
            int(b, 2))
    
#the size of the hiden image is kept in the last 2 cells
def insert_size():
    img[-1][-1][0] = len(imgHide)/255
    img[-1][-1][1] = len(imgHide)%255
    
    img[-1][-2][0] = len(imgHide[0])/255
    img[-1][-2][1] = len(imgHide[0])%255
    
def get_image(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".png") or file.endswith(".jpg"):
                return path+file
            
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
            
img = cv2.imread(get_image(ROOT_DIR+'\CoverImages\\'),1)
imgHide = cv2.imread(get_image(ROOT_DIR+'\ImageToEncode\\'),1)

i = j = 0

ratio = (len(img)*len(img[0])) // (len(imgHide)*len(imgHide[0]))
if ratio < 1:
    ctypes.windll.user32.MessageBoxW(0, "CoverImage MUST have a bigger size", "Alert!", 1)
    sys.exit()

for row in imgHide:
    for cell in row:
        
        rgb1 = int_to_bin(img[i][j])
        rgb2 = int_to_bin(cell)
        
        rgb = merge_rgb(rgb1, rgb2)

        img[i][j] = bin_to_int(rgb)
    
        j += ratio
        if j >= len(img[0]):
            j = 0
            i += 1

insert_size()

cv2.imwrite(ROOT_DIR+'\secret.png',img)

