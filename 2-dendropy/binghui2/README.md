Updates
-------
- [ ] Re-write the code to avoid using the `calc_node_root_distances` because right now your code assumes that the output of this function is the same traversal as `preorder_node_iter` but if this wasn't the case your output would break (for example if this was updated in future versions of dendropy). Also, it is useful to modify the tree structure to have new variables.
- [ ] Instead of printing the tree in the function `edgeLength` have the function return `newTree` -- which would allow this function to be called by another module.
- [ ] Instead of printing the tree, maybe write the tree to an output file in the `main` function. For example, you could specify the input and output files using args (`-i` and `-o`).
- [ ] Udate the code to use `if __name__ == "__main__":` so that your code can either be excuted on the command line or imported into another python script or module.

Notes
-----
Good work using main functions!


