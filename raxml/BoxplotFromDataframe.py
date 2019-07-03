
# coding: utf-8

# In[47]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import scipy.stats as stats
for num in range(37):
        
    df = pd.read_csv("Desktop/matrix_diff/box%s.csv"%(num))
    #print(df)
    plt.figure()
    index = 0
    if num == 36:
        B = 14*[None]
        for row in df.iterrows():
            numArr = np.zeros(30)
            for i in range(30):
                numArr[i] = (row[1][i+1])
            B[index] = numArr
            index += 1
        bp = plt.boxplot(B, patch_artist=True ,positions = range(14), widths = 0.4)
        plt.ylabel("average sequence estimation error")
        colors = ['blue']*14
    elif num == 16:
        B = 19*[None]
        for row in df.iterrows():
            numArr = np.zeros(30)
            for i in range(30):
                numArr[i] = (row[1][i+1])
            B[index] = numArr
            index += 1
        bp = plt.boxplot(B, patch_artist=True ,positions = range(19), widths = 0.4)
        plt.ylabel("average sequence estimation error")
        colors = ['blue']*19
    else:
        B = 20*[None]
        for row in df.iterrows():
            numArr = np.zeros(30)
            for i in range(30):
                numArr[i] = (row[1][i+1])
            B[index] = numArr
            index += 1
        bp = plt.boxplot(B, patch_artist=True ,positions = range(20), widths = 0.4)
        plt.ylabel("average sequence estimation error")
        colors = ['blue']*20
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
    plt.savefig('Desktop/tempres/box%s.png'%(num))

