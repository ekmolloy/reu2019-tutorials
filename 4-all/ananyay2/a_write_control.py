import dendropy
import sys
import os

def make_control_file(rep_folder, end_folder):
    print("[TYPE] NUCLEOTIDE 1")
    num_reps = len([i for i in os.listdir(rep_folder) if os.path.isdir(".")])
    model_submodel(num_reps)
    trees(rep_folder, num_reps)
    partitions(num_reps)
    evolutions(num_reps, end_folder)

def model_submodel(n):
    for i in range(n):
        print("\n[MODEL] m" + str(i)+ "\n [submodel] JC")

def trees(fldr, n):
    for i in range(n):
        fpath = fldr + "/R%u/rose.mt"%i
        tree = dendropy.Tree.get(path=fpath, schema="newick")
        print("\n[TREE] T%u "%i + tree._as_newick_string(real_value_format_specifier=".6f")+";")

def partitions(n):
    for i in range(n):
        print("[PARTITIONS] p%u\n[T%u m%u 1000]"%(i,i,i))

def evolutions(n, outs):
    print("\n[EVOLVE] ")
    for t in range(n):
        print("p%u 1 "%t + outs + "/R%u/INDELible_rose"%t)

f=open("a_control.txt", "w")
make_control_file(sys.argv[1], sys.argv[2])
f.close()
