import numpy as np 
import math

def get_e(w,g_m,y):
    e=[]
    for i in range(len(g_m)):
        e.append(0)
        for j in range(len(g_m[i])):
            if(g_m[i][j]!=y[j]):
                e[i]+=w[j]
        e[i]=round(e[i],2)
    return e

def sign(f):
    if(f>=0):
        return 1
    else:
        return -1 

#基本分类器Gm
def getGm(x,y):
    g_m=[[],[],[],[],[],[],[],[]]
    v=[0,1,0,1,2,0,1,2]
    for j in range(len(x[0])):
        if(x[0][j]<=v[0]):
            g_m[0].append(-1)
        else:
            g_m[0].append(1)
    for j in range(len(x[0])):
        if(x[0][j]<=v[1]):
            g_m[1].append(-1)
        else:
            g_m[1].append(1)
    for j in range(len(x[1])):
        if(x[1][j]<=v[2]):
            g_m[2].append(1)
        else:
            g_m[2].append(-1)
    for j in range(len(x[1])):
        if(x[1][j]<=v[3]):
            g_m[3].append(1)
        else:
            g_m[3].append(-1)
    for j in range(len(x[1])):
        if(x[1][j]<=v[4]):
            g_m[4].append(1)
        else:
            g_m[4].append(-1)
    for j in range(len(x[2])):
        if(x[2][j]<=v[5]):
            g_m[5].append(1)
        else:
            g_m[5].append(-1)
    for j in range(len(x[2])):
        if(x[2][j]<=v[6]):
            g_m[6].append(1)
        else:
            g_m[6].append(-1)
    for j in range(len(x[2])):
        if(x[2][j]<=v[7]):
            g_m[7].append(1)
        else:
            g_m[7].append(-1)
    return g_m   

def G(x,y,d,g_m,e,a,z,f,m):
    e=get_e(d[m],g_m,y)
    print('错误率e=',e)
    n=e.index(min(e))
    print('g_m取：g_m[%d]'%n)
    a.append(0)
    a[m]=round(0.5*math.log((1-e[n])/e[n]),8)
    i=int((n+1)/3)
    #print(i)
    d.append([])
    z_m=0
    for j in range(len(x[i])):
        z_m+=(d[m][j]*math.exp(-a[m]*y[j]*g_m[n][j]))
    z.append(round(z_m,8))
    for j in range(len(x[i])):
        d[m+1].append(round((d[m][j]/z[m])*math.exp(-a[m]*y[j]*g_m[n][j]),8))
    f.append([])
    for j in range(len(x[i])):
        f[m].append(g_m[n][j]*a[m])
    '''
    print(n,g_m[n])
    print(i,x[i])
    print('f=',f)
    '''
    #print('a=',a)
    ee=0
    
    for j in range(len(x[0])):
        e_r=0
        for k in range(len(f)):
            e_r+=f[k][j]
        e_r=sign(e_r)
        print(e_r,end=' ')
        if(e_r==y[j]):
            ee+=1/len(y)
    ee=round(ee,2)
    print(ee)
    return d,ee,a
    
if __name__ == '__main__':
    if(1):
        x=[[0,0,1,1,1,0,1,1,1,0],[1,3,2,1,2,1,1,1,3,2],[3,1,2,3,3,2,2,1,1,1]]
        y=[-1,-1,-1,-1,-1,-1,1,1,-1,-1]
        d0=[[]]
        for i in range(len(y)):
            d0[0].append(1/len(y)) 
        d=d0
        g_m=getGm(x,y)
        e=[];a=[]
        z=[]
        f=[]
        m=0
    ee=0
    while(ee!=1):
        print('第%d步'%(m+1))
        d,ee,a=G(x,y,d,g_m,e,a,z,f,m)
        m+=1
    print(a)

    
    



