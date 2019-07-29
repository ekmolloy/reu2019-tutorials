from dendropy import Tree
import sys

def remove_branch_lengths(f, out):

    t = Tree.get(file=open(f, 'r'), schema="newick")
    new = open(out, 'w+')

    for e in t.edges():
        e.length = None
    
    t.write(file=new, schema="newick")

if len(sys.argv) > 2:
    remove_branch_lengths(sys.argv[1], sys.argv[2])
    
