import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import plot, show, savefig, xlim, figure, \
                hold, ylim, legend, boxplot, setp, axes

 
df1 = pd.read_csv("../step4/fastme.csv")
plt.subplot(2, 3, 1)
plt.title("branch length*1.0")
outfileNJ = df1[(df1[u"MULT"]==1)]
bp = plt.boxplot(outfileNJ["RF"],widths = 0.6)
plt.subplot(2, 3, 2)
plt.title("branch length*0.1")
outfile1NJ = df1[(df1[u"MULT"]==0.1)]
bp = plt.boxplot(outfile1NJ["RF"],widths = 0.6)
plt.subplot(2, 3, 3)
plt.title("branch length*0.05")
outfile2NJ = df1[(df1[u"MULT"]==0.05)]
bp = plt.boxplot(outfile2NJ["RF"],widths = 0.6)
plt.subplot(2, 3, 4)
plt.title("branch length*0.01")
outfile3NJ = df1[(df1[u"MULT"]==0.01)]
bp = plt.boxplot(outfile3NJ["RF"],widths = 0.6)
plt.subplot(2, 3, 5)
plt.title("branch length*0.005")
outfile4NJ = df1[(df1[u"MULT"]==0.005)]
bp = plt.boxplot(outfile4NJ["RF"],widths = 0.6)
plt.subplot(2, 3, 6)
plt.title("branch length*0.001")
outfile5NJ = df1[(df1[u"MULT"]==0.001)]
bp = plt.boxplot(outfile5NJ["RF"],widths = 0.6)
plt.subplots_adjust(bottom=-0.5, top=1.5, left=-0.6, right=1.6)
plt.savefig('boxplots.png')

