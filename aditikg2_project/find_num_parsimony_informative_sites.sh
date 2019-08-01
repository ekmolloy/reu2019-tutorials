#!/bin/bash

cur='/projects/tallis/aditikg2/tutorials/aditikg2_project'
paup='/projects/tallis/reu2019/software/paup-4a165/paup4a165_centos64'
data="$cur/data/Scincella"
files="$data/*.nex"
out="$cur/output/data_info_out/Scincella"

counter=0

for f in $files
do
    base=`basename $f`
    out_f="$out/$base.paup"
    echo "exe $f; cstatus; q;" | $paup > $out_f

    num_prsmny_info=`grep -F 'Number of parsimony-informative characters = ' $out_f`
    num_prsmny_info=${num_prsmny_info/'Number of parsimony-informative characters = '/''}

    if [ "$counter" -eq "0" ]
    then
	echo $num_prsmny_info > "$out/parsimony_info_sites_data"
    else
	echo $num_prsmny_info >> "$out/parsimony_info_sites_data"
    fi

    rm $out_f
    counter=$((counter + 1))
done
