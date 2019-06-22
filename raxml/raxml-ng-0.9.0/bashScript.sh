#!/bin/bash
##randomly chosen
#filename="../astral/292RBBH_TRINITY_DN72_c0_g1_i1.phy"
mycommand="./raxml-ng --msa ../astral/genePHYLIPs/292RBBH_TRINITY_DN72_c0_g1_i1.phy --prefix treeResults/output --model GTR+G --bs-trees 100 -threads 2"
eval $mycommand
