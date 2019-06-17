import dendropy
import sys
import os
# in hindsight I didn't need to write part a, I could just make the scales list an argument. 
def make_control_file(rep_folder, end_folder):
    scales=[1.0, 0.1, 0.05, 0.01, 0.005, 0.001]
    num_reps = len([i for i in os.listdir(rep_folder) if os.path.isdir(".")])
    print("[TYPE] NUCLEOTIDE 1")
    model_submodel(num_reps*len(scales))
    tree(rep_folder, end_folder, num_reps, scales)
    partitions(num_reps*len(scales))
    evolutions(num_reps, scales, end_folder)

def model_submodel(n):
    for i in range(n):
        print("\n[MODEL] m%u \n [submodel] JC"%i)

def tree(rep_folder, end_folder, n, scales):
    for t in range(n):
        filepath = rep_folder + "/R%u/rose.mt"%t
        for j in range(len(scales)):
            tree = dendropy.Tree.get(path=filepath, schema="newick")
            tree.scale_edges(scales[j])
            p=end_folder+"/R%u/%s.tt"%(t, str(scales[j]).replace(".","-"))
            tree.write(path=p, schema="newick", real_value_format_specifier=".6f")

            full_contents = ""
            with open(p, 'r') as tree_file:
                full_contents += tree_file.read()

            print("[TREE] T%u %s\n"%((t*len(scales))+j, full_contents))

def partitions(n):
    for i in range(n):
        print("[PARTITIONS] p%u\n[T%u m%u 1000]"%(i,i,i))

def evolutions(n, scales, end_folder):
    print("\n[EVOLVE] ")
    for t in range(n):
        for j in range(len(scales)):
            print("p%u 1 %s/R%u/INDELible_%s"%((t*len(scales))+j,end_folder,t,str(scales[j]).replace(".","-")))        

make_control_file(sys.argv[1], sys.argv[2])

