import os
import sys
import numpy as np

directory = sys.argv[1]

repnums = []

for f in os.listdir(os.fsencode(directory)):
    f=f.decode('UTF-8')
    if f.endswith("est.m"):
        repnums.append(f[:-6])

for repnum in repnums:
    original = np.array([s.split() for s in open(directory+str(repnum) + "_or.m", 'r')])
    estimated = np.array([s.split() for s in open(directory+str(repnum) + "_est.m", 'r')])
    o_cols = original[:,0]
    est_cols = estimated[:,0]
    
    for row in range(len(original)):
        for col in range(2+row,len(original[0])):
            o_rowname=original[row, 0]
            o_colname=o_cols[col-1]
            e_rownum=np.where(est_cols == o_rowname)[0][0]
            e_colnum=np.where(est_cols == o_colname)[0][0] + 1
            print(o_rowname+","+ o_colname+","+original[row,col]+","+estimated[e_rownum,e_colnum])
