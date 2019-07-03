#!/bin/bash
#python3 pyScript_Boxplot_updated.py -t EstimatedSeq/uce-128/trueMatrix.txt -e EstimatedSeq/uce-128/estimatedMatrix.txt -o matrix_diff/diff1.cs
#v -n uce-128
count=0
num=0
path="/projects/tallis/binghui2/reu2019-tutorials/raxml/EstimatedSeq/"
for dir in EstimatedSeq/*
do
	csvfile="/projects/tallis/binghui2/reu2019-tutorials/raxml/matrix_diff/box$num.csv"
	if [ $count -eq 0 ]
	then
		echo "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30" >> $csvfile
	fi
	dirname=$(echo $dir | cut -d'/' -f 2)
	estimated="$path$dirname/estimatedMatrix.txt"
	truepath="$path$dirname/trueMatrix.txt"
	python3 pyScript_Boxplot_updated.py -t $truepath -e $estimated -o $csvfile -n $dirname
	let count+=1
	if [ $count -eq 20 ]
	then
		count=0
		let num+=1
	fi
done
