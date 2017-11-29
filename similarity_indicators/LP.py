# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:39:35 2017

@author: mong
"""
from __future__ import division
import numpy as np
import time

def LP(MatrixAdjacency_Train):
    similarity_StartTime = time.clock()
    Matrix_similarity = np.dot(MatrixAdjacency_Train,MatrixAdjacency_Train)
    
    Parameter = 1
    Matrix_LP = np.dot(np.dot(MatrixAdjacency_Train,MatrixAdjacency_Train),MatrixAdjacency_Train) * Parameter
    
    Matrix_similarity = np.dot(Matrix_similarity,Matrix_LP)
    similarity_EndTime = time.clock()
    print ("    SimilarityTime: %f s" % (similarity_EndTime- similarity_StartTime))
    return Matrix_similarity
