import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats
import seaborn as sns
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("address", type=str, help="tabelfile")
args = parser.parse_args()

df = pd.read_csv(args.address)
method = list(set(df["MTHD"]))
taxgene = list(set(df["MODL"]))
NAMES = ["# of Taxa", "# of Genes", "Species Tree Height", "Data Type", \
 "Method", "Fraction of Replicates", "Replicates numbers"]
need = {"100tax+75gen": \
          {"exon":{"500K":["NJMerge(True,log-det)","NJMerge(RAxML,AGID)"]}, \
           "intron":{"500K":["NJMerge(True,AGID)"]}}, \
        "1000tax+3000gen": \
          {"intron":{"10M":["NJMerge(ASTRAL,log-det)","SVDquartets","RAxML"], \
                     "500K":["ASTRAL","NJMerge(SVDquartets,log-det)","SVDquartets","RAxML"]}, \
            "exon":{"10M":["SVDquartets", "RAxML"],\
                    "500K":["ASTRAL","NJMerge(SVDquartets,log-det)","NJMerge(RAxML,log-det)", \
                    "NJMerge(True,log-det)","NJMerge(ASTRAL,log-det)","SVDquartets"]}}} 
DATA = ["exon", "intro"]
dic = {"NTAX":"# of Taxa", "NGEN":"# of Genes", "TRLN":"Species Tree Height", "DATA":"Data Type", \
 "MTHD":"Method", "REPL":"Replicates numbers"}
data_ = [[],[],[],[],[],[],[]]

def get_data(taxgene_, mthd_, data_, trln_):
    df1 = df[(df["MODL"]==taxgene_) & (df["MTHD"]==mthd_) & (df["DATA"]==data_) & (df["TRLN"]==trln_)]
    temp = df1["SERF"].values
    count = 0
    fail = []
    success = []
    for i in range(len(temp)):
        if(temp[i]>=0 and temp[i]<=1):
            count += 1
            success.append(i+1)
        else:
            fail.append(i+1)
    #print(count, fail, success)
    if(count >= 10):
        if(count == 20):
            return "0/20","None"
        else:
            tail = ""
            for i in fail:
                tail = tail + str(i) + " "
            return str(20-count)+"/20", tail     
    else:   
        if(count == 0):
            return "20/20","All"
        else:
            tail = ""
            for i in success:
                tail = tail + str(i) +" "
            return str(20-count)+"/20", "All except " + tail

for tax_gene in need:
    for type_ in need[tax_gene]:
        for length_ in need[tax_gene][type_]:
            for m in need[tax_gene][type_][length_]:
                x,y = get_data(tax_gene, m, type_,length_)
                data_[0].append(list(set(df[df["MODL"]==tax_gene]["NTAX"]))[0])
                data_[1].append(list(set(df[df["MODL"]==tax_gene]["NGEN"]))[0])
                data_[2].append(length_)
                data_[3].append(type_)
                data_[4].append(m)
                data_[5].append(x)
                data_[6].append(y)
result_df = pd.DataFrame(list(map(list, zip(*data_))), columns = NAMES)
print(result_df.to_latex(index=False))

#y = get_data(taxgene[0], "NJMerge(ASTRAL,AGID)", "intron", "500K")