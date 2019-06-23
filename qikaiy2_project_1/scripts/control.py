import dendropy
import os
result = "[TYPE] NUCLEOTIDE 1\n"
path = "/home/qikaiy2/Downloads/reu2019-tutorials/qikaiy2_project_1/output_data/trees/GTRGAMMA"
files= os.listdir(path)

def filter(strr):
    if((strr[0:14]=="RAxML_bestTree")):
        return 1
    else:
        return 0

for i in range(1479):
    result += "[MODEL]  modelname"+str(i)+"\n [submodel]    GTR\n"  

for file in files:
    if(filter(file)==1):
        result += "[TREE] Tree" + file+"  "
        f = open(path+"/"+file,'r')
        for line in f.readlines():
            line = line.strip()
            line = line[:len(line)-5]
            line = line+";"
            result += "  " + line.replace('\n','')
        result += "\n"

i=0
for file in files:
    if(filter(file)==1):
        result += "[PARTITIONS]  pGTR" + str(i) + " \n" + "[Tree"+ file + " modelname"+str(i)+ " 1000]\n"
        i+=1

result += "[EVOLVE] \n"

i = 0
for file in files:
    if(filter(file)==1):
        result += "pGTR"+ str(i) + " 1 " + "/home/qikaiy2/Downloads/qikaiy2_project_1/output_data/aligns/GTRGAMMA/"+ file + "\n"
        i += 1
print(result)
