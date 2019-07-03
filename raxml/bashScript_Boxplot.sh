#!/bin/bash
#python3 pyScript_Boxplot_updated.py -t EstimatedSeq/uce-128/trueMatrix.txt -e EstimatedSeq/uce-128/estimatedMatrix.txt -o matrix_diff/diff1.cs
#v -n uce-128
count=0
num=0
path="/projects/tallis/binghui2/reu2019-tutorials/raxml/EstimatedSeq/"
for dir in EstimatedSeq/*
do
	dirname=$(echo $dir | cut -d'/' -f 2)
	csvfile="/projects/tallis/binghui2/reu2019-tutorials/raxml/matrix_diff/box$num.csv"
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
