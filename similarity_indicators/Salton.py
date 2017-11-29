# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:42:55 2017

@author: mong
"""
from __future__ import division
import numpy as np
import time


def Salton(MatrixAdjacency_Train):
    similarity_StartTime = time.clock()
    
    similarity = np.dot(MatrixAdjacency_Train,MatrixAdjacency_Train)
    
    deg_row = sum(MatrixAdjacency_Train)
    deg_row.shape = (deg_row.shape[0],1)
    deg_row_T = deg_row.T
    tempdeg = np.dot(deg_row,deg_row_T)
    temp = np.sqrt(tempdeg)
    
    np.seterr(divide='ignore', invalid='ignore')
    Matrix_similarity = np.nan_to_num(similarity / temp)
    similarity_EndTime = time.clock()
    print ("    SimilarityTime: %f s" % (similarity_EndTime- similarity_StartTime))
    return Matrix_similarity
