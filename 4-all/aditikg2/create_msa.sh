#!/bin/bash

data="/projects/tallis/aditikg2/tutorials/4-all/data"
cntrl_fl="$data/example-control.txt"

for ((i=0;i<5;i++))
do
    fl_nm="control_$i.txt"
    cp $cntrl_fl $fl_nm

    repl="$data/100M3/R$i/rose.mt"
    fl=`cat $repl`
    
    sed -i "s/(A:0.1,B:0.1)/$fl/g" $fl_nm
done
