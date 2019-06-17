result = "[TYPE] NUCLEOTIDE 1\n"

for i in range(5):
    result += "[MODEL]  modelname"+str(i)+"\n [submodel]    JC\n"  

for i in range(5):
    result += "[TREE] Tree" + str(i) +"  "
    f = open("../../data/100M3/R"+str(i)+"/rose.mt",'r')
    for line in f.readlines():
        line = line.strip()
        result += "  " + line.replace('\n','')
    result += "\n"

for i in range(5):
    result += "[PARTITIONS]  pJC" + str(i) + " \n" + "[Tree"+ str(i) + " modelname"+str(i)+ " 1000]\n"

result += "[EVOLVE] \n"

for i in range(5):
    result += "pJC"+ str(i) + " 1 " + "data/align/alignment"+ str(i) + "\n"

print(result)
