# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:29:13 2017

@author: mong
"""

import numpy as np
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

data=[[0.787,0.631,0.523,0.436,0.360,0.293,0.231,0.174,0.121,0.071,0.023],
      [0.087,0.285,0.065,0.282,0.552,0.161,0.454,0.788,0.280,0.634,0.044],
      [0.126,0.084,0.412,0.282,0.087,0.546,0.314,0.038,0.599,0.296,0.933]]

test= np.array(data).reshape(11,3)

def mixture_index_1(MatrixAdjacency_Train):
    sim_1=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.Katz.Katz(MatrixAdjacency_Train)
    sim_3=similarity_indicators.RA.RA(MatrixAdjacency_Train)
    Matrix_similarity=test[0][0]*sim_1+test[0][1]*sim_2+test[0][2]*sim_3
    return Matrix_similarity

def mixture_index_2(MatrixAdjacency_Train):
    sim_1=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.Katz.Katz(MatrixAdjacency_Train)
    sim_3=similarity_indicators.RA.RA(MatrixAdjacency_Train)
    Matrix_similarity=test[1][0]*sim_1+test[1][1]*sim_2+test[1][2]*sim_3
    return Matrix_similarity

def mixture_index_3(MatrixAdjacency_Train):
    sim_1=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.Katz.Katz(MatrixAdjacency_Train)
    sim_3=similarity_indicators.RA.RA(MatrixAdjacency_Train)
    Matrix_similarity=test[2][0]*sim_1+test[2][1]*sim_2+test[2][2]*sim_3
    return Matrix_similarity

def mixture_index_4(MatrixAdjacency_Train):
    sim_1=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.Katz.Katz(MatrixAdjacency_Train)
    sim_3=similarity_indicators.RA.RA(MatrixAdjacency_Train)
    Matrix_similarity=test[3][0]*sim_1+test[3][1]*sim_2+test[3][2]*sim_3
    return Matrix_similarity

def mixture_index_5(MatrixAdjacency_Train):
    sim_1=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.Katz.Katz(MatrixAdjacency_Train)
    sim_3=similarity_indicators.RA.RA(MatrixAdjacency_Train)
    Matrix_similarity=test[4][0]*sim_1+test[4][1]*sim_2+test[4][2]*sim_3
    return Matrix_similarity

def mixture_index_6(MatrixAdjacency_Train):
    sim_1=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.Katz.Katz(MatrixAdjacency_Train)
    sim_3=similarity_indicators.RA.RA(MatrixAdjacency_Train)
    Matrix_similarity=test[5][0]*sim_1+test[5][1]*sim_2+test[5][2]*sim_3
    return Matrix_similarity

def mixture_index_7(MatrixAdjacency_Train):
    sim_1=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.Katz.Katz(MatrixAdjacency_Train)
    sim_3=similarity_indicators.RA.RA(MatrixAdjacency_Train)
    Matrix_similarity=test[6][0]*sim_1+test[6][1]*sim_2+test[6][2]*sim_3
    return Matrix_similarity

def mixture_index_8(MatrixAdjacency_Train):
    sim_1=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.Katz.Katz(MatrixAdjacency_Train)
    sim_3=similarity_indicators.RA.RA(MatrixAdjacency_Train)
    Matrix_similarity=test[7][0]*sim_1+test[7][1]*sim_2+test[7][2]*sim_3
    return Matrix_similarity

def mixture_index_9(MatrixAdjacency_Train):
    sim_1=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.Katz.Katz(MatrixAdjacency_Train)
    sim_3=similarity_indicators.RA.RA(MatrixAdjacency_Train)
    Matrix_similarity=test[8][0]*sim_1+test[8][1]*sim_2+test[8][2]*sim_3
    return Matrix_similarity

def mixture_index_10(MatrixAdjacency_Train):
    sim_1=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.Katz.Katz(MatrixAdjacency_Train)
    sim_3=similarity_indicators.RA.RA(MatrixAdjacency_Train)
    Matrix_similarity=test[9][0]*sim_1+test[9][1]*sim_2+test[9][2]*sim_3
    return Matrix_similarity

def mixture_index_11(MatrixAdjacency_Train):
    sim_1=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.Katz.Katz(MatrixAdjacency_Train)
    sim_3=similarity_indicators.RA.RA(MatrixAdjacency_Train)
    Matrix_similarity=test[10][0]*sim_1+test[10][1]*sim_2+test[10][2]*sim_3
    return Matrix_similarity






