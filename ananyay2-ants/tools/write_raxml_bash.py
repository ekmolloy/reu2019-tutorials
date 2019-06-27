import sys
import os

set_num = sys.argv[1]

in_location = sys.argv[2]
out_location = sys.argv[3]

files = [f for f in listdir(in_location) if isfile(join(in_location, f))]

print("#!/bin/bash")
print("#PBS -N \"raxml-%s\""%num)
print("#PBS -W group_list=tallis")
print("#PBS -q secondary")
print("#PBS -l nodes=1:ppn=28")
print("#PBS -l walltime=03:00:00")
print("#PBS -j oe")
print("#PBS -M ananyay2@illinois.edu")
print("#PBS -m be")

print("jobloc=\"/projects/tallis/ananyay2/ants/environment-%s\""%num)

print("cd %s"%out_location)

for i in range(num * num_files, min((num+1)*num_files, len(files))):
    f = files[i]
    print("raxmlHPC-PTHREADS-SSE3 -T 28 -m GTRGAMMA -f a -# 200 -p 12345 -x 12345 -s ../original/%s -n %s-out.phylip"%(f,f))
    

