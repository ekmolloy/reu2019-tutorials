import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats
import seaborn as sns

colors = ['pink', 'lightblue', 'lightgreen', 'blue', 'green']

figure,axes=plt.subplots()
df = pd.read_csv("../step4/step4.csv")
data = np.zeros((6,5))
dic = [1.0,0.1,0.05,0.01,0.005,0.001]
for i in range(6):
    temp = df[df["MULT"]==dic[i]]["RF"].values
    for j in range(len(temp)):
        data[i][j] = temp[j]
print(data)
bplot = axes.boxplot(data.T,  patch_artist=True)
axes.yaxis.grid(True)  #在y轴上添加网格线
for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)  #加颜色
plt.xlabel("Different Scaling Factors for Branches")
plt.ylabel("Accuracy")  
plt.title("Accuracy on The Dataset with Different Scaling Factors")
#改坐标参数
plt.setp(axes,xticks=[1,2,3,4,5,6],\
        xticklabels=['Factor=1', 'Factor=0.1', 'Factor=0.05', 'Factor=0.01', 'Factor=0.005', 'Factor=0.001'])
plt.show()
