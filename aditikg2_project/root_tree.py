import sys
from dendropy import Tree

def root_tree(f_name, out):

    t = Tree.get(path=f_name, schema="newick", rooting='force-rooted')
    
    t.reroot_at_midpoint()
    
    f = open(out, "w+")
    t.write(path=out, schema="newick", suppress_rooting=True, real_value_format_specifier="12.8f")
    f.close()

if len(sys.argv) > 2:
    root_tree(sys.argv[1], sys.argv[2])
else:
    print("Enter a valid tree file")
