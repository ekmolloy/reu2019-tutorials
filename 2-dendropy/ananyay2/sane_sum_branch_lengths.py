import dendropy
import sys
import os

# Get the tree
tree = dendropy.Tree.get(path=sys.argv[1], schema="newick")

# add distance to root to each of the nodes
dists = tree.calc_node_root_distances()

# make dist to root the new edge length so newick comes out ok
for node in tree.preorder_node_iter():
    node.edge.length = node.root_distance

print(tree.__str__())
