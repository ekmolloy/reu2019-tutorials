import dendropy
import sys
from dendropy.calculate import treecompare


if len(sys.argv) > 2:

    f = open('compare.csv', 'w+')
    
    t1 = dendropy.Tree.get(data=sys.argv[1], schema="newick", rooting="default-rooted")
    t2 = dendropy.Tree.get(data=sys.argv[2], schema="newick", rooting="default-rooted")
    
    bi1 = t1.bipartition_edge_map
    bi2 = t2.bipartition_edge_map

    common = {}
    
    for b1 in bi1:
        if (not b1.is_trivial()):
            if (bi1[b1].length is not None):
                f.write(str(bi1[b1].length))
            else:
                f.write('0.0')
            f.write(",")
            if (b1 in bi2) and (bi2[b1].length is not None):
                f.write(str(bi2[b1].length))
                common[b1] = bi2[b1]
            elif (b1 in bi2) and (bi2[b1].length is None):
                f.write('0.0')
                common[b1] = bi2[b1]
            else:
                f.write("NA")

            f.write("\n")

    for b2 in bi2:

        if (b2 not in common) and (not b2.is_trivial()):
            f.write("NA,")

            if (bi2[b2].length is not None):
                f.write(str(bi2[b2].length))
            else:
                f.write('0.0')

            f.write("\n")    

    f.close()
else:
    print("Enter two trees to compare as arguments")
