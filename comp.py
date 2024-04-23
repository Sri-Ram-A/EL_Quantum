import cmath
import numpy as np
import math as m
if __name__=='__main__':
    #BASIC GATES
    def X():
        np.array([[0  ,1],
                [1  ,0]])
    def Y():
        np.array([[0  ,-1j],
                [1j  ,0]])
    def Z():
        np.array([[1  ,0],
                [0  ,-1]])
    def H():      
        s=2**0.5
        np.array([[1/s   ,1/s], 
                [1/s  ,-1/s]])
    #ROTATIONAL GATES
    p=int()
    def RX():
        np.array([[m.cos(p/2)        ,-1j*(m.sin(p/2))],
                [-1j*(m.sin(p/2))  ,m.cos(p/2)]])  
    def RY():
        np.array([[m.cos(p/2)  ,m.sin(-p/2)],
                [m.sin(p/2)  ,m.cos(+p/2)]])   
    def RX():
        np.array([[m.exp(-1j*p/2),                0],
                [0,                m.exp(-1j*p/2)]]) 
    #P GATE
    def P():
        np.array([[1,           0],
                [0,m.exp(p*1j)]])
    #SQUARE ROOT GATE
    def SR():
        np.array([[(1-1j)/2     ,(1+1j)/2],
                [(1+1j)/2     ,(1-1j)/2]])   
    #HERMITIAN CONJUGATES
    def St():
        np.array([[1,   0],
                [0, -1j]])
    def Tt():
        np.array([[1,   0],
                [0,   m.exp(-1j*m.pi/4)]])
    def SRt():
        np.array([[(1+1j)/2     ,(1-1j)/2],
              [(1-1j)/2     ,(1+1j)/2]])      
