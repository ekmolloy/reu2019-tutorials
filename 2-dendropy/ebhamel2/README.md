**When you make one of these changes, add replace -[ ] with -[X] and commit this file.**

- [ ] I like that you are using exceptions. These are good for catching a exceptions thrown by functions and then handling them so that the code can progress, for example, 
```
try:
    # Try to read tree as NEXUS file
    tree = dendropy.Tree.get(path=sys.argv[1], schema='nexus', preserve_underscores=True)
except NotNexusFileError:
    # Try to read tree as NEWICK file
    tree = dendropy.Tree.get(path=sys.argv[1], schema='newick', preserve_underscores=True)
    
# Do things with trees
```
I probably won't use an exception here, because you are really just using it to surpress an error message --- that a user would find useful.
- [ ] Re-write the code to avoid using the `calc_node_root_distances`, because this essentially assumes that you can guarantee the ordering of the vector returned by `calc_node_root_distances` (which could change in future versions of dendropy). Here are some useful things from the dendropy API:

```
for node in newTree.preorder_node_iter():
    edge.old_length = length
    if node._parent_node is not None:
        edge.length = 10000
```
