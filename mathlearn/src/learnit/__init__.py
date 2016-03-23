#coding:utf-8
'''
@author: Zoe
function:利用matplotlib快速绘图函数库画函数图像
'''
import math
import numpy as np
import matplotlib.pyplot as plt
from lib2to3.pgen2.token import COLON

if __name__ == "__main__":
    #每隔0.05个单位描一个点
    x = np.arange(0.05,3,0.05)
    
    y1 = [math.log(a,1.5) for a in x]
    plt.plot(x,y1,linewidth=2,color='#007500',label='log1.5(x)')
    
    plt.plot([1,1],[y1[0],y1[-1]],"r--",linewidth=2)
    
    #log(a,b) a是对数的数字，b是对数的底
    y2 = [math.log(a,2) for a in x]
    plt.plot(x,y2,linewidth=2,color='#9F35FF',label='log2(x)')
    
    y3 = [math.log(a,3) for a in x]
    plt.plot(x,y3,linewidth=2,color='#F75000',label='log3(x)')
    
    #图示legend函数显示
    plt.legend(loc='center right')
    
    #plt.xlabel(x)
    #plt.ylabel(x)
    
    plt.grid(True)
    plt.show()

