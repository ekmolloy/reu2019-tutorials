#!/bin/bash
##randomly chosen
#filename="../astral/292RBBH_TRINITY_DN72_c0_g1_i1.phy"
#softwarePath="../../../reu2019/software/standard-RAxML-8.2.12/raxmlHPC-PTHREADS-SSE3"
#resPath="/projects/tallis/binghui2/reu2019-tutorials/raxml/treeResults"
#for file in uce_phylip/*
#do
#	filename=$(echo $file | cut -d'/' -f 2)	
#	mycommand="./raxmlHPC-PTHREADS-SSE3 -s $file -p 12345 -w $resPath -m GTRGAMMA -T 8 -n $filename"
#	eval $mycommand
#done
resPath="/projects/tallis/binghui2/reu2019-tutorials/raxml/Rooted_Results"
for file in uce_phylip/*
do 
	filename=$(echo $file | cut -d'.' -f 1)
	realname=$(echo $filename | cut -d'/' -f 2)
	#mycommand="./raxmlHPC-PTHREADS-SSE3 -s $file -p 12345 -w $resPath/$realname -m GTRGAMMA -T 12 -n $realname"
	#eval $mycommand
	mkdir $resPath/$realname
done
