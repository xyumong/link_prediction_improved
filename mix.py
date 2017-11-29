# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:10:54 2017

@author: mong
"""

import time
import Initialize
from Evaluation_Indicators import Calculation_AUC
import pandas as pd
import numpy as np
import similarity_indicators.mixture_index


startTime = time.clock()

similarity_StartTime = time.clock()

# Matrix_similarity = similarity_indicators.Cos.ACT(MatrixAdjacency_Train)
def get_auc_mix(MatrixAdjacency_Train,MatrixAdjacency_Test, MaxNodeNum):

    auc=[]
    for Method in range(23):
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
        elif Method == 12:
            print ('----------SIM----------混合指标----------SIM----------')
            print ('----------1----------')
            Matrix_similarity = similarity_indicators.mixture_index.mixture_index_1(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))     
        elif Method == 13:
            print ('----------2----------')
            Matrix_similarity = similarity_indicators.mixture_index.mixture_index_2(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        elif Method == 14:
            print ('----------3----------')
            Matrix_similarity = similarity_indicators.mixture_index.mixture_index_3(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        elif Method ==15:
            print ('----------4----------')
            Matrix_similarity = similarity_indicators.mixture_index.mixture_index_4(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        elif Method == 16:
            print ('----------5----------')
            Matrix_similarity = similarity_indicators.mixture_index.mixture_index_5(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        elif Method == 17:
            print ('----------6----------')
            Matrix_similarity = similarity_indicators.mixture_index.mixture_index_6(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        elif Method == 18:
            print ('----------7----------')
            Matrix_similarity = similarity_indicators.mixture_index.mixture_index_7(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        elif Method == 19:
            print ('----------8----------')
            Matrix_similarity = similarity_indicators.mixture_index.mixture_index_8(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        elif Method == 20:
            print ('----------9----------')
            Matrix_similarity = similarity_indicators.mixture_index.mixture_index_9(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        elif Method == 21:
            print ('----------10----------')
            Matrix_similarity = similarity_indicators.mixture_index.mixture_index_10(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))
        elif Method == 22:
            print ('----------11----------')
            Matrix_similarity = similarity_indicators.mixture_index.mixture_index_11(MatrixAdjacency_Train)
            auc.append(Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum))    
        else:
            print ("Method Error!")
    return auc
        
similarity_EndTime = time.clock()
print ('----------！！----------')
print ("All SimilarityTime: %f s" % (similarity_EndTime- similarity_StartTime))

def cross_validation(NetFile,NetName,fold=10):
    methods=['CN','Salton','Jaccard','Sorenson','HPI','HDI','LHN-I','PA','AA','RA','LP','Katz']
    auc_mix=np.zeros(23)
    for i in range(10):   
        MatrixAdjacency_Net,MaxNodeNum = Initialize.Init(NetFile)
        MatrixAdjacency_Train,MatrixAdjacency_Test = Initialize.Divide(NetFile, MatrixAdjacency_Net, MaxNodeNum,NetName)
        auc=get_auc_mix(MatrixAdjacency_Train,MatrixAdjacency_Test, MaxNodeNum)
        auc=np.array(auc)
        auc_mix+=auc
    auc_mix=(0.1)*auc_mix
    auc_mix=pd.Series(auc_mix,index=methods+(list(range(1,12))))
    auc_mix.name='auc'    
    return auc_mix

       
