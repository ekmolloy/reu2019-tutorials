import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import sys

df = pd.read_csv(sys.argv[1])
df["MULT"]=df["MULT"].str.replace('-', '.', regex=False)

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6, 6))

axes.set_title("100M3 RF rates")
f=sns.boxplot(x="MULT", y="RF", data=df, ax=axes, width=.4, flierprops={"marker":"o"})

plt.savefig("boxplot.png")
plt.savefig("boxplot.pdf")
