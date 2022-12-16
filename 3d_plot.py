import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import time
# from tkinter import messagebox

def pcontour(x,y,z):
    plt.figure()
    plt.contourf(x,y,z)
    plt.show()

    n = np.meshgrid(x,y)
    dt = pd.DataFrame(columns=['X(mm)','Y(mm)','I(pA)'])
    # messagebox.showinfo('z',z)
    for i in range(len(x)):
        for j in range(len(y)):
            # print("x:",n[0][i][j],'; y:',n[1][i][j],';z:',z[i][j])
            tmps = pd.Series({'X(mm)':n[0][i][j],'Y(mm)':n[1][i][j],'I(pA)':z[i][j]})
            tmpdf = tmps.to_frame()
            tmp = pd.DataFrame(tmpdf.values.T, columns=tmps.index)
            dt = pd.concat([dt,tmp],ignore_index=False)
    
    wdir = 'D:\\Github\\Motor_ctrl\\data\\'
    path = wdir+'DATA'+time.strftime("-%Y_%m_%d %H_%M_%S", time.localtime())+'.csv'

    dt.to_csv(path ,index=False)

    

    

# pcontour([1,2,3],[1,2,3],[[1,1,1],[1,3,1],[1,1,1]])