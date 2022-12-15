import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# from tkinter import messagebox
import os

def pcontour(x,y,z):
    plt.figure()
    plt.contourf(x,y,z)
    plt.show()

    n = np.meshgrid(x,y)
    dt = pd.DataFrame(columns=['X','Y','I'])
    # messagebox.showinfo('z',z)
    for i in range(len(x)):
        for j in range(len(y)):
            # print("x:",n[0][i][j],'; y:',n[1][i][j],';z:',z[i][j])
            dt = dt.append({'X':n[0][i][j],'Y':n[1][i][j],'I':z[i][j]},ignore_index=True)

    curdir = os.getcwd().encode('utf-8').decode('utf-8')
    dt.to_csv(curdir+'data.csv')

    

# pcontour([1,2,3],[1,2,3],[[1,1,1],[1,3,1],[1,1,1]])