import os
import string
import numpy as np
import argparse
import dendropy

def main(args):
    estimatedPath = args.estimated
    truePath = args.true
    filename = args.filename
    tax = dendropy.TaxonNamespace()
    estimatedTree = dendropy.Tree.get(path=estimatedPath
                                  ,schema="newick"
                                  ,taxon_namespace=tax)
    trueTree = dendropy.Tree.get(path=truePath
                             ,schema="newick"
                             ,taxon_namespace=tax)
    RF = dendropy.calculate.treecompare.robinson_foulds_distance(trueTree, estimatedTree, edge_weight_attr='length')
    fptr = open("all_RF_Distance.csv", "a")
    fptr.write("%s,%s\n"%(filename,RF))
    fptr.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compares two trees")
    parser.add_argument("-t1", "--estimated", type=str,  required=True,
                        help="estimated")
    parser.add_argument("-t2", "--true", type=str, required=True,
                        help="true")
    parser.add_argument("-f","--filename",type=str,required=True,help="filename")
    main(parser.parse_args())
