import os
import sys
import dendropy

tree = dendropy.Tree.get(
    path=sys.argv[1], 
    schema="newick", 
    rooting="default-unrooted"
)

outgroup_leaves = ["Atta_cephalotes_Genome", "Camponotus_floridanus_Genome","Cardiocondyla_obscurior_Genome","Linepithema_humile_Genome","Pogonomyrmex_barbatus_Genome", "Solenopsis_invicta_Genome","Vollenhovia_emeryi_Genome"]

# since dendropy implements mrca by looking at bipartitions this is an okay thing to do 
mrca = tree.mrca(taxon_labels=outgroup_leaves)
if mrca is not None:
    tree.reroot_at_edge(mrca.edge, update_bipartitions=True)
else:
    tree.reroot_at_midpoint(update_bipartitions=True)
print(tree.as_string(schema="newick"))
