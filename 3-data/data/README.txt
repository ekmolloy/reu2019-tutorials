This folder contains CSV files for making graphs and tables.


* data-species-trees.csv = contains species tree estimation error for different methods and model conditions
    + MODL = model condition specified by number of taxa and number of genes (e.g., 100tax+75gen means 100 taxa and 75 genes)
    + NTAX = number of taxa
             + 100
             + 1000
    + NGEN = number of genes
             + 75 = 25 exons, 25 introns, 25 UCEs; only exons and introns were analyzed (separately) in this study
             + 300 = 100 exons, 100 introns, 100 UCEs; only exons and introns were analyzed (separately) in this study
             + 3000 = 1000 exons, 1000 introns, 1000 UCEs; only exons and introns were analyzed (separately) in this study
    + TRLN = species tree length
             + 10M = low/moderate ILS
             + 500K = very high ILS
    + REPL = replicate number
             + 1 through 20
    + DATA = sequence data type
             + exon
             + intron
    + MTHD = species tree estimation method
             + NJ(AGID) = NJ given average gene tree internode distance (AGID) matrix
             + NJ(log-det) = NJ given log-det distance matrix
             + ASTRAL = ASTRAL-III
             + NJMerge(ASTRAL,AGID) = NJMerge given ASTRAL-III constraint trees and AGID matrix
             + NJMerge(ASTRAL,log-det) = NJMerge given ASTRAL-III constraint trees and log-det distance matrix
             + SVDquartets
             + NJMerge(SVDquartets,AGID) = NJMerge given SVDquartets constraint trees and AGID matrix
             + NJMerge(SVDquartets,log-det) = NJMerge given SVDquartets constraint trees and log-det distance matrix
             + RAxML
             + NJMerge(RAxML,AGID) = NJMerge given RAxML constraint trees and AGID matrix
             + NJMerge(RAxML,log-det) = NJMerge given RAxML constraint trees and log-det distance matrix
             + NJMerge(True,AGID) = NJMerge given constraint trees derived from true species tree and AGID matrix
             + NJMerge(True,log-det) = NJMerge given constraint trees derived from true species tree and log-det distance matrix
    + SMAX = maximum number of leaves in subset (NA if not NJMerge)
             + 30 for NJMerge on 100-taxon datasets
             + 120 for NJMerge on 1000-taxon datasets
             + NA for methods not NJMerge
    + SE_NL = number of leaves in both the true and the estimated species trees
    + SE_I1 = number of internal branches in the true species tree
    + SE_I2 = number of internal branches in the estimated species tree
    + SE_FP = number of false positive branches between the true and the estimated species trees
    + SE_FN = number of false negative branches between the true and the estimated species trees
    + SE_RF = normalized Robinson-Foulds (RF) distance between the true and the estimated species trees


* data-compare-timings.csv = contains running time (in seconds) for different methods and model conditions
    + MTHD = As described above but note that NJMerge methods include the flags “-Serial” or “-Parallel” for Equations 1 or 2 in the main text, respectively
    + SECS = running time in seconds


* data-constraint-trees-w-agid.csv = contains species tree error between the subset (or constraint) trees (computed for the NJMerge pipeline using AGID distance matrix) and the true species tree
    + ISUB = constraint tree number
    + NSUB = number of constraint trees


* data-constraint-trees-w-logdet.csv = contains species tree error between the subset (or constraint) trees (computed for the NJMerge pipeline using log-det distance matrix) and the true species tree


* data-gene-trees.csv = contains information about each gene tree
    + GENE = gene number
             + 1 through 1000
    + AD_NL = number of leaves in both the true species tree and the true gene tree
    + AD_I1 = number of internal branches in the true species tree
    + AD_I2 = number of internal branches in the true gene tree
    + AD_FP = number of false positive branches between the true species tree and the true gene tree
    + AD_FN = number of false negative branches between the true species tree and the true gene tree
    + AD_RF = normalized Robinson-Foulds (RF) distance between the true species tree and the true gene tree
    + GE_NL = number of leaves in both the true and the estimated gene tree
    + GE_I1 = number of internal branches in the true gene tree
    + GE_I2 = number of internal branches in the estimated gene tree
    + GE_FP = number of false positive branches between the true and the estimated gene trees
    + GE_FN = number of false negative branches between the true and the estimated gene trees
    + GE_RF = normalized Robinson-Foulds (RF) distance between the true and the estimated gene trees
    + TD_NL = number of leaves in both the true species tree and the estimated gene tree
    + TD_I1 = number of internal branches in the true species tree
    + TD_I2 = number of internal branches in the estimated gene tree
    + TD_FP = number of false positive branches between the true species tree and the estimated gene tree
    + TD_FN = number of false negative branches between the true species tree and the estimated gene tree
    + TD_RF = normalized Robinson-Foulds (RF) distance between the true species tree and the estimated gene tree


* data-verify-njmerge-w-agid.csv = contains tree error between subset (or constraint) trees and NJMerge tree for NJMerge pipeline using AGID distance matrix


* data-verify-njmerge-w-logdet.csv = contains tree error between subset (or constraint) trees and NJMerge tree for NJMerge pipeline using log-det distance matrix