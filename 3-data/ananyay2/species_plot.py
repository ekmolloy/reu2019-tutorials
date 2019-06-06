import pandas as pd
import matplotlib
import numpy as np

import sys

df = pd.read_csv(sys.argv[1])

print(df.columns)

first_plot=df.loc[(df["NTAX"] == 100) & (df["NGEN"] == 75) & (df["TRLN"] == "10M")]

print(type(first_plot))

first_boxplot=first_plot.boxplot(column=["ASTRAL", "NJMerge(ASTRAL,AGID)"], by=["SERF"])

