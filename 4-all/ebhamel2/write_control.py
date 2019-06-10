import dendropy
import os
import sys

def get_newick_string(tree):
    """
    Creates a newick string with  branch lengths in decimal notation.
    This function was taken from Phybase.py, see
    github.com/ngcrawford/CloudForest/blob/master/cloudforest/phybase.py

    Parameters
    ----------
    tree : dendropy tree

    Returns
    -------
    new_tree : string
               newick representation of tree
    """
    from decimal import Decimal

    str_newick_tree = tree.as_string(schema='newick')

    colon_s = 0
    comma_back_paren_s = 0
    num = ''
    new_tree = ''
    for count, char in enumerate(str_newick_tree):
        if char == ':':
            colon_s = count
            continue
        if char in (')', ','):
            comma_back_paren_s = 1
            num = '%1.12f' % Decimal(num)
            new_tree += ":" + num
            colon_s = 0
            num = ''
        if colon_s != 0:
            num = num + char
        if colon_s == 0:
            new_tree += char
    new_tree = new_tree.strip('\'').strip('\"').strip('\'') + ';\n'
    new_tree = new_tree[5:].replace(";\n;\n", ";\n")
    return new_tree


def resolve_polytomies(tree):
    """
    Randomly resolves polytomies in tree.

    Parameters
    ----------
    tree : dendropy tree
    """
    tree.resolve_polytomies(limit=2,
                            update_bipartitions=True)

for i in range(0, 1): 
	tre = dendropy.Tree.get(file=open("/Users/emmahamel/Research/Phylogeny/trees/rate_0.00001/1/0_tree.tre"), 
		schema="newick")
	resolve_polytomies(tre)
	
	file = open('control.txt', 'w')

	treeString = get_newick_string(tre)

	file.write("[TYPE] NUCLEOTIDE 1\n")
	file.write("[MODEL] modelname\n")
	file.write("[submodel] GTR 0.318706 0.083336 0.126271 0.450343 0.089108\n")
	file.write("[statefreq] 0.193359 0.253100 0.330303 0.223238\n")
	file.write("[rates] 0 0.188771 0\n")
	file.write("[TREE] treename  " + treeString + "\n")
	file.write("[SETTINGS] [fileperrep] TRUE [output] FASTA\n")
	file.write("[PARTITIONS] partitionname\n")
	file.write("[treename modelname 500]\n")
	file.write("[EVOLVE] partitionname 20 /projects/tallis/hamel/reu2019-tutorials/4-all/ebhamel2/results/" + sys.argv[1] + "alignment")
	file.close()

	os.system("/projects/tallis/reu2019/software/INDELibleV1.03/src/indelible")

