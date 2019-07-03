import numpy as np
import os
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

g = os.walk("/home/qikaiy2/Downloads/reu2019-tutorials/qikaiy2_project_1/results/data/gtrcat_dist")
path1 = "/home/qikaiy2/Downloads/reu2019-tutorials/qikaiy2_project_1/results/data/origin_dist"
i=0
record = ['alectoris_rufa', 'catreus_wallichi', 'chrysolophus_pictus', 'crossoptilon_crossoptilon', 'cyrtonyx_montezumae', 'galgal4',\
     'lophophorus_impejanus', 'lophura_inornata', 'lophura_nycthemera', 'lophura_swinhoii', 'melgal2', 'pavo_cristatus'\
    , 'perdix_dauuricae', 'phasianus_colchicus', 'rollulus_rouloul', 'syrmaticus_ellioti', 'syrmaticus_reevesii', 'tragopan_blythii']
def tackle(lis):
    for i in range(len(lis)):
        if(lis[i]==' '):
            lis.pop(i)

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
                transfer.append((line.replace('\n','')).split(" ",1))
    return transfer

def get_matrix(input):
    str_before = []
    index_after = []
    str_after = []
    for i in range(len(input)):
        str_before.append(input[i][0])
    for i in range(len(input)):
        str_after.append(input[i][0])
    str_after.sort()
    for i in range(len(str_after)):
        index_after.append(str_before.index(str_after[i]))
    #-------------------------
    temp = []
    for i in range(len(input)):
        temp.append(input[i][1].split())
    result = [[temp[i][j] for j in index_after] for i in index_after]
    '''for i in range(len(result)):
        print(result[i][i])'''
    return result

def change_address(address):
    return address[15:len(address)-18] +".nex.phy.mt"

box_array = []
mean_array = []
median_array = []
origin_array = []
simulated_array = []
x = np.arange(1479)
#x = x*0.1
print(x)

for path,dir_list,file_list in g:  
    for file_name in file_list:
        after = read_data(path+"/"+file_name) 
        before = read_data(path1 + "/" + change_address(file_name))
        after_ = get_matrix(after)
        before_ = get_matrix(before)
        for i in range(len(after_)):
            for j in range(len(after_[0])):
                after_[i][j] = float(after_[i][j])
                before_[i][j] = float(before_[i][j])
        before_ = np.array(before_)
        after_ = np.array(after_)
        subtraction = (before_-after_)
        temp = []
        for i in range(len(subtraction)):
            for j in range(i+1, len(subtraction[0])):
                temp.append(subtraction[i][j])
        box_array.append(temp)
        mean_array.append(np.mean(temp))
        median_array.append(np.median(temp))
        temp = []
        for i in range(len(before_)):
            for j in range(i+1, len(before_[0])):
                temp.append(before_[i][j])
        origin_array.append(temp)
        temp = []
        for i in range(len(after_)):
            for j in range(i+1, len(after_[0])):
                temp.append(after_[i][j])
        simulated_array.append(temp)

#--
plt.figure(figsize=(200,100))
plt.plot(x,mean_array,color="red")
plt.plot(x,median_array,color="blue")
plt.ylabel("Distance Differences")
plt.xlabel("1479 Data Sets")
plt.title("Distance errors of 1479 data sets")
plt.legend(["mean values of differences","median values of differences"])
plt.savefig('/home/qikaiy2/Downloads/reu2019-tutorials/qikaiy2_project_1/results/graph/mean_median_line.png')
#--
for i in range(5):
    plt.figure(i+1)
    plt.figure(figsize=(200,100))
    for j in range(4):
        haha = plt.subplot(2,2,j+1)
        plt.boxplot(box_array[int((i*4+j)*len(box_array)/20):int(((i*4+j)+1)*len(box_array)/20)],sym = 'o', \
        vert = True,\
        patch_artist = True,\
        meanline = False,\
        showmeans = True,\
        showbox = True,\
        showcaps = True,\
        showfliers=False)
        plt.xticks([])
        plt.xlabel("Data set Part "+str((i*4+j)+1))
        plt.ylabel("Distance Differences")
        haha.yaxis.grid(True)
    plt.suptitle("Distance Differences on Data Sets (from Part " + str(i*4+1) + " to Part " + str(str(i*4+4)+") without Outliers"))
    #plt.savefig('/home/qikaiy2/Downloads/reu2019-tutorials/qikaiy2_project_1/results/graph/dist_diff_without'+str(i+1)+'.png')

