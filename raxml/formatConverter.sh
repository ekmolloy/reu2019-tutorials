#!/bin/bash
for file in uce_nexus/*
do
		filename=$(echo $file | cut -d'/' -f 2)
		python ../tools/seqtools.py -f phylip -i $file -o uce_phylip/$filename.phylip
done
