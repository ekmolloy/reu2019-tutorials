from Bio import AlignIO
import os
#g = "/home/qikaiy2/Downloads/qikaiy2_project_1/input_data/aligns/paper_data"
g = os.walk("/home/qikaiy2/Downloads/qikaiy2_project_1/input_data/aligns/paper_data")
i = 0
path1 = "/home/qikaiy2/Downloads/qikaiy2_project_1/input_data/aligns/tackle_data"
for path,dir_list,file_list in g:  
    for file_name in file_list:
        print(file_name)  
        i+=1
        alignments = AlignIO.read(os.path.join(path, file_name), "nexus")
        output_handle = open(os.path.join(path1, file_name[:len(file_name)-3])+"fasta", "w")
        AlignIO.write(alignments, output_handle, "fasta")