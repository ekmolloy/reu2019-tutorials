import dendropy
import argparse
from dendropy.calculate import treecompare
tax = dendropy.TaxonNamespace()

# when applying this function, we sgould do as below:
# python compare.py xxx1.txt xxx2.txt --> result.csv
# xxx1.txt and xxx2.txt contain trees that we needto compare

def exist(bi, ls):
    for i in range(len(ls)):
        if(bi == ls[i].bipartition):
            return i
    return -1

parser = argparse.ArgumentParser()
parser.add_argument("tree1", type=str, help="fastafilename1")
parser.add_argument("tree2", type=str, help="fastafilename1")
args = parser.parse_args()

tree1 = dendropy.Tree.get(path = args.tree1, schema = "newick", rooting = "force-rooted",taxon_namespace=tax)
tree2 = dendropy.Tree.get(path = args.tree2, schema = "newick", rooting = "force-rooted",taxon_namespace=tax)
#----------------------------------------------------------------------
#From Ph.D. Erin Molloy at University of Illinois at Urbana-Champaign
lb1 = set([l.taxon.label for l in tree1.leaf_nodes()])
lb2 = set([l.taxon.label for l in tree2.leaf_nodes()])

com = lb1.intersection(lb2)
if com != lb1 or com != lb2:
    com = list(com)
    tns = dendropy.TaxonNamespace(com)

    tree1.retain_taxa_with_labels(com)
    tree1.migrate_taxon_namespace(tns)

    tree2.retain_taxa_with_labels(com)
    tree2.migrate_taxon_namespace(tns)
com = list(com)

tree1.update_bipartitions()
tree2.update_bipartitions()
#-----------------------------------------------------------------------
edges1 = tree1.internal_edges(exclude_seed_edge=True)
edges2 = tree2.internal_edges(exclude_seed_edge=True)

for i in range(len(edges1)):
    if(exist(edges1[i].bipartition, edges2) != -1):
        print edges1[i].length,",",edges2[exist(edges1[i].bipartition, edges2)].length
    else:
        print edges1[i].length,",","NA"

for j in range(len(edges2)):
    if(exist(edges2[j].bipartition, edges1) == -1):
        print "NA",",",edges2[j].length
