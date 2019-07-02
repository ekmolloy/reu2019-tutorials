import os
import sys
import dendropy

tree = dendropy.Tree.get(
    path=sys.argv[1], 
    schema="newick", 
    rooting="default-unrooted"
)

outgroup_leaves = ["Atta cephalotes Genome", "Camponotus floridanus Genome","Cardiocondyla obscurior Genome","Linepithema humile Genome","Pogonomyrmex barbatus Genome", "Solenopsis invicta Genome","Vollenhovia emeryi Genome", "Harpegnathos saltator Genome"]

# don't look for leaves that aren't there
for l in outgroup_leaves:
    if tree.find_node_with_taxon_label(l) is None:
        outgroup_leaves.remove(l)

# since dendropy implements mrca by looking at bipartitions this is an okay thing to do 
mrca = tree.mrca(taxon_labels=outgroup_leaves)
if mrca is not None:
    tree.reroot_at_edge(mrca.edge, update_bipartitions=True)
else:
    tree.reroot_at_midpoint(update_bipartitions=True)
print(tree.as_string(schema="newick"))
