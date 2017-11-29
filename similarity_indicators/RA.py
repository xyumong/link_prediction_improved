# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:41:38 2017

@author: mong
"""
from __future__ import division
import numpy as np
import time

def RA(MatrixAdjacency_Train):
    similarity_StartTime = time.clock()
    
    RA_Train = sum(MatrixAdjacency_Train)
    RA_Train.shape = (RA_Train.shape[0],1)
    MatrixAdjacency_Train_Log = MatrixAdjacency_Train / RA_Train
    MatrixAdjacency_Train_Log = np.nan_to_num(MatrixAdjacency_Train_Log)

    Matrix_similarity = np.dot(MatrixAdjacency_Train,MatrixAdjacency_Train_Log)

    similarity_EndTime = time.clock()
    print ("    SimilarityTime: %f s" % (similarity_EndTime- similarity_StartTime))
    return Matrix_similarity
