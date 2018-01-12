from numpy import *
import numpy as np

x=np.matrix(np.array([[1,4.50],[2,4.75],[3,4.91]]))
sum=0
ave=[0,0,0,0]

for i in range(3):
    sum=sum+x[i,1];
for i in range(2):
    sum1=0
    sum2=0
    ave1=0
    ave2=0
    for j in range(i+1):
        sum1=sum1+x[j,1]
    sum2=sum-sum1
    e1=sum1/(i+1)
    e2=sum2/(3-i-1)
    for m in range(i+1):
        ave1=ave1+(x[m,1]-e1)*(x[m,1]-e1)
    for n in range(3-i-1):
        ave2=ave2+(x[i+1+n,1]-e2)*(x[i+1+n,1]-e2)
    ave[i]=ave1+ave2;
    print(e1,e2)
    print(ave1,ave2)

for i in range(2):
    print(ave[i]);
    
