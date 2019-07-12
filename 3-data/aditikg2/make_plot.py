import pandas as pd
import matplotlib.pyplot as plt
import sys

def make_box_plot():

    data = pd.read_csv("../data/data-species-trees.csv")

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)
    print(data.ndim)
    #for i in range(data.ndim):
        
        #if data["N"]:
        

make_box_plot()
