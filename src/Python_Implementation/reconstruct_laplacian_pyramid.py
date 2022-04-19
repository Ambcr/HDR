# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 15:35:20 2022

@author: Ambcr
"""

from cv2_process import upsample


def reconstruct_laplacian_pyramid(pyr):
    nlev = len(pyr)
    R = pyr[nlev-1]
    for l in range(nlev-2, -1, -1):
        R = pyr[l] + upsample(R)

    return R
