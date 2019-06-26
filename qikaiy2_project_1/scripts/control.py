import dendropy
import os
import decimal
result = "[TYPE] NUCLEOTIDE 1\n"
path = "/home/qikaiy2/Downloads/reu2019-tutorials/qikaiy2_project_1/output_data/trees/GTRCAT"
files= os.listdir(path)
#The below codes come from this blog and the copyright belongs to the blogger:------------
# create a new context for this task
ctx = decimal.Context()

# 20 digits should be enough for everyone :D
ctx.prec = 20

def float_to_str(f):
    """
    Convert the given float to a string,
    without resorting to scientific notation
    """
    d1 = ctx.create_decimal(repr(f))
    return format(d1, 'f')
#-----------------------------------------------------------------------------------------

def filter(strr):
    if((strr[0:14]=="RAxML_bestTree")):
        return 1
    else:
        return 0

def filter1(strr):
    if((strr[0:10]=="RAxML_info")):
        return 1
    else:
        return 0

def filter2(strr):
    if((strr[len(strr)-7:len(strr)])=="reduced"):
        return 0
    else:
        return 1


def get_base(address):
    f = open(address,'r')
    result = ""
    for line in f.readlines():
        if(line[0:17]=="Base frequencies:"):
            result = line.split()
    return " " + str(result[5]) + " " + str(result[3]) + " " + str(result[2]) + " " + str(result[4]) 

def get_freq(address):
    f = open(address,'r')
    result = ""
    for line in f.readlines():
        if(line[0:9]=="alpha[0]:"):
            result = line.split()
    return " " + float_to_str(float(result[13])/float(result[10])) + " " + float_to_str(float(result[11])/float(result[10])) \
             + " " + float_to_str(float(result[14])/float(result[10])) + " " + float_to_str(float(result[9])/float(result[10])) \
             + " " + float_to_str(float(result[12])/float(result[10]))

i = 0
for file in files:
    if(filter(file)==1 and filter2(file)==1):
        temp = file.replace("bestTree","info")
        get_freq(path+"/"+temp)
        result += "[MODEL]  modelname"+ str(i) +"\n" \
                + " [submodel] GTR "+ get_freq(path+"/"+temp) + "\n" \
                + " [statefreq] " + get_base(path+"/"+temp) + " " + "\n"\
                + " [indelrate] 0 1 0" +"\n"
        i += 1

i=0
for file in files:
    if(filter(file)==1 and filter2(file)==1):
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
    if(filter(file)==1 and filter2(file)==1):
        result += "[PARTITIONS]  pGTR" + str(i) + " \n" + "[Tree"+ file + " modelname"+str(i)+ " 1000]\n"
        i+=1

result += "[EVOLVE] \n"

i = 0
for file in files:
    if(filter(file)==1 and filter2(file)==1):
        result += "pGTR"+ str(i) + " 1 " + "/home/qikaiy2/Downloads/reu2019-tutorials/qikaiy2_project_1/output_data/aligns/GTRCAT/"+ file + "\n"
        i += 1
print(result)
