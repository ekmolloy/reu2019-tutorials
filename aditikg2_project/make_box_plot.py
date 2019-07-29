import glob
import seaborn as sns
import matplotlib.pyplot as plt

def make_box_plot():

    source = "./output/raxml_out/Scincella/*.phylip"
    source2 = "./output/raxml_out/Scincella/*.log"

    num_seq = []
    algn_len = []
    gaps = []

    for f in glob.glob(source):

        con = open(f, 'r')

        a,b = con.readline().split(" ")
        num_seq.append(int(a))
        algn_len.append(int(b))

    for f in glob.glob(source2):

        con = open(f, 'r')

        lines = con.readlines()

        for line in lines:

            if "Gaps:" in line:
                a,b,c = line.split(" ")
                gaps.append(float(b)*100)
                break

    sns.set_style("whitegrid")
    plt.figure(1)
    sns.boxplot(data=num_seq, orient="h")
    plt.xlabel("Number of sequences")
    plt.yticks([""])
    plt.savefig("./output/data_info_out/Scincella/num_seq.pdf", tight_layout=True, format='pdf', dpi=300)
    plt.figure(2)
    sns.boxplot(data=algn_len, orient="h")
    plt.xlabel("Length of sequence alignments")
    plt.yticks([""])
    plt.savefig("./output/data_info_out/Scincella/len_algn.pdf", tight_layout=True, format='pdf', dpi=300)
    plt.figure(3)
    sns.boxplot(data=gaps, orient="h")
    plt.xlabel("Percent gaps in data")
    plt.yticks([" "])
    plt.savefig("./output/data_info_out/Scincella/gaps.pdf", tight_layout=True, format='pdf', dpi=300)
    plt.show()

make_box_plot()