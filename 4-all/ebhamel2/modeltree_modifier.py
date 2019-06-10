import dendropy
import sys

tree_dictionary = {}

def get_rep(file_path):
        file_path_split = file_path.split("/")
        return file_path_split[-2]

for i in range (0, 6):
	tree_dictionary[i] = dendropy.Tree.get(file=open(sys.argv[1]),
                	schema="newick")

set_constant = [1, 0.1, 0.05, 0.01, 0.005, 0.001]

for k in range(0, len(set_constant)):
	tree_dictionary[k].scale_edges(set_constant[k])

for i in range(0, len(set_constant)):
	tree_dictionary[i].write(path='/projects/tallis/hamel/reu2019-tutorials/4-all/ebhamel2/scaled_tree/modeltrees/' + get_rep(sys.argv[1]) + '_scale_' +  str(set_constant[i]) + '.tre', 
		schema="newick")
	print(str(set_constant[i]) + " is finished")


