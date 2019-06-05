import argparse
import dendropy
import os
import sys

def isShared(bi,tree):
    edges = tree.edges()
    for e in edges:
        if bi == e.bipartition:
            return e
    return None

def compareBiparitate(tree1,tree2,tax):
    res1 = dendropy.Tree.encode_bipartitions(tree1)
    res2 = dendropy.Tree.encode_bipartitions(tree2)
    
    edges1 = tree1.edges()
    edges2 = tree2.edges()
    for e1 in edges1:
        if e1.bipartition.is_trivial():
            continue
        res = isShared(e1.bipartition,tree2)
        if res == None:
            print(e1.length,'NA')
        else: 
            print(e1.length,res.length)
    for e2 in edges2:
        if e2.bipartition.is_trivial():
            continue
        res = isShared(e2.bipartition,tree1)
        if res == None:
            print('NA',e2.length)
        




def main(args):
    tax = dendropy.TaxonNamespace()
    tree1 = dendropy.Tree.get(path=args.tree1,
                             schema='newick',
                             rooting='force-rooted',
                             suppress_internal_node_taxa=False,
                             taxon_namespace=tax)
    tree2 = dendropy.Tree.get(path=args.tree2,
                             schema='newick',
                             rooting='force-rooted',
                             suppress_internal_node_taxa=False,
                             taxon_namespace=tax)
    compareBiparitate(tree1,tree2,tax)
    os._exit(0)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="comparison")
    parser.add_argument("-t1","--tree1",type=str, required=True)
    parser.add_argument("-t2,","--tree2",type=str,required=True)
    main(parser.parse_args())
