import dendropy
import argparse
import os
def helpfunc(tree):
	
	sum = 0
	for node in tree.preorder_node_iter():
		if node.edge.length == None:
			continue
		sum+=node.edge.length
	return sum

def main(args):
	factor = args.factor
	tax = dendropy.TaxonNamespace()
#for factor in [0.1,0.05,0.01,0.005,0.001]:
	file = open("control.txt","w") 
	file.write("[TYPE] NUCLEOTIDE 1\n") 
	file.write("[MODEL] mymodel\n")
	file.write("\t[submodel] JC\n")
	for i in range(5):
    		treePath = "../../data/100M3/R%s/rose.mt" %(i)
		tree = dendropy.Tree.get(path=treePath,schema='newick',taxon_namespace=tax)
		print(treePath)
		total = helpfunc(tree)
		treelength = total * factor
    		treefile = open(treePath, "r")
    		contents = treefile.read()
    		file.write("[TREE] tree%s %s"%(i,contents))
		file.write("[treelength] %s\n"%(treelength))
	for i in range(5):
    		file.write("[PARTITIONS] p%s\n"%(i))
    		file.write("\t[tree%s mymodel 100]\n"%(i))
		file.write("[EVOLVE]\n")
	for i in range(5):
    		file.write("\tp%s 1 output%s%s\n"%(i,i,factor))
	file.close()
	os._exit(0)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="factor")
	parser.add_argument("-f","--factor",type=float,required=True)
	main(parser.parse_args())
