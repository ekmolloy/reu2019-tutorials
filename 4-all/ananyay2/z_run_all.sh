#!/bin/bash

qsub a_run_control.pbs

until [ -f t4-1* ]; do
	sleep 5
done
qsub b_run_control.pbs

rm control.txt
rm indelible

mv trees.txt LOG.txt output-files/

until [ -f t4-2* ]; do
	sleep 5
done
qsub c_fastme.pbs

until [ -f t4-3* ]; do
	sleep 5
done
qsub d_compare_fastme.pbs

until [ -f t4-4* ]; do
	sleep 5
done
qsub e_boxplot.pbs

until [ -f t4-5* ]; do
	sleep 5
done
qsub f_branch_csv.pbs

until [ -f t4-6* ]; do
	sleep 5
done
mv t4-* cluster-outputs/
