#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 13:02:14 2017

@author: ruobingwang
"""

import pandas as pd

def toCAMEO(namelist):
    codebook=pd.read_csv('countrycode.csv')
    result=[]
    for e in namelist:
        try:
            result.append(codebook[codebook['Country']==e]['Code'].values[0])
        except:
            pass
    return result

            