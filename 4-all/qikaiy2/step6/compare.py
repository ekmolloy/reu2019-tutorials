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

def get_depth(tree):
    dists = []
    for node in tree.preorder_internal_node_iter():
        if(node._parent_node is None):
            node.root_distance = 0.0
        else:
            node.root_distance = node.edge.length + node._parent_node.root_distance
            if((node.is_leaf()) is False):
                dists.append(node.root_distance)
    return dists

#parser = argparse.ArgumentParser()
#parser.add_argument("tree1", type=str, help="fastafilename1")
#parser.add_argument("tree2", type=str, help="fastafilename1")
#args = parser.parse_args()

dic = [1, 0.1, 0.05, 0.01, 0.005, 0.001]
head = "../data/tree/tree"
tail = ".tre"
print "MODL REPL MULT DIST TREE ESTI_LNTH ESTI_DEPTH TRUE_LNTH TRUE_DPTH"
for m in range(5):
    for n in range(6):
        tree1 = dendropy.Tree.get(path = head+str(m)+str(n)+tail, schema = "newick", rooting = "force-rooted",taxon_namespace=tax)
        tree2 = dendropy.Tree.get(path = "/projects/tallis/qikaiy2/reu2019-tutorials/data/100M3/R"+str(m)+"/rose.mt", schema = "newick", rooting = "force-rooted",taxon_namespace=tax)
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
        dist1 = get_depth(tree1)
        dist2 = get_depth(tree2)
        #print(len(get_depth(tree1)))
        #print(len(get_depth(tree2)))
        #print(len(edges1))
        #print(len(edges2)) 
        for i in range(len(edges1)):
            if(exist(edges1[i].bipartition, edges2) != -1):
                temp = exist(edges1[i].bipartition, edges2)
                print "100M3", \
                      "R"+str(m), \
                      str(dic[n]),\
                      "JC", \
                      "NJ", \
                      edges1[i].length, \
                      dist1[i], \
                      edges2[temp].length, \
                      dist2[i]
            else:
                print "100M3", \
                      "R"+str(m), \
                      str(dic[n]), \
                      "JC", \
                      "NJ", \
                      edges1[i].length, \
                      dist1[i], \
                      "NA", \
                      "NA"

        for j in range(len(edges2)):
            if(exist(edges2[j].bipartition, edges1) == -1):
                print "100M3", \
                      "R"+str(m), \
                      str(dic[n]), \
                      "JC", \
                      "NJ", \
                      "NA", \
                      "NA", \
                      edges2[j].length, \
                      dist2[j]
