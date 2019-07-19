#!/bin/bash

data="/projects/tallis/aditikg2/tutorials/4-all/data"
cntrl_fl="$data/example-control.txt"
fl_nm="control.txt"

for ((i=0;i<5;i++))
do
    for n in '0' 0.1 0.05 0.01 0.005 0.001
    do
	cp $cntrl_fl $fl_nm
	f=${n/'.'/'_'}

	repl_orig="../data/100M3/R$i/rose.mt"
	repl="../data/100M3/R$i/rose_$f.mt"
       	
	if [ $n == '0' ]
	then
	    repl=$repl_orig
	    sed -i "s/outputname/control_$i/g" $fl_nm
	else
	    python3 scale_tree.py $repl_orig $n
	    sed -i "s/outputname/control_${i}_${f}/g" $fl_nm
	fi
	
	fl=`cat $repl`
	sed -i "s/(A:0.1,B:0.1);/$fl/g" $fl_nm
	
	./indelible $fl_nm
	rm $fl_nm
    done
done
