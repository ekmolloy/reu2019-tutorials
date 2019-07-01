#!/bin/bash
matPath="/projects/tallis/binghui2/reu2019-tutorials/raxml/EstimatedSeq/"
echo "mean,median" >> boxplot.txt
for dir in EstimatedSeq/*
do
		
		filename=$(echo $dir | cut -d'/' -f 2)
		trueMat="$matPath$filename/trueMatrix.txt"
		estimatedMat="$matPath$filename/estimatedMatrix.txt"
		python3 pyScript_Matrix.py -t $trueMat -e $estimatedMat -o boxplot.txt
done
