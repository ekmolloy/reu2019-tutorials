import sys
import os 

input_loc = sys.argv[1]
output_loc = sys.argv[2]


def get_num(filename):
    return filename[filename.find("raxml-") + 6 : filename.find("_a-out")]

def get_gtr_nums(n):
    a=1
    b=1
    c=1
    d=1
    e=1
    f=1
    alpha=1
    freqt=1
    freqa=1
    freqg=1
    freqc=1
    filename = input_loc+"/info/RAxML_info.raxml-%s_a-out.phylip"%n
    with open(filename, 'r') as file:
        for line in file:
            line = line.rstrip()
            if "alpha: " in line:
                alpha=float(line[7:])
            elif "rate A <-> C: " in line:
                d=float(line[14:])
            elif "rate A <-> G: " in line:
                f=float(line[14:])
            elif "rate A <-> T: " in line:
                b=float(line[14:])
            elif "rate C <-> G: " in line:
                e=float(line[14:])
            elif "rate C <-> T: " in line:
                a=float(line[14:])
            elif "rate G <-> T: " in line:
                c=float(line[14:])
            elif "freq pi(A): " in line:
                freqa=float(line[12:])
            elif "freq pi(C): " in line:
                freqc=float(line[12:])
            elif "freq pi(G): " in line:
                freqg=float(line[12:])
            elif "freq pi(T): " in line:
                freqt=float(line[12:])
    
    return [a/f, b/f, c/f, d/f, e/f, alpha, freqt, freqg, freqa, freqc]

def tree(files):
    for f in files:
        tree = ""
        with open(input_loc+"/best-tree/" + f, 'r') as content_file:
            tree = content_file.read()
        print("[TREE] T%s %s\n"%(get_num(f), tree[:-6]+";"))

def model_submodel(files):
    for f in files:
        n = get_num(f)
        nums = get_gtr_nums(n)
        print("\n[MODEL] m%s \n [submodel] GTR    %f %f %f %f %f \n [rates] 0 %f 0\n [statefreq] %f %f %f %f"%(n, nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7], nums[8], nums[9]))


def partitions(files):
    for i in range(len(files)):
        tree_num = int(get_num(files[i]))
        print("[PARTITIONS] p%u\n[T%u m%u 1000]"%(tree_num,tree_num,tree_num))

def evolutions(files, end_folder):
    print("\n[EVOLVE]")
    for f in files:
        tree_num = get_num(f)
        print("\np%s 1 %sindelible-%s"%(tree_num, end_folder, tree_num))

def make_control_file(files, end_folder):
    num_reps = len(files)
    print("[TYPE] NUCLEOTIDE 1")
    model_submodel(files)
    tree(files)
    partitions(files)
    evolutions(files, end_folder)


fils = []
for subdir, dirs, files in os.walk(input_loc+"/best-tree/"):
    fils = files
make_control_file(fils, output_loc)
