# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:32:21 2017

@author: mong
"""
from __future__ import division
import numpy as np
import time

def Cn(MatrixAdjacency_Train):
    similarity_StartTime = time.clock()
    Matrix_similarity = np.dot(MatrixAdjacency_Train,MatrixAdjacency_Train)
    
    similarity_EndTime = time.clock()
    print ("    SimilarityTime: %f s" % (similarity_EndTime- similarity_StartTime))
    return Matrix_similarity
