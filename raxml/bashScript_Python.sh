#!/bin/bash
resPath="/projects/tallis/binghui2/reu2019-tutorials/raxml/RAxML_Results/"
for dir in RAxML_Results/*
do
	dir_name=$(echo $dir | cut -d'/' -f 2)
	pathname="$resPath$dir_name"
	info_filename="RAxML_info.$dir_name"
	tree_filename="RAxML_bestTree.$dir_name"
	python3 pyScript.py -i $pathname/$info_filename -t $pathname/$tree_filename -o $dir_name
	#echo $dir_name
done
