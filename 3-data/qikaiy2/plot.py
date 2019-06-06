import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats
import seaborn as sns

df1 = pd.read_csv("../data/data-species-trees.csv")
df2 = pd.read_csv("../data/data-compare-timings.csv")
dic1 = {0:75, 1:300, 2:3000, 3:3000}
dic2 = {0:100, 1:100, 2:100, 3:1000}
dic3 = {0:"100tax, 25intro",1:"100tax, 100intro",2:"100tax, 1000intro",3:"1000tax, 1000intro"}

for i in range(4):
    ax = plt.subplot(2,4,i+1)
    if(i==0):
        ax.set_ylabel("Error Rate")
    err1 = (df1[(df1["NTAX"]==dic2[i]) & (df1["NGEN"] == dic1[i]) & (df1["DATA"] == "intron") \
         & (df1["TRLN"] == "10M") & (df1["MTHD"] == "ASTRAL")]["SERF"]).values
    
    err2 = (df1[(df1["NTAX"]==dic2[i]) & (df1["NGEN"] == dic1[i]) & (df1["DATA"] == "intron") \
         & (df1["TRLN"] == "10M") & (df1["MTHD"] == "NJMerge(ASTRAL,AGID)")]["SERF"]).values

    err3 = (df1[(df1["NTAX"]==dic2[i]) & (df1["NGEN"] == dic1[i]) & (df1["DATA"] == "intron") \
         & (df1["TRLN"] == "500K") & (df1["MTHD"] == "ASTRAL")]["SERF"]).values
    err3 = np.delete(err3,np.where(np.isnan(err3))[0],axis=0)
    err4 = (df1[(df1["NTAX"]==dic2[i]) & (df1["NGEN"] == dic1[i]) & (df1["DATA"] == "intron") \
         & (df1["TRLN"] == "500K") & (df1["MTHD"] == "NJMerge(ASTRAL,AGID)")]["SERF"]).values
    data_ = [err1,err2,err3,err4]
    plt.boxplot(data_)
    ax.set_title(dic3[i])

df2["SECS"] = df2["SECS"]/60

for i in range(4):
    ax = plt.subplot(2,4,i+5)
    df2 = df2.rename(columns={'SECS':'Running Time'})
    time = (df2[(df1["NTAX"]==dic2[i]) & (df2["NGEN"] == dic1[i]) & (df2["DATA"] == "intron") \
     & ((df2["MTHD"] == "NJMerge(ASTRAL,AGID)-Serial") | (df2["MTHD"] == "ASTRAL"))])
    sns.barplot(x="TRLN", y="Running Time", hue="MTHD", data=time)
plt.show()
