import dendropy
import sys

def get_corresponding_edge(et, tt, e):
    tt.encode_bipartitions()
    for t in tt.internal_edges():
        if t.bipartition == e.bipartition:
            return t
    return None

def calc_depth(tree, edge=None, node=None):
    if edge is not None:
       # print("we're in the edgegame now")
        return calc_depth(tree, node=edge.head_node)
    if node is not None:
       # print("node.js")
        if node._parent_node is None:
            return 0
        else:
            return node.edge.length + calc_depth(tree, node=node._parent_node)

def calc_length(tree, edge):
    return e.length

et = dendropy.Tree.get(path=sys.argv[1], schema="newick")
tt = dendropy.Tree.get(path=sys.argv[2], schema="newick")

# get et's bipartitions
# make each of et's internal edges be associated with a bipartition
etbiparts = et.encode_bipartitions()

ttbiparts = tt.encode_bipartitions()

for e in et.internal_edges(exclude_seed_edge=True):
    esti_lnth = calc_length(et, e)
    esti_dpth = calc_depth(et, edge=e)
    if e.bipartition in ttbiparts:
        t = get_corresponding_edge(et, tt, e)
        print("%s %s %s %s"%(esti_lnth, esti_dpth, calc_length(tt, edge=t), calc_depth(tt, edge=t)))
    else:
        print("%s %s NA NA"%(esti_lnth, esti_dpth))
    
