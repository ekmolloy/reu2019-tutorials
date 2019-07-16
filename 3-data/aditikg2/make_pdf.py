import pandas as pd
import math
import numpy as np

def make_pdf():

# Get the data into a suitable form

    # Get data from csv file
    data = pd.read_csv("../data/data-species-trees.csv")

    na = data.loc[pd.isna(data["SENL"]) & pd.isna(data["SEI1"]) & pd.isna(data["SEI2"]) & pd.isna(data["SEFP"]) & pd.isna(data["SEFN"]) & pd.isna(data["SERF"]),
                  ["REPL", "NTAX", "NGEN", "TRLN", "DATA", "MTHD"]]

    # n_100_25 = data.loc[(data["MODL"] == "100tax+75gen"), ["REPL"]].max()
    # n_100_100 = data.loc[(data["MODL"] == "100tax+300gen"), ["REPL"]].max()
    # n_100_1000 = data.loc[(data["MODL"] == "100tax+3000gen"), ["REPL"]].max()
    # n_1000_1000 = data.loc[(data["MODL"] == "1000tax+3000gen"), ["REPL"]].max()

    k = na.groupby(["NTAX", "NGEN", "TRLN", "DATA", "MTHD"])

# Write a LaTeX document

    # Create a document
    f = open("Err_table.tex", "w+")

    # The basics of a LaTeX pdf
    f.write("\documentclass{article}\n")
    f.write("\\begin{document}\n\n")

    # Make the table
    f.write("\\noindent\makebox[\\textwidth]{%\n")
    f.write("\\begin{tabular}{ |p{0.1\linewidth}|p{0.1\linewidth}|p{0.1\linewidth}|p{0.1\linewidth}|p{0.4\linewidth}|p{0.1\linewidth}|p{0.2\linewidth}| }\n")

    f.write("\t\hline\n")
    f.write("\t\# of Taxa & \# of Genes & Species Tree Height & Data Type & Method & Fraction of Replicates & Replicate Numbers \\\\\n")
    f.write("\t\hline\n")

    for name, group in k:
        for i in range(5):

            if i == 1:
                f.write(str(int(name[i])/3))
            else:
                f.write(str(name[i]))

            f.write(" & ")

        f.write(str(len(group["REPL"])) + "/20 & ")
        n = 0

        if len(group["REPL"]) <= 18:
            n = len(group["REPL"])
            k = 0
            for i in group["REPL"]:
                f.write(str(i))
                k = k + 1
                if not k == n:
                    f.write(", ")
        elif len(group["REPL"]) == 20:
                f.write("All")
        elif len(group["REPL"]) == 19:
                f.write("All except ")
                f.write(str(find_missing_num(group["REPL"], 20)))

        f.write(" \\\\\n")

    f.write("\t\hline\n")

    f.write("\end{tabular}}\n")

    f.write("\end{document}")

def find_missing_num(g, tot):

    sum = 0

    for i in g:
        sum = sum + int(i)

    lit_sum = int(tot * (tot + 1)/2)

    return lit_sum - sum

make_pdf()