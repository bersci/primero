# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 22:48:20 2020

@author: SOSAMSUNG
"""

import random
import matplotlib.pyplot as plt
import numpy as np

X_0 = np.array([[0],[0]])
#¿Delta es avance aleatorío para caminar?
delta_X = np.random.normal(0,50,(2,10))
#la escala
#variable x a partir de X_0
X=np.concatenate((X_0,np.cumsum(delta_X,axis=1)),axis=1)
#dibuja el avance
rw = plt.plot(X[0],X[1],"ro-")
plt.savefig('camborr.jpg')