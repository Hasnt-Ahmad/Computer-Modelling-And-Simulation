import random
from math import sin
from math import pi
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

x_cord=[]
y_cord=[]
listx=[]
listcount=[]
N=1000
def plot(x_cord,y_cord):
    x = np.arange(1.5,1*np.pi,0.1)  
    y = np.sin(x**2)
    plt.plot(x_cord,y_cord,x,y,'')
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.show()
def check(x,y):
    value=sin(x**2)
    if(y<value):
        x_cord.append(x)
        y_cord.append(y)
        listcount.append(1)
        
    
    
def dots(u_x_bound,l_x_bound,u_y_bound,l_y_bound):
    list=[]
    x=(random.uniform(l_x_bound,u_x_bound))
    y=(random.uniform(l_y_bound,u_y_bound));
    check(x,y)
    listx.append(x)
    return 

def mean_std(N):
    list1=[]
    list2=[]
    mean=0
    std=0
    for i in range(0,N):
        dots(2.5,2,-1,0)
        mean+=listx[i]
        list1.append(listx[i])
    for i in range(0,N):
        dots(3,2.5,1,0)
        mean+=listx[i]
        list1.append(listx[i])
    for i in list1:
        std+=(i-mean)**2
    std=(1/N)*std
    std=sqrt(std)
    list2.append(mean)
    list2.append(std)

    return list2
print("Mean And Std = ",mean_std(N))
count=0
for i in listcount:
    count+=1
print("Area= ",(count/N)*pi)
plot(x_cord,y_cord)