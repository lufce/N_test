'''
Created on 2016/11/23

@author: Harusame
'''

import numpy as np
import matplotlib.pyplot as plt
from numba.tests.npyufunc.test_ufunc import dtype

print("start")

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([1, 1])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.4, 0.4])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 1
    else:
        return 0

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    return AND(s1, s2)

def step_function(x):
    return np.array(x > 0, dtype=np.int)

def sigmoid(x):
    return 1 / (1 + np.exp( -x ))

def ReLU(x):
    return x.maximum(0, x)

x = np.arange(-5,5,0.1)
y = sigmoid(x)
plt.plot(x,y)
plt.ylim(-0.1, 1.1)
plt.show()

'''
print(XOR(0,0))
print(XOR(1,0))
print(XOR(0,1))
print(XOR(1,1))
'''