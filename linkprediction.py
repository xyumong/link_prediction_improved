# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:10:54 2017

@author: mong
"""
from __future__ import division#精确除法（使用'/'时，保留小数）
import Initialize
from Evaluation_Indicators import Calculation_AUC
import time
import similarity_indicators.CommonNeighbor
import similarity_indicators.Salton
import similarity_indicators.Jaccard
import similarity_indicators.Sorenson
import similarity_indicators.HPI
import similarity_indicators.HDI
import similarity_indicators.LHN_I
import similarity_indicators.PA
import similarity_indicators.AA
import similarity_indicators.RA
import similarity_indicators.LP
import similarity_indicators.Katz
import pandas as pd
import numpy as np
import similarity_indicators.mixture_index

startTime = time.clock()

similarity_StartTime = time.clock()

# Matrix_similarity = similarity_indicators.Cos.ACT(MatrixAdjacency_Train)
def get_auc_all(MatrixAdjacency_Train,MatrixAdjacency_Test, MaxNodeNum):
    auc=[]
    for Method in range(12):
        if Method == 0:
            print ('----------SIM----------共同邻居----------SIM----------')
            print ('----------CN----------')
            Matrix_similarity = similarity_indicators.CommonNeighbor.Cn(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        
        elif Method == 1:
            print ('---------Salton-----------')
            Matrix_similarity = similarity_indicators.Salton.Salton(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        elif Method == 2:
            print ('---------Jaccavrd-----------')            
            Matrix_similarity = similarity_indicators.Jaccard.Jaccavrd(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        elif Method == 3:
            print ('---------Sorenson-----------')  
            Matrix_similarity = similarity_indicators.Sorenson.Sorenson(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        elif Method == 4:
            print ('---------HPI-----------') 
            Matrix_similarity = similarity_indicators.HPI.HPI(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        elif Method == 5:
            print ('---------HDI-----------') 
            Matrix_similarity = similarity_indicators.HDI.HDI(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        elif Method == 6:
            print ('---------LHN_I-----------')
            Matrix_similarity = similarity_indicators.LHN_I.LHN_I(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        elif Method == 7:
            print ('---------PA-----------')
            Matrix_similarity = similarity_indicators.PA.PA(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        elif Method == 8:
            print ('---------AA-----------')
            Matrix_similarity = similarity_indicators.AA.AA(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        elif Method == 9:
            print ('---------RA-----------')
            Matrix_similarity = similarity_indicators.RA.RA(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        elif Method == 10:
            print ('---------LP-----------')
            Matrix_similarity = similarity_indicators.LP.LP(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        elif Method == 11:
            print ('---------Katz-----------')
            Matrix_similarity = similarity_indicators.Katz.Katz(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        
        
        else:
            print ("Method Error!")
        
    return auc

similarity_EndTime = time.clock()
print ('----------！！----------')
print ("All SimilarityTime: %f s" % (similarity_EndTime- similarity_StartTime))


def cross_validation(NetFile,NetName,fold=10):
    auc_val=np.zeros(12)
    methods=['CN','Salton','Jaccard','Sorenson','HPI','HDI','LHN-I','PA','AA','RA','LP','Katz']
    for i in range(10): 
        MatrixAdjacency_Net,MaxNodeNum = Initialize.Init(NetFile)
        MatrixAdjacency_Train,MatrixAdjacency_Test = Initialize.Divide(NetFile, MatrixAdjacency_Net, MaxNodeNum,NetName)
        auc=get_auc_all(MatrixAdjacency_Train,MatrixAdjacency_Test, MaxNodeNum)
        auc=np.array(auc)
        auc_val+=auc
    auc_val=(0.1)*auc_val
    auc_val=pd.Series(auc_val,index=methods)
    auc_val.name='auc'    
    return auc_val

