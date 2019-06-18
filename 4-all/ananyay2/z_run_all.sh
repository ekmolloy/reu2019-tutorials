#!/bin/bash

pwd
mkdir processed-data log-files

qsub a_run_control.pbs

echo "PART A DONE"

until [ -f t4-1* ]; do
	sleep 5
done
qsub b_run_control.pbs

echo "PART B DONE"

rm control.txt
rm indelible

mv trees.txt LOG.txt log-files/

until [ -f t4-2* ]; do
	sleep 5
done
qsub c_fastme.pbs

echo "PART C DONE"

until [ -f t4-3* ]; do
	sleep 5
done
qsub d_compare_fastme.pbs

echo "PART D DONE"

until [ -f t4-4* ]; do
	sleep 5
done
qsub e_boxplot.pbs

echo "PART E DONE"

until [ -f t4-5* ]; do
	sleep 5
done
qsub f_branch_csv.pbs

echo "PART F DONE"

until [ -f t4-6* ]; do
	sleep 5
done
python3 g_scatterplots.py branch-length.csv

echo "PART G DONE"

mv t4-* cluster-outputs/
mv *.txt log-files/

echo "finished."
