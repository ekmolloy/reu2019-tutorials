#!/bin/bash

raw_in='/projects/tallis/aditikg2/tutorials/aditikg2_project/data/Scincella/Scincella_SELT.nex'
in='/projects/tallis/aditikg2/tutorials/aditikg2_project/data/Scincella/Scincella_SELT.phy'
out='/projects/tallis/aditikg2/tutorials/aditikg2_project/output/heat_plot_out/Scincella/SELT_matrix.mat'
tools='/projects/tallis/aditikg2/tutorials/tools'

python3 $tools/seqtools.py -f p -i $raw_in -o $in
fastme-2.1.5-linux64-omp -i $in -dp -O $out