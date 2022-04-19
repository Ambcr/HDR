# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 15:34:35 2022

@author: Ambcr
"""

from cv2_process import downsample


def gaussian_pyramid(I, nlev):
    pyr = [I]
    for l in range(1, nlev):
        I = downsample(I)
        pyr.append(I)
    return pyr
