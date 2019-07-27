import glob
import seaborn as sns
import matplotlib.pyplot as plt

def make_box_plot():

    source = "./output/raxml_out/Scincella/*.phylip"

    num_seq = []
    algn_len = []

    for f in glob.glob(source):

        con = open(f, 'r')

        a,b = con.readline().split(" ")
        num_seq.append(int(a))
        algn_len.append(int(b))

    sns.set_style("whitegrid")
    plt.figure(1)
    sns.boxplot(data=num_seq, orient="h")
    plt.xlabel("Number of sequences")
    plt.yticks([""])
    plt.figure(2)
    sns.boxplot(data=algn_len, orient="h")
    plt.xlabel("Length of sequence alignments")
    plt.yticks([""])
    plt.show()

make_box_plot()