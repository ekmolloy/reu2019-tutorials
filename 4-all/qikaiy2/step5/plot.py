import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats
import seaborn as sns

df = pd.read_csv("../step4/step4.csv")
data = np.zeros((6,5))
dic = [1.0,0.1,0.05,0.01,0.005,0.001]
for i in range(6):
    temp = df[df["MULT"]==dic[i]]["RF"].values
    for j in range(len(temp)):
        data[i][j] = temp[j]
print(data)
plt.boxplot(data.T)
plt.xlabel("Different Factors (from big to small)")
plt.ylabel("Accuracy")
plt.show()
