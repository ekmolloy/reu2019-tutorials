import dendropy
import sys

def make_control_file(f, rep_folder):
    scales=[1.0, 0.1, 0.05, 0.01, 0.005, 0.001]
    f.write("[TYPE] NUCLEOTIDE 1\n")
    model_submodel(f, 5*len(scales))
    tree(f, rep_folder, scales)
    partitions(f, 5*len(scales))
    evolutions(f, scales)

def model_submodel(f, n):
    for i in range(n):
        f.write("[MODEL] m" + str(i)+"\n")
        f.write("[submodel] JC\n")

def tree(f, rep_folder, scales):
    for t in range(5):
        filepath = rep_folder + "R" + str(t) + "/rose.mt"
        print(rep_folder)
        print(filepath)
        for j in range(len(scales)):
            tree = dendropy.Tree.get(path=filepath, schema="newick")
            tree.scale_edges(scales[j])
            p=rep_folder+"R"+str(t)+"/" + str(scales[j]).replace(".","-") + ".tt"
            tree.write(path=p, schema="newick", real_value_format_specifier=".6f")
            f.write("[TREE] T"+str((t*len(scales))+j) + " " + p + "\n")

def partitions(f, n):
    for i in range(n):
        f.write("[PARTITIONS] p" + str(i) + "\n")
        f.write("[T" + str(i) + " m" + str(i) + " 1000]\n")

def evolutions(f, scales):
    f.write("[EVOLVE] ")
    for t in range(5):
        for j in range(len(scales)):
            f.write("p" + str((t*len(scales)) + j) + " 1 scaled-outputs/100M3R" + str(t) + "S" + str(scales[j]).replace(".","-") + "\n")
            



f = open("part2-control.txt", "w")
make_control_file(f, sys.argv[1])
f.close()


