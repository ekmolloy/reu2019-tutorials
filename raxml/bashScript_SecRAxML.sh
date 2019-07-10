#!/bin/bash
estimatedPath="/projects/tallis/binghui2/reu2019-tutorials/raxml/SecRAxML"
truePath="/projects/tallis/binghui2/reu2019-tutorials/raxml/SecRAxML"
resPath="/projects/tallis/binghui2/reu2019-tutorials/raxml/SecRAxML"
for estfile in EstimatedSeq/*
do
	realname=$(echo $estfile | cut -d'/' -f 2)
	mycommand1="./raxmlHPC-PTHREADS-SSE3 -s $estfile/Estimated_TRUE.phy -p 1 -w $resPath/$realname -m GTRGAMMA -T 12 -n Esti$realname"
	eval $mycommand1
done
#for truefile in uce_phylip/*
#do
#	filename=$(echo $truefile | cut -d'.' -f 1)
#	realname=$(echo $filename | cut -d'/' -f 2)
#	mycommand2="./raxmlHPC-PTHREADS-SSE3 -s $truefile -p 1 -w $resPath/$realname -m GTRGAMMA -T 12 -n TRUE$realname"
#	eval $mycommand2
#done
