mport matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import string
import seaborn as sns
df = pd.read_csv("all_RF_Distance.csv")
plt.title("RF distances of between the estimated sequence and true sequence")
plt.ylabel("RF-distance")
plt.boxplot(df["RF-distance"], patch_artist=True, widths = 0.6)
plt.figure()
