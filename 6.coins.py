from numpy import *
import numpy as np

y=[1,1,0,1,0,0,1,0,1,1]
u=[0,0,0,0,0,0,0,0,0,0] 
t=0.4
p=0.6
q=0.7
for m in range(4):
    sum=0
    mul=0
    lsum=0
    lmul=0
    for i in range(10):
        u[i]=(t*pow(p,y[i])*pow(1-p,1-y[i]))/((t*pow(p,y[i])*pow(1-p,1-y[i]))+(1-t)*pow(q,y[i])*pow(1-q,1-y[i]))
        sum=sum+u[i]
        mul=mul+u[i]*y[i]
        lmul=lmul+(1-u[i])*y[i]
        lsum=lsum+(1-u[i]);
    t=sum/10
    p=mul/sum
    q=lmul/lsum
    print(t,p,q);

    