import dendropy
result = "[TYPE] NUCLEOTIDE 1\n"

dic = [1, 0.1, 0.05, 0.01, 0.005, 0.001]

def change(treestring,n):
    tackle = "[&R] " + treestring
    #print(tackle)
    tree = dendropy.Tree.get(data=tackle, schema="newick", rooting = "force-rooted")
    #print(tree.as_string(schema="newick"))
    for node in tree.preorder_node_iter():
        if(node.edge.length is None):
            node.edge.length = 0
        else:
            node.edge.length = '%6f' % (dic[n]*float(node.edge.length))

    final = tree.as_string(schema="newick")
    #final = final[4:]
    final = final[4:len(final)-4]
    final += ";"
    #print(final)
    return final

for i in range(5):
    for j in range(6):
        result += "[MODEL]  modelname"+str(i)+str(j)+"\n [submodel]    JC\n"  

for i in range(5):
    for j in range(6):
        result += "[TREE] Tree" + str(i)+str(j) +"  "
        f = open("../../data/100M3/R"+str(i)+"/rose.mt",'r')
        for line in f.readlines():
            line = line.strip()
            result += "  " + change(line.replace('\n',''), j)
        result += "\n"

for i in range(5):
    for j in range(6):
        result += "[PARTITIONS]  pJC" + str(i)+str(j) + " \n" + "[Tree"+ str(i)+str(j) + " modelname"+str(i)+str(j)+ " 1000]\n"

result += "[EVOLVE] \n"

for i in range(5):
    for j in range(6):
        result += "pJC"+ str(i)+str(j) + " 1 " + "data/align/alignment"+ str(i)+str(j) + "\n"

print(result)
y = change("((((A:1,B:2):6,C:3):7,D:4):8,E:5);",1)
