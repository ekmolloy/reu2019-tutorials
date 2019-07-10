#!/bin/bash
echo "filename,RF-distance" >> all_RF_Distance.csv
for dir in SecRAxML/*
do
	dirname=$(echo $dir | cut -d'/' -f 2)
	estimated="$dir/RAxML_bestTree.Esti$dirname"
	truePath="$dir/RAxML_bestTree.TRUE$dirname"
	python3 pyScript_RF.py -t1 $estimated -t2 $truePath -f $dirname
done
