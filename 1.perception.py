from numpy import *
import numpy as np

x=np.matrix(np.array([[0,0,0],[1,0,0],[1,0,1],[1,1,0],[0,0,1],[0,1,1],[0,1,0],[1,1,1]]))
y=np.matrix(np.array([[1],[1],[1],[1],[-1],[-1],[-1],[-1]]))
n=1
b=0
w=np.matrix(np.array([[0],[0],[0]]))
count=8;
while count!=0:
    count=8;
    for i in range(8):
         if(y[i,0]*(w[0,0]*x[i,0]+w[1,0]*x[i,1]+w[2,0]*x[i,2]+b)<=0):
            w=w+(n*y[i,0]*x[i,:]).T
            b=b+n*y[i,0]
            print(i);
         else:
            count-=1;
print(w)    
print(b)