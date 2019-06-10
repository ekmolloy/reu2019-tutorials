import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import sys

df_st = pd.read_csv("../data/data-species-trees.csv")
df_rt = pd.read_csv("../data/data-compare-timings.csv")

df_rt["MINS"] = df_rt["SECS"] / 60

def get_data(df, ntax, ngen, trln, mthd):
    frame=df.loc[(df["NTAX"] == ntax) & (df["NGEN"] == ngen) & (df["TRLN"] == trln) \
                  & (df["MTHD"] == mthd)].reset_index()
    frame=frame.drop(columns=["index"]).rename(index=str, columns={"MTHD":"Method"})
    return frame

fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(12, 6))

axes[0,0].set_title("100 taxa, 25 introns")
axes[0,1].set_title("100 taxa, 100 introns")
axes[0,2].set_title("100 taxa, 1000 introns")
axes[0,3].set_title("1000 taxa, 1000 introns")

# we"re dealing with 100-25 rn
def make_boxplot(ax, ntaxa, nintrons):
    ngen=nintrons*3
    
    astral_l = get_data(df_st, ntaxa, ngen, "10M", "ASTRAL")
    nj_l = get_data(df_st, ntaxa, ngen, "10M", "NJMerge(ASTRAL,AGID)")

    astral_h = get_data(df_st, ntaxa, ngen, "500K", "ASTRAL")
    nj_h = get_data(df_st, ntaxa, ngen, "500K", "NJMerge(ASTRAL,AGID)")

    df_fig = pd.concat([astral_l, astral_h, nj_h, nj_l], ignore_index=True)

    f=sns.boxplot(x="TRLN", y="SERF", hue="Method", data=df_fig, ax=ax, width=.4, flierprops={"marker":"o"})
    f.legend_.remove()
    f.set(xlabel="", ylabel= ("Species Tree Error" if ax==axes[0,0] else ""))
    
def make_barchart(ax, ntaxa, nintrons):
    ngen=nintrons * 3
    
    astral_l = get_data(df_rt, ntaxa, ngen, "10M", "ASTRAL")
    nj_lp = get_data(df_rt, ntaxa, ngen, "10M", "NJMerge(ASTRAL,AGID)-Parallel")
    nj_ls = get_data(df_rt, ntaxa, ngen, "10M", "NJMerge(ASTRAL,AGID)-Serial")

    astral_h = get_data(df_rt, ntaxa, ngen, "500K", "ASTRAL")
    nj_hp = get_data(df_rt, ntaxa, ngen, "500K", "NJMerge(ASTRAL,AGID)-Parallel")
    nj_hs = get_data(df_rt, ntaxa, ngen, "500K", "NJMerge(ASTRAL,AGID)-Serial")

    df_fig = pd.concat([astral_l, astral_h, nj_lp, nj_ls, nj_hp, nj_hs], ignore_index=True)
    
    # rename all the NJMerge things be just 'NJMerge'
    df_fig["Method"] = df_fig["Method"].replace(["NJMerge(ASTRAL,AGID)-Parallel", "NJMerge(ASTRAL,AGID)-Serial"], "NJMerge(ASTRAL,AGID)")
        
    f = sns.barplot(x="TRLN", y="MINS", hue="Method", data=df_fig, ax=ax)
    f.legend_.remove()
    f.set(xlabel="", ylabel=("Running Time (m)" if ax==axes[1,0] else ""))
    

make_boxplot(axes[0, 0], 100, 25)
make_boxplot(axes[0, 1], 100, 100)
make_boxplot(axes[0, 2], 100, 1000)
make_boxplot(axes[0, 3], 1000, 1000)

make_barchart(axes[1, 0], 100, 25)
make_barchart(axes[1, 1], 100, 100)
make_barchart(axes[1, 2], 100, 1000)
make_barchart(axes[1, 3], 1000, 1000)

plt.savefig("fig1.png")
