# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:40:42 2017

@author: mong
"""
from __future__ import division
import numpy as np
import time

def PA(MatrixAdjacency_Train):
    similarity_StartTime = time.clock()
    
    deg_row = sum(MatrixAdjacency_Train)
    deg_row.shape = (deg_row.shape[0],1)
    deg_row_T = deg_row.T
    
    Matrix_similarity = np.dot(deg_row,deg_row_T)

    similarity_EndTime = time.clock()
    print ("    SimilarityTime: %f s" % (similarity_EndTime- similarity_StartTime))
    return Matrix_similarity
