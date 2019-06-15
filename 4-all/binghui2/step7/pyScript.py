import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import string
import seaborn as sns
import math
from pylab import plot, show, savefig, xlim, figure, \
                hold, ylim, legend, boxplot, setp, axes
df1 = pd.read_csv("Desktop/comparison.csv")


plt.subplot(2, 3, 1)
plt.title("factor = 1.0")
red = df1[( pd.isna(df1[u"TRUE_DPTH"]) ) & (df1[u"MULT"]==1)]
black = df1[( pd.isna(df1[u"TRUE_DPTH"]) == False ) & (df1[u"MULT"]==1)]
plt.scatter(red["ESTI_LNTH"],red["ESTI_DPTH"],c="r")
plt.scatter(black["ESTI_LNTH"],black["ESTI_DPTH"],c="black")

plt.subplot(2, 3, 2)
plt.title("factor = 0.1")
red1 = df1[(pd.isna(df1[u"TRUE_DPTH"])) & (df1[u"MULT"]==0.1)]
#print(red1)
black1 = df1[( pd.isna(df1[u"TRUE_DPTH"]) == False ) & (df1[u"MULT"]==0.1)]

plt.scatter(red1["ESTI_LNTH"],red1["ESTI_DPTH"],c="r")
plt.scatter(black1["ESTI_LNTH"],black1["ESTI_DPTH"],c="black")

plt.subplot(2, 3, 3)
plt.title("factor = 0.05")
red2 = df1[(pd.isna(df1[u"TRUE_DPTH"])) & (df1[u"MULT"]==0.05)]
#print(red1)
black2 = df1[( pd.isna(df1[u"TRUE_DPTH"]) == False ) & (df1[u"MULT"]==0.05)]

plt.scatter(red2["ESTI_LNTH"],red2["ESTI_DPTH"],c="r")
plt.scatter(black2["ESTI_LNTH"],black2["ESTI_DPTH"],c="black")

plt.subplot(2, 3, 4)
plt.title("factor = 0.01")
red3 = df1[(pd.isna(df1[u"TRUE_DPTH"])) & (df1[u"MULT"]==0.01)]
#print(red1)
black3 = df1[( pd.isna(df1[u"TRUE_DPTH"]) == False ) & (df1[u"MULT"]==0.01)]

plt.scatter(red3["ESTI_LNTH"],red3["ESTI_DPTH"],c="r")
plt.scatter(black3["ESTI_LNTH"],black3["ESTI_DPTH"],c="black")

plt.subplot(2, 3, 5)
plt.title("factor = 0.005")
red4 = df1[(pd.isna(df1[u"TRUE_DPTH"])) & (df1[u"MULT"]==0.005)]
#print(red1)
black4 = df1[( pd.isna(df1[u"TRUE_DPTH"]) == False ) & (df1[u"MULT"]==0.005)]

plt.scatter(red4["ESTI_LNTH"],red4["ESTI_DPTH"],c="r")
plt.scatter(black4["ESTI_LNTH"],black4["ESTI_DPTH"],c="black")

plt.subplot(2, 3, 6)
plt.title("factor = 0.001")
red5 = df1[(pd.isna(df1[u"TRUE_DPTH"])) & (df1[u"MULT"]==0.001)]
#print(red1)
black5 = df1[( pd.isna(df1[u"TRUE_DPTH"]) == False ) & (df1[u"MULT"]==0.001)]

plt.scatter(red5["ESTI_LNTH"],red5["ESTI_DPTH"],c="r")
plt.scatter(black5["ESTI_LNTH"],black5["ESTI_DPTH"],c="black")

plt.subplots_adjust(bottom=-0.5, top=1.5, left=-0.9, right=1.9)
