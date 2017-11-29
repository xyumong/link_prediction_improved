# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 09:00:56 2017

@author: mong
"""

import linkprediction
import mix

NetFile = 'PB.txt'
NetName = 'PB'


auc_val=linkprediction.cross_validation(NetFile,NetName)
auc_val.sort_values()

auc_mix=mix.cross_validation(NetFile,NetName)
auc_mix.sort_values()

