#!/bin/bash
resPath="/projects/tallis/binghui2/reu2019-tutorials/raxml/EstimatedSeq/"
for dir in EstimatedSeq/*
do
	filename=$(echo $dir | cut -d'/' -f 2)
	treePath="$resPath$filename"
	fastme-2.1.5-linux64 -i $treePath/Estimated_TRUE.phy -O $treePath/estimatedMatrix.txt -d p
	fastme-2.1.5-linux64 -i uce_phylip/$filename.nexus.phylip -O $treePath/trueMatrix.txt -d p
done
