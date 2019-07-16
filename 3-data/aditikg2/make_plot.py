import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

def make_box_plot():

    data = pd.read_csv("../data/data-species-trees.csv")
    timings = pd.read_csv("../data/data-compare-timings.csv")

    fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4)

    astral_e = {}
    njmerge_e = {}
    astral_t = {}
    njmerge_t = {}

    for i in range(data.shape[0]):

        if data["DATA"][i] == "intron" and not math.isnan(float(data["SERF"][i])):

            if data["MODL"][i] not in astral_e:
                astral_e[data["MODL"][i]] = [[], []]

            if data["MODL"][i] not in njmerge_e:
                njmerge_e[data["MODL"][i]] = [[], []]

            if data["MTHD"][i] == "ASTRAL":
                if data["TRLN"][i] == "500K":
                    astral_e[data["MODL"][i]][0].append(data["SERF"][i])
                elif data["TRLN"][i] == "10M":
                    astral_e[data["MODL"][i]][1].append(data["SERF"][i])

            if "NJMerge" and "AGID" and "ASTRAL" in data["MTHD"][i]:
                if data["TRLN"][i] == "500K":
                    njmerge_e[data["MODL"][i]][0].append(data["SERF"][i])
                if data["TRLN"][i] == "10M":
                    njmerge_e[data["MODL"][i]][1].append(data["SERF"][i])

    for i in range(timings.shape[0]):

        if timings["DATA"][i] == "intron" and not math.isnan(float(timings["SECS"][i])):

            if timings["MODL"][i] not in astral_t:
                astral_t[timings["MODL"][i]] = [[], []]

            if timings["MODL"][i] not in njmerge_t:
                njmerge_t[timings["MODL"][i]] = [[], []]

            if timings["MTHD"][i] == "ASTRAL":
                if timings["TRLN"][i] == "500K":
                    astral_t[timings["MODL"][i]][0].append(float(timings["SECS"][i]/60))
                elif timings["TRLN"][i] == "10M":
                    astral_t[timings["MODL"][i]][1].append(float(timings["SECS"][i]/60))

            if "NJMerge" and "AGID" and "ASTRAL" in timings["MTHD"][i]:
                if timings["TRLN"][i] == "500K":
                    njmerge_t[timings["MODL"][i]][0].append(float(timings["SECS"][i]/60))
                if timings["TRLN"][i] == "10M":
                    njmerge_t[timings["MODL"][i]][1].append(float(timings["SECS"][i]/60))

    l1 = ["ASTRAL-III"]*2
    l2 = ["NJMerge"]*2

    ax1.set_title("100 Taxa, 25 introns")
    str1 = "100tax+75gen"
    ax1.boxplot([astral_e[str1][0], astral_e[str1][1], njmerge_e[str1][0], njmerge_e[str1][1]], positions=[1, 4, 2, 5])

    ax2.set_title("100 Taxa, 100 introns")
    str2 = "100tax+300gen"
    ax2.boxplot([astral_e[str2][0], astral_e[str2][1], njmerge_e[str2][0], njmerge_e[str2][1]], positions=[1, 4, 2, 5])

    ax3.set_title("100 Taxa, 1000 introns")
    str3 = "100tax+3000gen"
    ax3.boxplot([astral_e[str3][0], astral_e[str3][1], njmerge_e[str3][0], njmerge_e[str3][1]], positions=[1, 4, 2, 5])

    ax4.set_title("1000 Taxa, 1000 introns")
    str4 = "1000tax+3000gen"
    ax4.boxplot([astral_e[str4][0], astral_e[str4][1], njmerge_e[str4][0], njmerge_e[str4][1]], positions=[1, 4, 2, 5])

    mean_as = [[np.mean(astral_t[str1][0]), np.mean(astral_t[str1][1])],
               [np.mean(astral_t[str2][0]), np.mean(astral_t[str2][1])],
               [np.mean(astral_t[str3][0]), np.mean(astral_t[str3][1])],
               [np.mean(astral_t[str4][0]), np.mean(astral_t[str4][1])]]
    mean_nj = [[np.mean(njmerge_t[str1][0]), np.mean(njmerge_t[str1][1])],
               [np.mean(njmerge_t[str2][0]), np.mean(njmerge_t[str2][1])],
               [np.mean(njmerge_t[str3][0]), np.mean(njmerge_t[str3][1])],
               [np.mean(njmerge_t[str4][0]), np.mean(njmerge_t[str4][1])]]
    std_as = [[np.std(astral_t[str1][0]), np.std(astral_t[str1][1])],
               [np.std(astral_t[str2][0]), np.std(astral_t[str2][1])],
               [np.std(astral_t[str3][0]), np.std(astral_t[str3][1])],
               [np.std(astral_t[str4][0]), np.std(astral_t[str4][1])]]
    std_nj = [[np.std(njmerge_t[str1][0]), np.std(njmerge_t[str1][1])],
               [np.std(njmerge_t[str2][0]), np.std(njmerge_t[str2][1])],
               [np.std(njmerge_t[str3][0]), np.std(njmerge_t[str3][1])],
               [np.std(njmerge_t[str4][0]), np.std(njmerge_t[str4][1])]]

    num = np.arange(2)
    wid = 0.35
    label = ("Low/mod ILS", "Very high ILS")

    plt.ylabel(["Sp", "r"])

    l1 = ax5.bar(num,
            mean_as[0],
            yerr=std_as[0],
            width=wid,
            label=l1[0])
    l2 = ax5.bar(num + wid,
            mean_nj[0],
            yerr=std_nj[0],
            width=wid,
            label=l2[0])
    plt.sca(ax5)
    plt.xticks(num + wid,
               label)
    plt.ylim(bottom=0)

    ax6.bar(num,
            mean_as[1],
            yerr=std_as[1],
            width=wid,
            label=l1[0])
    ax6.bar(num + wid,
            mean_nj[1],
            yerr=std_nj[1],
            width=wid,
            label=l2[0])
    plt.sca(ax6)
    plt.xticks(num + wid,
               label)
    plt.ylim(bottom=0)

    ax7.bar(num,
            mean_as[2],
            yerr=std_as[2],
            width=wid,
            label=l1[0])
    ax7.bar(num + wid,
            mean_nj[2],
            yerr=std_nj[2],
            width=wid,
            label=l2[0])
    plt.sca(ax7)
    plt.xticks(num + wid,
               label)
    plt.ylim(bottom=0)

    ax8.bar(num,
            mean_as[3],
            yerr=std_as[3],
            width=wid,
            label=l1[0])
    ax8.bar(num + wid,
            mean_nj[3],
            yerr=std_nj[3],
            width=wid,
            label=l2[0])
    plt.sca(ax8)
    plt.xticks(num + wid,
               label)
    plt.ylim(bottom=0)

    fig.legend((l1, l2), ("ASTRAL-III", "NJMerge"), loc=8)
    plt.show()

make_box_plot()