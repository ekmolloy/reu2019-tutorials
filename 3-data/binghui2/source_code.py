import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import string
import seaborn as sns
from pylab import plot, show, savefig, xlim, figure, \
                hold, ylim, legend, boxplot, setp, axes
df1 = pd.read_csv("Desktop/data-species-trees.csv")
df2 = pd.read_csv("Desktop/data-compare-timings.csv")
ax = axes()
hold(True)

plt.subplot(2, 4, 1)
plt.title("100 taxa, 25 intron")
outfileNJ = df1[(df1[u"NTAX"]==100) & (df1[u"NGEN"]==75) &(df1[u"DATA"]=="intron") & (df1[u"TRLN"]=="500K") & (df1[u"MTHD"] == "NJMerge(ASTRAL,AGID)")&(df1["SERF"].values < 1)]
outfileAS = df1[(df1[u"NTAX"]==100) & (df1[u"NGEN"]==75) &(df1[u"DATA"]=="intron") & (df1[u"TRLN"]=="500K") & (df1[u"MTHD"] == "ASTRAL")&(df1["SERF"].values < 1)]
outfile1NJ = df1[(df1[u"NTAX"]==100) & (df1[u"NGEN"]==75) &(df1[u"DATA"]=="intron") & (df1[u"TRLN"]=="10M") & (df1[u"MTHD"] == "NJMerge(ASTRAL,AGID)")&(df1["SERF"].values < 1)]
outfile1AS = df1[(df1[u"NTAX"]==100) & (df1[u"NGEN"]==75) &(df1[u"DATA"]=="intron") & (df1[u"TRLN"]=="10M") & (df1[u"MTHD"] == "ASTRAL")&(df1["SERF"].values < 1)]
B = [outfile1NJ["SERF"],outfile1AS["SERF"],outfileNJ["SERF"],outfileAS["SERF"]]
bp = plt.boxplot(B, patch_artist=True ,positions = [1,2,3,4], widths = 0.6)
plt.ylabel("Species Tree Error")
colors = ['blue', 'orange', 'blue','orange']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)


plt.subplot(2, 4, 2)
plt.title("100 taxa, 100 intron")
outfile2NJ = df1[(df1[u"NTAX"]==100) & (df1[u"NGEN"]==300) &(df1[u"DATA"]=="intron") & (df1[u"TRLN"]=="500K") & (df1[u"MTHD"] == "NJMerge(ASTRAL,AGID)")&(df1["SERF"].values < 1)]
outfile2AS = df1[(df1[u"NTAX"]==100) & (df1[u"NGEN"]==300) &(df1[u"DATA"]=="intron") & (df1[u"TRLN"]=="500K") & (df1[u"MTHD"] == "ASTRAL")&(df1["SERF"].values < 1)]
outfile3NJ = df1[(df1[u"NTAX"]==100) & (df1[u"NGEN"]==300) &(df1[u"DATA"]=="intron") & (df1[u"TRLN"]=="10M") & (df1[u"MTHD"] == "NJMerge(ASTRAL,AGID)")&(df1["SERF"].values < 1)]
outfile3AS = df1[(df1[u"NTAX"]==100) & (df1[u"NGEN"]==300) &(df1[u"DATA"]=="intron") & (df1[u"TRLN"]=="10M") & (df1[u"MTHD"] == "ASTRAL")&(isinstance(df1["SERF"].values,float) < 1)]
B1 = [outfile3NJ["SERF"],outfile3AS["SERF"],outfile2NJ["SERF"],outfile2AS["SERF"]]
bp = plt.boxplot(B1, patch_artist=True,positions = [5,6,7,8], widths = 0.6)
colors = ['blue', 'orange', 'blue','orange']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

