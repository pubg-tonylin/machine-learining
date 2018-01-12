import numpy as np 
import math

A=np.matrix(np.array([[0.5,0.1,0.4],[0.3,0.5,0.2],[0.2,0.2,0.6]]))
B=np.matrix(np.array([[0.5,0.5],[0.4,0.6],[0.7,0.3]]))

t=np.matrix(np.array([[0.2],[0.3],[0.5]]))

a=np.matrix(np.zeros((5,3)))
b=np.matrix(np.zeros((5,3)))
for i in range(3):
    a[0,i]=t[i,0]*B[i,0]
    print(a[0,i])
for i in range(3):
    a[1,i]=(a[0,0]*A[0,i]+a[0,1]*A[1,i]+a[0,2]*A[2,i])*B[i,1]
    print(a[1,i])
for i in range(3):
    a[2,i]=(a[1,0]*A[0,i]+a[1,1]*A[1,i]+a[1,2]*A[2,i])*B[i,0]
    print(a[2,i])
for i in range(3):
    a[3,i]=(a[2,0]*A[0,i]+a[2,1]*A[1,i]+a[2,2]*A[2,i])*B[i,0]
    print(a[3,i])
for i in range(3):
    a[4,i]=(a[3,0]*A[0,i]+a[3,1]*A[1,i]+a[3,2]*A[2,i])*B[i,1]
    print(a[4,i])

for i in range(3):
    b[0,i]=1
    print(b[0,i])
for i in range(3):
    b[1,i]=A[i,0]*B[0,1]*b[0,0]+A[i,1]*B[1,1]*b[0,1]+A[i,2]*B[2,1]*b[0,2]
    print(b[1,i])
for i in range(3):
    b[2,i]=A[i,0]*B[0,1]*b[1,0]+A[i,1]*B[1,1]*b[1,1]+A[i,2]*B[2,1]*b[1,2]
    print(b[2,i])
for i in range(3):
    b[3,i]=A[i,0]*B[0,0]*b[2,0]+A[i,1]*B[1,0]*b[2,1]+A[i,2]*B[2,0]*b[2,2]
    print(b[3,i])
for i in range(3):
    b[4,i]=A[i,0]*B[0,1]*b[3,0]+A[i,1]*B[1,1]*b[3,1]+A[i,2]*B[2,1]*b[3,2]
    print(b[4,i])

print('结果为')

p=(a[4,2]*b[3,2])/(a[4,0]*b[3,0]+a[4,1]*b[3,1]+a[4,2]*b[3,2])
print(p)
