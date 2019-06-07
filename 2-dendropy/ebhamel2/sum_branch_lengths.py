import dendropy
import os
import sys

def sum_branch_lengths(tree):
	distances = tree.calc_node_root_distances(return_leaf_distances_only=False)
	distances.pop(0)
	new_tree = tree.as_string("newick")
	removed_lengths = ''.join([i for i in new_tree if not i.isdigit()])
	length = len(removed_lengths)
	removed_lengths = removed_lengths.replace(".", "")
	removed_lengths_list = list(removed_lengths)

	for x in range(0, length):
		if removed_lengths_list[x] == ":":
			removed_lengths_list.insert(x+1, str(distances[0]))
			distances.pop(0)
		 
	final = ''.join(removed_lengths_list)
	return final
	
if __name__ == "__main__":
	argc = len(sys.argv)
	assert (argc == 2), "Usage: assess_dataset.py tree"
	try:
		tree = dendropy.Tree.get(path=sys.argv[1], schema='newick',preserve_underscores=True)
		branch_lengths = sum_branch_lengths(tree)
		sys.stdout.write('%s\n' % (branch_lengths))
		quit()
	except:
		quit()
