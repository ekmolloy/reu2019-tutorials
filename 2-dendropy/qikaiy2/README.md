Updates
-------
- [ ] Re-write the code to avoid using the `calc_node_root_distances` because right now your code assumes that the output of this function is the same traversal as `preorder_node_iter` but if this wasn't the case your output would break (for example if this was updated in future versions of dendropy). Also, it is useful to modify the tree structure to have new variables.
- [ ] Instead of printing the tree, maybe write the tree to an output file that can be specifying in args (`-i` and `-o`).
- [ ] `Use if __name__ == "__main__":` and `main` functions and a separate function that does the work so that your script can be excuted from the command line or imported into a different python script or module --- baically this will make your code more reusable. 
