import argparse
import dendropy
import os
import sys


def edgeLength(inputTree):
    res = dendropy.Tree.calc_node_root_distances(inputTree,
                                                return_leaf_distances_only=False)    
    newTree = inputTree.extract_tree(is_apply_filter_to_internal_nodes=False)
    i = 0
    for node in newTree.preorder_node_iter():
        if node._parent_node is None:
            i = i+1
            continue
        node.edge.length = res[i]
        i = i+1
    print(newTree.as_string(schema='newick'))
    #print(res)



def main(args):
    tax = dendropy.TaxonNamespace()
    inputTree = dendropy.Tree.get(path=args.tree1,
                                  schema='newick',
                                  rooting='force-rooted',
                                  suppress_internal_node_taxa=False,
                                  taxon_namespace=tax)
    edgeLength(inputTree)
    #sys.stdout.write(outputTree.as_string(schema="newick"))
    #sys.stdout.flush()
    #os._exit(0)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="inputTree")
    parser.add_argument("-t1","--tree1",type=str, required=True,help="File for inputTree")
    main(parser.parse_args())
