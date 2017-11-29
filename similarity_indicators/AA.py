# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:31:32 2017

@author: mong
"""
from __future__ import division
import numpy as np
import time

def AA(MatrixAdjacency_Train):
    similarity_StartTime = time.clock()
    
    logTrain = np.log(sum(MatrixAdjacency_Train))
    logTrain = np.nan_to_num(logTrain)
    logTrain.shape = (logTrain.shape[0],1)
    MatrixAdjacency_Train_Log = MatrixAdjacency_Train / logTrain
    MatrixAdjacency_Train_Log = np.nan_to_num(MatrixAdjacency_Train_Log)
    
    Matrix_similarity = np.dot(MatrixAdjacency_Train,MatrixAdjacency_Train_Log)

    similarity_EndTime = time.clock()
    print ("    SimilarityTime: %f s" % (similarity_EndTime- similarity_StartTime)) 
    return Matrix_similarity
