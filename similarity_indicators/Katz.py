# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 11:17:58 2017

@author: mong
"""

import numpy as np
import time

def Katz(MatrixAdjacency_Train):
    similarity_StartTime = time.clock()
    Parameter = 0.01
    Matrix_EYE = np.eye(MatrixAdjacency_Train.shape[0])
    Temp = Matrix_EYE - MatrixAdjacency_Train * Parameter
    
    Matrix_similarity = np.linalg.inv(Temp)

    Matrix_similarity = Matrix_similarity - Matrix_EYE

    similarity_EndTime = time.clock()
    print ("    SimilarityTime: %f s" % (similarity_EndTime- similarity_StartTime))
    return Matrix_similarity
