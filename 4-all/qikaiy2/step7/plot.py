import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats
import seaborn as sns

df = pd.read_csv("../step6/step6.csv")
dic = [1, 0.1, 0.05, 0.01, 0.005, 0.001]
labels = ["correct nodes", "wrong nodes"]
for i in range(6):
    ax = plt.subplot(1,6,i+1)
    ax.set_title("MULT = " + str(dic[i]))
    x1 = df[df["MULT"]==dic[i]]["ESTI_LNTH"].values
    x2 = df[df["MULT"]==dic[i]]["TRUE_LNTH"].values
    y1 = df[df["MULT"]==dic[i]]["ESTI_DEPTH"].values
    y2 = df[df["MULT"]==dic[i]]["TRUE_DPTH"].values
    black_x = []
    black_y = []
    red_x = []
    red_y = [] 
    judge = np.isnan(x2)
    for i in range(len(judge)):
        if(judge[i] == True):
           black_x.append(x1[i])
           black_y.append(y1[i])
        else:
           red_x.append(x1[i])
           red_y.append(y1[i])
    plt.scatter(black_x,black_y,c='k')
    plt.scatter(red_x,red_y,c='r')
    plt.legend(labels)
    plt.xlabel("Edge Length")
    plt.ylabel("Node Depth")
plt.show()