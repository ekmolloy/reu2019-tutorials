#!/bin/bash
resPath="/projects/tallis/binghui2/reu2019-tutorials/raxml/Rooted_Results/"
readPath="/projects/tallis/binghui2/reu2019-tutorials/raxml/"
for result in RAxML_Results/*
do
	filename=$(echo $result | cut -d'/' -f 2)
	input="$readPath$result/RAxML_bestTree.$filename"
	output="$resPath$filename/rootedBestTree.$filename"
	python3 pyScript_Root.py -t $input -o $output
done
