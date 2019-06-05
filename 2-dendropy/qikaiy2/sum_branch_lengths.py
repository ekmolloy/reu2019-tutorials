import dendropy
import argparse

# when applying this function, we should do as below:
# python sum_branch_lengths.py xxxx 
# xxxx is the txt file that store the input tree as newwick format

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="input_tree")
args = parser.parse_args()
print("the address of the tree file is as below:")
print(args.file)
print("-------")
tree = dendropy.Tree.get(path = args.file, schema = "newick", rooting = "force-rooted")
store = tree.calc_node_root_distances(return_leaf_distances_only=False)
print("the original tree is as below:")
print(tree.as_string(schema="newick"))
print("-------")
#----------------------------------above is the first part -> get the tree and all the distances------------------------------
i = 0
for node in tree.preorder_node_iter():
    node.edge.length = store[i]
    i += 1
print("the editted tree is as below:")
print(tree.as_string(schema="newick"))
print("-------")
#----------------------------------second part -> change the weights of the edges 
