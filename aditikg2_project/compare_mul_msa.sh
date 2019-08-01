#!/bin/bash

cur='/projects/tallis/aditikg2/tutorials/aditikg2_project'
msa1="$cur/data/Scincella/*.nex"
msa2="$cur/output/indelible_out/Scincella"
out="$cur/output/data_info_out/Scincella"

counter=0

for f in $msa1
do
    base=`basename $f`
    f2=${base/'.nex'/'.phylip.raxml_TRUE.phy'}
    f2="$msa2/$f2"
    
    if [ $counter -eq '0' ]
    then
	python3 compare_msa.py $f $f2 > "$out/msa_diff"
    else
	python3 compare_msa.py $f $f2 >> "$out/msa_diff"
    fi

    counter=$((counter + 1))
done