for i in range(5):
    plt.figure(i+6)
    plt.figure(figsize=(200,100))
    for j in range(4):
        haha = plt.subplot(2,2,j+1)
        plt.boxplot(box_array[int((i*4+j)*len(box_array)/20):int(((i*4+j)+1)*len(box_array)/20)],sym = 'o', \
        vert = True,\
        patch_artist = True,\
        meanline = False,\
        showmeans = True,\
        showbox = True,\
        showcaps = True)
        plt.xticks([])
        plt.xlabel("Data set Part "+str((i*4+j)+1))
        plt.ylabel("Distance Differences")
        haha.yaxis.grid(True)
    plt.suptitle("Distance Differences on Data Sets (from Part " + str(i*4+1) + " to Part " + str(str(i*4+4)+") with Outliers"))
    #plt.savefig('/home/qikaiy2/Downloads/reu2019-tutorials/qikaiy2_project_1/results/graph/dist_diff_with'+str(i+6)+'.png')

for i in range(5):
    plt.figure(i+11)
    plt.figure(figsize=(200,100))
    for j in range(4):
        haha = plt.subplot(2,2,j+1)
        plt.boxplot(origin_array[int((i*4+j)*len(origin_array)/20):int(((i*4+j)+1)*len(origin_array)/20)],sym = 'o', \
        vert = True,\
        patch_artist = True,\
        meanline = False,\
        showmeans = True,\
        showbox = True,\
        showcaps = True,\
        showfliers=False)
        plt.xticks([])
        plt.xlabel("Data set Part "+str((i*4+j)+1))
        plt.ylabel("Original Data set's Distances")
        haha.yaxis.grid(True)
    plt.suptitle("Distances of Original Data Sets (from " + str(i*4+1) + " to " + str(str(i*4+4)+") without Outliers"))
    #plt.savefig('/home/qikaiy2/Downloads/reu2019-tutorials/qikaiy2_project_1/results/graph/orig_dist_without'+str(i+11)+'.png')

for i in range(5):
    plt.figure(i+16)
    plt.figure(figsize=(200,100))
    for j in range(4):
        haha = plt.subplot(2,2,j+1)
        plt.boxplot(origin_array[int((i*4+j)*len(origin_array)/20):int(((i*4+j)+1)*len(origin_array)/20)],sym = 'o', \
        vert = True,\
        patch_artist = True,\
        meanline = False,\
        showmeans = True,\
        showbox = True,\
        showcaps = True)
        plt.xticks([])
        plt.xlabel("Data set Part "+str((i*4+j)+1))
        plt.ylabel("Original Data set's Distances")
        haha.yaxis.grid(True)
    plt.suptitle("Distances of Original Data Sets (from " + str(i*4+1) + " to " + str(str(i*4+4)+") with Outliers"))
    #plt.savefig('/home/qikaiy2/Downloads/reu2019-tutorials/qikaiy2_project_1/results/graph/orig_dist_with'+str(i+16)+'.png')

for i in range(5):
    plt.figure(i+21)
    plt.figure(figsize=(200,100))
    for j in range(4):
        haha = plt.subplot(2,2,j+1)
        plt.boxplot(simulated_array[int((i*4+j)*len(simulated_array)/20):int(((i*4+j)+1)*len(simulated_array)/20)],sym = 'o', \
        vert = True,\
        patch_artist = True,\
        meanline = False,\
        showmeans = True,\
        showbox = True,\
        showcaps = True,\
        showfliers=False)
        plt.xticks([])
        plt.xlabel("Data set Part "+str((i*4+j)+1))
        plt.ylabel("Simulated Data Set's Distances")
        haha.yaxis.grid(True)
    plt.suptitle("Distances of Simulated Data Sets (from " + str(i*4+1) + " to " + str(str(i*4+4)+") without Outliers"))
    #plt.savefig('/home/qikaiy2/Downloads/reu2019-tutorials/qikaiy2_project_1/results/graph/simu_dist_without'+str(i+16)+'.png')

for i in range(5):
    plt.figure(i+26)
    plt.figure(figsize=(200,100))
    for j in range(4):
        haha = plt.subplot(2,2,j+1)
        plt.boxplot(simulated_array[int((i*4+j)*len(simulated_array)/20):int(((i*4+j)+1)*len(simulated_array)/20)],sym = 'o', \
        vert = True,\
        patch_artist = True,\
        meanline = False,\
        showmeans = True,\
        showbox = True,\
        showcaps = True)
        plt.xticks([])
        plt.xlabel("Data set Part "+str((i*4+j)+1))
        plt.ylabel("Simulated Data Set's Distances")
        haha.yaxis.grid(True)
    plt.suptitle("Distances of Simulated Data Sets (from " + str(i*4+1) + " to " + str(str(i*4+4)+") with Outliers"))
    #plt.savefig('/home/qikaiy2/Downloads/reu2019-tutorials/qikaiy2_project_1/results/graph/simu_dist_with'+str(i+16)+'.png')

plt.show()