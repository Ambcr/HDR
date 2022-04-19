# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 15:35:40 2022

@author: Ambcr
"""

import cv2
import time


def downsample(I):
    return cv2.resize(I, dsize=(0, 0), fx=0.5, fy=0.5)


def upsample(I):
    return cv2.resize(I, dsize=(0, 0), fx=2, fy=2)


def rgb2gray(I):
    img_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
    return img_gray / 255


def imfilter(I, h):
    return cv2.filter2D(I, -1, h)


def contrast_clahe(I):
    b, g, r = cv2.split(I)
    
    start1=time.perf_counter()
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(8, 8))
    
    b = clahe.apply(b)
    g = clahe.apply(g)
    r = clahe.apply(r)
    image = cv2.merge([b, g, r])
    end1=time.perf_counter()
    
    print(end1-start1)
    return image
