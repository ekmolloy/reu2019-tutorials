#!/bin/bash
#PBS -N "tutorial-1-campus-cluster"
#PBS -W group_list=tallis
#PBS -q secondary
#PBS -l nodes=1:ppn=12
#PBS -l walltime="01:00:00"
#PBS -j oe
#PBS -M qikaiy2@illinois.edu
#PBS -m be

#cd $PBS_O_WORKDIR

path="/projects/tallis/qikaiy2/reu2019-tutorials/qikaiy2_project_1/output_data/aligns/GTRGAMMA"
cd ../../output_data/aligns/GTRGAMMA
files=$(find . -name "*.phy")

for file in $files
do
	fastme-2.1.5-linux64-omp \
	-i $path/$file \
	-O /projects/tallis/qikaiy2/reu2019-tutorials/qikaiy2_project_1/results/data/gtrgamma_dist/$file.mt \
	-d p \
	-T 12 
done
