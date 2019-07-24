#!/bin/bash

raxml='/projects/tallis/reu2019/software/raxml-ng-0.9.0/raxml-ng'
data='/projects/tallis/aditikg2/tutorials/aditikg2_project/data/Scincella'
files="$data/*.nex"

for i in $files
do
    python3 nex_to_phy.py $i
    phylip=${i/'.nex'/'.phylip'}
    msa=${phylip/'data'/'output'}
    $raxml --msa $msa --model GTR+G --threads 1 # Use 1 thread per 500 DNA sequences
done
