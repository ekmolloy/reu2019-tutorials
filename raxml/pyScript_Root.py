import os
import string
import argparse
import dendropy

def rootTree(inputTree):
	mrca = inputTree.mrca(taxon_labels=["cardinalis cardinalis ku21828", "cardinalis cardinalis ku25393"])
	inputTree.reroot_at_node(mrca, update_bipartitions=False)
	return inputTree
    #inputTree.to_outgroup_position()

def main(args):
	tax = dendropy.TaxonNamespace()
	inputTree = dendropy.Tree.get(path=args.tree,
                                  schema='newick',
                                  rooting='force-rooted',
                                  suppress_internal_node_taxa=False,
                                  taxon_namespace=tax)
        
	outputTree = rootTree(inputTree)
	outputTree.write_to_path(args.output,
                    schema="newick")
    
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="inputTree")
	parser.add_argument("-t","--tree",type=str, required=True,help="File for inputTree")
	parser.add_argument("-o","--output",type=str,required=True,help="path for output")
	main(parser.parse_args())
