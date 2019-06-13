"""
Comparison of two trees using dendropy.

Written by EKM (molloy.erin.k@gmail.com) in October 2016.

If the input is
+ tree 1 = "(((A,B,C),D),E);"
+ tree 2 = "((((A,B),C),D),E);"

then the output is
+ "5 1 2 0 1 0.25"

where

NL = 5
    + # of leaves are shared between tree 1 and tree 2
    + in this example: A, B, C, D, and E
I1 = 1
    + # of internal branch in tree 1
    + in this example: A,B,C|D,E
I2 = 2
    + # of internal branches in tree 2
    + in this example: A,B|C,D,E and A,B,C|D,E
FN = 0
    + # of internal branches (from tree 1) missing from tree 2
    + # of false negatives if tree 1 is true and tree 2 is estimated
FP = 1
    + # of internal branch (from tree 2) missing from tree 1
    + # of false positives if tree 1 is true and tree 2 is estimated
    + in this example: A,B|C,D,E
RF = 0.25
    + Robinson-Foulds (RF) distance
    + in this example: (FP+FN)/(2*NL-6) = (1+0)/(2*5-6) = 0.25
"""
import os
import sys

import dendropy
from dendropy.calculate.treecompare \
    import false_positives_and_negatives


def compare_trees(tr1, tr2):
    from dendropy.calculate.treecompare \
        import false_positives_and_negatives

    lb1 = set([l.taxon.label for l in tr1.leaf_nodes()])
    lb2 = set([l.taxon.label for l in tr2.leaf_nodes()])

    com = lb1.intersection(lb2)
    if com != lb1 or com != lb2:
        com = list(com)
        tns = dendropy.TaxonNamespace(com)

        tr1.retain_taxa_with_labels(com)
        tr1.migrate_taxon_namespace(tns)

        tr2.retain_taxa_with_labels(com)
        tr2.migrate_taxon_namespace(tns)
    com = list(com)

    tr1.update_bipartitions()
    tr2.update_bipartitions()

    nl = len(com)
    ei1 = len(tr1.internal_edges(exclude_seed_edge=True))
    ei2 = len(tr2.internal_edges(exclude_seed_edge=True))

    [fn, fp] = false_positives_and_negatives(tr1, tr2)
    rf = (fn + fp) / (2.0 * nl - 6.0)

    return(nl, ei1, ei2, fn, fp, rf)


if __name__ == "__main__":
    argc = len(sys.argv)
    assert (argc == 3), "Usage: assess_dataset.py tr1 tr2"

    tax = dendropy.TaxonNamespace()
    tr1 = dendropy.Tree.get(path=sys.argv[1],
                            schema='newick',
                            rooting='force-unrooted',
                            taxon_namespace=tax)

    tr2 = dendropy.Tree.get(path=sys.argv[2],
                            schema='newick',
                            rooting='force-unrooted',
                            taxon_namespace=tax)

    tr1.collapse_basal_bifurcation(set_as_unrooted_tree=True)
    tr2.collapse_basal_bifurcation(set_as_unrooted_tree=True)

    [nl, ei1, ei2, fn, fp, rf] = compare_trees(tr1, tr2)
    sys.stdout.write('%d,%d,%d,%d,%d,%1.6f\n' % (nl, ei1, ei2, fn, fp, rf))
    sys.stdout.flush()
    os._exit(0)  # CRITICAL ON BLUE WATERS LOGIN NODE
