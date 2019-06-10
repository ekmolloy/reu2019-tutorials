import pandas as pd

tg = [(100, 25), (100, 100), (100, 1000), (1000, 1000)]
methods = ["NJ(AGID)", "NJ(log-det)", "ASTRAL", "NJMerge(ASTRAL,AGID)", \
           "NJMerge(ASTRAL,log-det)", "SVDquartets", "NJMerge(SVDquartets,AGID)", \
           "NJMerge(SVDquartets,log-det)", "RAxML", "NJMerge(RAxML,AGID)", \
           "NJMerge(RAxML,log-det)", "NJMerge(True,AGID)", "NJMerge(True,log-det)"]
mthd_latex = {
    "NJ(AGID)" : "NJ($\\mathcal{D}_{AGID})",
    "NJ(log-det)" : "NJ($\\mathcal{D}_{LD}",
    "ASTRAL" : "ASTRAL-III",
    "NJMerge(ASTRAL,AGID)" : "NJMerge($\\mathcal{T}_{AST}, \\mathcal{D}_{AGID}$)", 
    "NJMerge(ASTRAL,log-det)" : "NJMerge($\\mathcal{T}_{AST}, \\mathcal{D}_{LD}$)", 
    "SVDquartets" : "SVDquartets", 
    "NJMerge(SVDquartets,AGID)" : "NJMerge($\\mathcal{T}_{SVD}, \\mathcal{D}_{AGID}$)", 
    "NJMerge(SVDquartets,log-det)" : "NJMerge($\\mathcal{T}_{SVD}, \\mathcal{D}_{LD}$)", 
    "RAxML" : "RAxML", 
    "NJMerge(RAxML,AGID)" : "NJMerge($\\mathcal{T}_{RAX}, \\mathcal{D}_{AGID}$)", 
    "NJMerge(RAxML,log-det)" : "NJMerge($\\mathcal{T}_{RAX}, \\mathcal{D}_{LD}$)", 
    "NJMerge(True,AGID)" : "NJMerge($\\mathcal{T}_{true}, \\mathcal{D}_{AGID}$)", 
    "NJMerge(True,log-det)" :"NJMerge($\\mathcal{T}_{true}, \\mathcal{D}_{LD}$)"
}

def make_intro(f):
    f.write("\\documentclass{article}\n")
    f.write("\\usepackage{booktabs}\n")
    f.write("\\usepackage[margin=1in]{geometry}")
    f.write("\\begin{document}\n")
    f.write("\\begin{table}[h!]\n")
    f.write("\\begin{center}\n")
    f.write("\\caption{Insert description of the table here.}\n")
    f.write("\\begin{tabular}{cccccrl}\n")
    f.write("\\toprule\n")
    f.write("\\# of     & \\# of     & Species Tree  & Data  & Method    & Fraction of   & Replicate\\\\\n")
    f.write("Taxa      & Genes     & Height        & Type  &           & Replicates    & Numbers\\\\\n")
    f.write("\\midrule\n")

def make_ending(f):
    f.write("\\bottomrule\n")
    f.write("\\end{tabular}\n")
    f.write("\\end{center}\n")
    f.write("\\end{table}\n")
    f.write("\\end{document}\n")

def get_data(df, ntaxa, ngenes, nht, dtype, mthd):
    return df.loc[(df["NTAX"] == ntaxa) & (df["NGEN"] == 3 * ngenes) & (df["TRLN"] == nht) \
                  & (df["DATA"] == dtype) & (df["MTHD"] == mthd)].reset_index()
    
def tex_string(ntaxa, ngenes, nht, dtype, mthd, nreps, ntotalreps, repnums):
    if(repnums.size == 20):
        # this is an "all" case
        repnumstring="All"
    elif(repnums.size >= 10): 
        # this is an "all except" case
        repnumstring = "All except "
        for i in range(1, 21):
            if not i in set(repnums):
                repnumstring += str(i) + ", "
        repnumstring = repnumstring[:-2]
    elif(repnums.size > 0):
        repnumstring = ""
        for i in repnums:
            repnumstring += str(i) + ", "
        repnumstring = repnumstring[:-2]
    else:
        None
    sand = " & "
    return str(ntaxa) + sand + str(ngenes) + sand + str(nht) + sand + dtype + \
        sand + mthd_latex[mthd] + sand + "$" + str(nreps) + "\\backslash" + str(ntotalreps) + \
            "$" + sand + repnumstring + "\\\\\n"
    
def make_middle(df, f):
    tg = [(100, 25), (100, 100), (100, 1000), (1000, 1000)]
    
    invalids = df.loc[df["SERF"].isnull()]
    combos=[(g[0], g[1], trln, dtype, mthd) for g in tg for trln in ["10M", "500K"] for dtype in ["exon", "intron"] \
     for mthd in methods]
    
    for c in combos:
        dat = get_data(df, c[0], c[1], c[2], c[3], c[4])
        inv_dat = get_data(invalids, c[0], c[1], c[2], c[3], c[4])
        if(len(inv_dat.index) > 0):
            f.write(tex_string(c[0], c[1], c[2], c[3], c[4], len(inv_dat.index), len(dat.index), inv_dat["REPL"]))
       
    
    
    
df = pd.read_csv("../data/data-species-trees.csv")

file = open("latexfile.tex", "w")
make_intro(file)
make_middle(df, file)
make_ending(file)
file.close()