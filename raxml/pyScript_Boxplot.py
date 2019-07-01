import matplotlib.pyplot as plt
%matplotlib inline
import pandas as pd
import numpy as np
df = pd.read_csv("Desktop/boxplot.txt")
plt.subplot(1, 2, 1)
plt.boxplot(df["mean"], labels=["means"])
plt.title("Box plot of means of all matrices")
plt.subplot(1, 2, 2)
plt.boxplot(df["median"], labels=["medians"])
plt.title("Box plot of medians of all matrices")
plt.subplots_adjust(bottom=0, top=1, left=-0.5, right=1.5)
