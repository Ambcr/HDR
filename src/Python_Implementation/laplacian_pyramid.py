# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 15:35:02 2022

@author: Ambcr
"""

from cv2_process import downsample, upsample


def laplacian_pyramid(I, nlev):
    pyr = []
    J = I
    for l in range(nlev-1):
        I = downsample(J)
        pyr.append(J - upsample(I))
        J = I
    pyr.append(J)
    return pyr
