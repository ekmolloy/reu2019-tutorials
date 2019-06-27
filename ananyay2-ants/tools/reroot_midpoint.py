import os
import sys
import dendropy

tree = dendropy.Tree.get(
    path=sys.argv[1], 
    schema="newick", 
    rooting="default-unrooted"
)

tree.reroot_at_midpoint(update_bipartitions=True)
print(tree.as_string(schema="newick"))
