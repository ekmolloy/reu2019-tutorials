import sys
from dendropy import Tree

# Scales the branch length of a given tree file
def scale_tree(f_name, n):

    t = Tree.get(file=open(f_name, 'r'), schema="newick", tree_offset=0)

    for e in t.edges():
        if e.length is not None:
            e.length = float(n*float(e.length))
    
    t.write(file=open(f_name.replace('.mt', '') + '_' + str(n).replace('.', '_') + '.mt', 'w+'), schema="newick")

if len(sys.argv) > 2:

    f = sys.argv[1]
    scaling_fac = float(sys.argv[2])
    scale_tree(f, scaling_fac)
