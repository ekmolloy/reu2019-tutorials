import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_table('./output/heat_plot_out/Scincella/SELT_matrix.mat', delimiter=" ", skiprows=1, header=None, skipinitialspace=True, index_col=False)
k = data.drop(data.shape[1] - 1, 1)
k = k.drop(0, 1)

heat_map = sb.heatmap(k, cmap="YlGnBu", cbar_kws={'label': 'p-distance between sequences'}, xticklabels=data[0], yticklabels=data[0])
plt.xlabel("Scincella lateralis individuals")
plt.ylabel("Scincella lateralis individuals")
plt.savefig("./output/heat_plot_out/Scincella/heat_plot_SELT.pdf", tight_layout=True, format='pdf', dpi=300)

