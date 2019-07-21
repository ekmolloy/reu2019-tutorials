import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def make_plot():

    data = pd.read_csv("./fastme.csv")

    sns.boxplot(y='RF', x='REPL', data=data).set(xlabel="100M3 model Replicates", ylabel="RF error distribution")
    plt.show()


make_plot()