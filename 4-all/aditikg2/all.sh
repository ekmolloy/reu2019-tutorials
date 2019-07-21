#!/bin/bash

sh 1_create_msa.sh
sh 3_create_tree.pbs
sh 4_compare_trees.pbs
sh 6_make_den_csv.pbs
