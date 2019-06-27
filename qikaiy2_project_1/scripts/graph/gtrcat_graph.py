import numpy as np
import os

g = os.walk("/home/qikaiy2/Downloads/reu2019-tutorials/qikaiy2_project_1/results/data/gtrcat_dist")
i=0

def read_data(address):
    f = open(address,'r')
    transfer = []
    i = 0
    for line in f.readlines():
        if(i==0):
            i+=1
            continue
        else:
            if(line != '\n'):
                transfer.append((line.replace('\n','')).split(' ', 1))
    return transfer

j = 0
for path,dir_list,file_list in g:  
    for file_name in file_list:
        if(j==0):
            print(read_data(path+"/"+file_name)) 
            j+=1
