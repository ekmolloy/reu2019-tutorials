import numpy as np
import dendropy 
import os
import decimal
ctx = decimal.Context()
ctx.prec = 20

path1 = "/home/qikaiy2/Downloads/reu2019-tutorials/qikaiy2_project_1/output_data/trees/GTRCAT"
path2 = "/home/qikaiy2/Downloads/reu2019-tutorials/qikaiy2_project_1/output_data/trees/R_GTRCAT"
g = os.walk(path1)

def filter(strr):
    if((strr[0:14]=="RAxML_bestTree")):
        return 1
    else:
        return 0

def filter2(strr):
    if((strr[len(strr)-7:len(strr)])=="reduced"):
        return 0
    else:
        return 1

def float_to_str(f):
    """
    Convert the given float to a string,
    without resorting to scientific notation
    """
    d1 = ctx.create_decimal(repr(f))
    return format(d1, 'f')

#TO_DO!! MAKE THE RESULTS NUMERICAL!!!
#--------------------------------------------------------------------------------
#The below function's copyright belongs to this link:https://github.com/faircloth-lab/phyluce/blob/master/bin/genetrees/phyluce_genetrees_phybase
#--------------------------------------------------------------------------------
def branch_lengths_2_decimals(str_newick_tree):
    """replaces branch lengths in scientific notation with decimals"""
    colon_s = 0
    #comma_back_paren_s = 0
    num = ''
    new_tree = ''
    for count, char in enumerate(str_newick_tree):
        if char == ':':
            colon_s = count
            continue
        if char in (')', ','):
            #comma_back_paren_s = 1
            num = float_to_str(float(num)) 
            new_tree += ":" + num
            colon_s = 0
            num = ''
        if colon_s != 0:
            num = num + char
        if colon_s == 0:
            new_tree += char
    new_tree = new_tree.strip('\'').strip('\"').strip('\'') + ";"
    return new_tree
#--------------------------------------------------------------------------------

i=0
for path_,dir_list,file_list in g:  
    for file_name in file_list:
        if(filter(file_name)==1 and filter2(file_name)==1):
            f = open(path_+"/"+file_name,'r')
            for line in f.readlines():
                tree_string = line.replace('\n','')
                tree = dendropy.Tree.get(data=tree_string, schema="newick", rooting='force-rooted')
                node = tree.find_node_with_taxon_label("cyrtonyx montezumae")
                temp = node.edge.length/2.0                                        # root length record
                tree.reroot_at_edge(node.edge, update_bipartitions=False)
                #----------------after reroot------------------------------------------------------------
                node = tree.find_node_with_taxon_label("cyrtonyx montezumae")
                node.parent_node.child_edges()[0].length = temp
                node.parent_node.child_edges()[1].length = temp
                #----------------store the tree----------------------------------------------------------
                result = branch_lengths_2_decimals(tree.as_string(schema='newick')[5:])
                print(result)
                f = open(path2 + "/" + file_name,'w')
                f.write(result)