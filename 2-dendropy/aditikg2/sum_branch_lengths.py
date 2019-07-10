import dendropy
import sys

if (len(sys.argv) > 1):

    t = dendropy.Tree.get(data=sys.argv[1], schema="newick")
    edges = t.edges()

    for edge in edges:
        edge.length = edge.head_node.distance_from_root()

    print(t)
else:
    print("Please enter the tree in Newick format as an argument")
