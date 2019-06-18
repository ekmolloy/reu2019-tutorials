import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import sys

scales=[1.0, 0.1, 0.05, 0.01, 0.005, 0.001]
colors=sns.dark_palette("red", n_colors=2)

df = pd.read_csv(sys.argv[1])
df["MULT"]=df["MULT"].str.replace('-', '.', regex=False)

fig, axes = plt.subplots(nrows=1, ncols=len(scales)+1, figsize=(10*(len(scales)+1),10))

def get_data(df, modl, repl, mult):
    frame = df.loc[(df["MODL"] == modl) & \
                   (df["REPL"] == repl) & \
                   (df["MULT"] == str(mult))].reset_index()
    frame["COLR"] = (frame["TRUE_LNTH"].isnull()).astype(int)
    return frame

def make_scatterplot(ax, df, modl, repls, scales, legend=False):
    frames = []
    for s in scales:
        for r in repls:
            frames.append(get_data(df, modl, r, s))
    
    df_fig = pd.concat(frames, ignore_index=True)
    
    f = sns.scatterplot(x="ESTI_LNTH", y="ESTI_DPTH", hue="COLR", \
                        palette=colors, data=df_fig, ax=ax, legend=legend)


def make_plots(axes, df, modl, repls, scales):
    for i in range(len(axes)):
        if i == len(axes) - 1:
            # make plot
            make_scatterplot(axes[i], df, modl, repls, scales, legend="full")
            
            # deal with title
            axes[i].set_title("All scales")
            
            # deal with legend
            h, l = axes[i].get_legend_handles_labels()
            axes[i].legend((h[0], h[1], h[2]), ("Legend", "In true tree", "Not in true tree"))
        else:
            # make plot
            make_scatterplot(axes[i], df, modl, repls, [scales[i]])
            
            # deal with title
            axes[i].set_title("Scale: %s"%str(scales[i]))
        
        # y axis label
        if i != 0:
            axes[i].set_ylabel("")
        else:
            axes[i].set_ylabel("Estimated Depth")
        
        # x axis label
        axes[i].set_xlabel("Estimated Length")

        
make_plots(axes, df, "100M3", ["R0", "R1", "R2", "R3", "R4"], scales)
plt.savefig("scatterplots.png")
plt.savefig("scatterplots.pdf")
