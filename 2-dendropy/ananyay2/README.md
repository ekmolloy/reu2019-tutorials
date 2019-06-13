**When you make one of these changes, add replace -[ ] with -[X] and commit this file.**

- [ ] I think that your life would be easier if you used the [dendropy API](https://dendropy.org):

```
tree = dendropy.Tree.get(path="", schema="")
for node in tree.preorder_node_iter():
    edge.old_length = length
    if node._parent_node is not None:
        edge.length = 10000
tree.write(path="", schema="")
```
