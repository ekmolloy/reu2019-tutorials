import sys
import dendropy
import numpy as np

def compare_msa(path1, path2):

    msa1 = dendropy.DnaCharacterMatrix.get(file=open(path1), schema="nexus")
    msa2 = dendropy.DnaCharacterMatrix.get(file=open(path2), schema="phylip")

    diff = []
    
    for i in range(len(msa1)):
        temp = 0
        
        for j in range(len(msa1[i])):
            if not msa1[i][j] == msa2[i][j]:
                temp = temp + 1

            #if i == 0:
                #print(msa1[i][j])
                #print(msa2[i][j])
                #print("\n")

        diff.append(float(float(temp)/len(msa1[i])))

        #if i == 0:
            #print(msa1[0])
            #print(msa2[0])
        
    print(np.mean(diff))

if len(sys.argv) > 2:
    
    compare_msa(sys.argv[1], sys.argv[2])
