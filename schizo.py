# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 18:02:10 2016

@author: ling
"""

import os
import scipy.stats
import pandas as pd
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt

#%%
'load and view nii files'
def _nii_(file_path,file_name):
    a=nib.load(os.path.join(file_path,file_name)).get_data()
    return a

#%% for MRI data

b=_nii_('C:\Users\ling\Documents\GitHub','schizophrenia_voxelwise154330.nii')
b=np.reshape(np.array(b),(int(b.shape[0])*int(b.shape[1])*int(b.shape[2])))
e=[]
for dirPath,dirNames,fileNames in os.walk('C:\Users\ling\Desktop\Try\data'):
    for i in fileNames:
        a=_nii_(dirPath,i)
        a=np.reshape(np.array(a),(int(a.shape[0])*int(a.shape[1])*int(a.shape[2]),int(a.shape[3])))
        a[np.isnan(a)]=0
        c=[]
        for i in range(len(b)):
            if b[i]!=0:
                d=a[i]
                c.append(d)
        c=np.asarray(c)
#        e.append(c)

#%%








