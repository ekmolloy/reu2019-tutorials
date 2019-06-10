import argparse
import dendropy
import os
import sys
#############get the depth of an edge
def getDepth(inputTree,bipar_edge):
	res = dendropy.Tree.calc_node_root_distances(inputTree,
	                                            return_leaf_distances_only=False)
	#print(res)
	#all_nodes = inputTree.extract_tree(is_apply_filter_to_internal_nodes=False)
	i = 0
	for node in inputTree.preorder_node_iter():
		if node.edge == bipar_edge:
			#print(res[i])
			return res[i]
		i = i+1
	return -1
	#print(newTree.as_string(schema='newick'))


##### is this used to check whether the split is shard
def isShared(bi,tree):
    edges = tree.edges()
    for e in edges:
        if bi == e.bipartition:
			return e
    return None
####comparsion func
####tree1 is estimated
####tree2 is true tree
def compareBiparitate(tree1,tree2,tax,index,factor):
    if len(tree1.nodes()) != len(tree1.nodes()):
        print("trees of different number of leaves")
        return
    res1 = dendropy.Tree.encode_bipartitions(tree1)
    res2 = dendropy.Tree.encode_bipartitions(tree2)
    
    edges1 = tree1.edges()
    edges2 = tree2.edges()
    for e1 in edges1:
		if e1.bipartition.is_trivial():
			continue
		res = isShared(e1.bipartition,tree2)
		depth1 = getDepth(tree1,e1)
		if res == None:
			#return e1.length,depth1,'NA','NA')
			print "100M3,R%s,%s,JC,NJ,%s,%s,NA,NA"%(index,factor,e1.length,depth1)
		else:
			depth2 = getDepth(tree2,res)
			#return (e1.length,depth1,res.length,depth2)
			print "100M3,R%s,%s,JC,NJ,%s,%s,%s,%s"%(index,factor,e1.length,depth1,res.length,depth2)
    #for e2 in edges2:
    #   if e2.bipartition.is_trivial():
    #        continue
    #    res = isShared(e2.bipartition,tree1)
    #    if res == None:
    #        print('NA',e2.length)
        



###main func
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
	index = args.index
	factor = args.factor
	compareBiparitate(tree1,tree2,tax,index,factor)
	sys.stdout.flush()
	#print(res)
	#return res
	#os._exit(0)


###parser copied from compare_trees.py
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="comparison")
	parser.add_argument("-t1","--tree1",type=str, required=True)
	parser.add_argument("-t2,","--tree2",type=str,required=True)
	parser.add_argument("-t3","--index",type=float,required=False)
	parser.add_argument("-t4","--factor",type=float,required=False)
	main(parser.parse_args())