plt.subplot(2, 4, 3)
plt.title("100 taxa, 1000 intron")
outfile4NJ = df1[(df1[u"NTAX"]==100) & (df1[u"NGEN"]==3000) &(df1[u"DATA"]=="intron") & (df1[u"TRLN"]=="500K") & (df1[u"MTHD"] == "NJMerge(ASTRAL,AGID)")&(df1["SERF"].values < 1)]
outfile4AS = df1[(df1[u"NTAX"]==100) & (df1[u"NGEN"]==3000) &(df1[u"DATA"]=="intron") & (df1[u"TRLN"]=="500K") & (df1[u"MTHD"] == "ASTRAL")&(df1["SERF"].values < 1)]
outfile5NJ = df1[(df1[u"NTAX"]==100) & (df1[u"NGEN"]==3000) &(df1[u"DATA"]=="intron") & (df1[u"TRLN"]=="10M") & (df1[u"MTHD"] == "NJMerge(ASTRAL,AGID)")&(df1["SERF"].values < 1)]
outfile5AS = df1[(df1[u"NTAX"]==100) & (df1[u"NGEN"]==3000) &(df1[u"DATA"]=="intron") & (df1[u"TRLN"]=="10M") & (df1[u"MTHD"] == "ASTRAL")&(isinstance(df1["SERF"].values,float) < 1)]
B2 = [outfile5NJ["SERF"],outfile5AS["SERF"],outfile4NJ["SERF"],outfile4AS["SERF"]]
bp = plt.boxplot(B2, patch_artist=True,positions = [9,10,11,12], widths = 0.6)
colors = ['blue', 'orange', 'blue','orange']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)


plt.subplot(2, 4, 4)
plt.title("1000 taxa,1000 intron")
outfile6NJ = df1[(df1[u"NTAX"]==1000) & (df1[u"NGEN"]==3000) &(df1[u"DATA"]=="intron") & (df1[u"TRLN"]=="500K") & (df1[u"MTHD"] == "NJMerge(ASTRAL,AGID)")&(df1["SERF"].values < 1)]
outfile6AS = df1[(df1[u"NTAX"]==1000) & (df1[u"NGEN"]==3000) &(df1[u"DATA"]=="intron") & (df1[u"TRLN"]=="500K") & (df1[u"MTHD"] == "ASTRAL")&(df1["SERF"].values < 1)]
outfile7NJ = df1[(df1[u"NTAX"]==1000) & (df1[u"NGEN"]==3000) &(df1[u"DATA"]=="intron") & (df1[u"TRLN"]=="10M") & (df1[u"MTHD"] == "NJMerge(ASTRAL,AGID)")&(df1["SERF"].values < 1)]
outfile7AS = df1[(df1[u"NTAX"]==1000) & (df1[u"NGEN"]==3000) &(df1[u"DATA"]=="intron") & (df1[u"TRLN"]=="10M") & (df1[u"MTHD"] == "ASTRAL")&(isinstance(df1["SERF"].values,float) < 1)]
B3 = [outfile7NJ["SERF"],outfile7AS["SERF"],outfile6NJ["SERF"],outfile6AS["SERF"]]
bp = plt.boxplot(B3, patch_artist=True ,positions = [13,14,15,16], widths = 0.6)
colors = ['blue', 'orange', 'blue','orange']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    
    
    
    
plt.subplot(2, 4, 5)
# set height of bar
outfileNJ = df2[(df2[u"NTAX"]==100) & (df2[u"NGEN"]==75) &(df2[u"DATA"]=="intron") & ((df2[u"MTHD"] == "NJMerge(ASTRAL,AGID)-Serial") | (df2[u"MTHD"] == "ASTRAL"))]
sns.set(style="whitegrid")
#tips = sns.load_dataset("tips")
sns.barplot(x="TRLN",y="SECS",hue="MTHD" ,data=outfileNJ)
plt.subplot(2, 4, 6)
outfile1NJ = df2[(df2[u"NTAX"]==100) & (df2[u"NGEN"]==300) &(df2[u"DATA"]=="intron") & ((df2[u"MTHD"] == "NJMerge(ASTRAL,AGID)-Serial") | (df2[u"MTHD"] == "ASTRAL"))]
sns.barplot(x="TRLN",y="SECS",hue="MTHD" ,data=outfile1NJ)
plt.subplot(2, 4, 7)
outfile1NJ = df2[(df2[u"NTAX"]==100) & (df2[u"NGEN"]==3000) &(df2[u"DATA"]=="intron") & ((df2[u"MTHD"] == "NJMerge(ASTRAL,AGID)-Serial") | (df2[u"MTHD"] == "ASTRAL"))]
sns.barplot(x="TRLN",y="SECS",hue="MTHD" ,data=outfile1NJ)
plt.subplot(2, 4, 8)
outfile1NJ = df2[(df2[u"NTAX"]==1000) & (df2[u"NGEN"]==3000) &(df2[u"DATA"]=="intron") & ((df2[u"MTHD"] == "NJMerge(ASTRAL,AGID)-Serial") | (df2[u"MTHD"] == "ASTRAL"))]
sns.barplot(x="TRLN",y="SECS",hue="MTHD" ,data=outfile1NJ)


plt.subplots_adjust(bottom=-0.5, top=1.5, left=-0.9, right=1.9)
