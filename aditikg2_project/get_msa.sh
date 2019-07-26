#!/bin/bash

cur="/projects/tallis/aditikg2/tutorials/aditikg2_project"
in="$cur/output/raxml_out/Scincella/*.bestTree"
control="$cur/input/indelible_in/Scincella/control.txt"

for f in $in
do
    python3 remove_tree_brnch_lngths.py $f
    tf=${f/'.bestTree'/'.bestTree.tre'}
    tree=`cat $tf`
    base=$(basename $f)
    out_nm=${base/'.bestTree'/''}
    
    cp $control "$cur/"
    sed -i "s/(A:0.1,B:0.1);/${tree}/g" "$cur/control.txt"
    sed -i "s/outputname/${out_nm}/g" "$cur/control.txt"

    "$cur/indelible" "$cur/control.txt"
    #rm "$cur/control.txt"
done
