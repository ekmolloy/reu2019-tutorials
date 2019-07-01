import os
import sys
import numpy as np

directory = sys.argv[1]

repnums = []

for f in os.listdir(os.fsencode(directory)):
    filename = os.fsendcode(f)
    if filename.endswith("est.m"):
        repnums.append(filename[:-6])

for repnum in repnums:
    original = [s.strip() for s in open(str(repnum) + "_or.m", 'r')]
    estimated = [s.strip() for s in open(str(repnum) + "_est.m", 'r')]
    o_cols = original[:,0]
    est_cols = estimated[:,0]
    print(o_cols)
    print(est_cols)
    print(original)
    print(estimated)
    
    for row in range(len(original)):
        for col in range(2+row,len(original[0])):
            o_rowname=original[row, 0]
            o_colname=o_cols[col-1,0]
            e_rownum=est_cols.index(o_rowname)
            e_colnum=est_cols.index(o_colname) + 1
            print(o_rowname+","+ o_colname+","+original[row,col]+","+estimated[e_rownum,e_colnum])

