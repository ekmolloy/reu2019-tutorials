#!/bin/bash

for modl in "100M1" "100M2" "100M3"; do
    for repl in `seq -f "R%01g" 0 4`; do
        for dist in "P" "J"; do
            for tree in "B" "N"; do
                qsub -N "$modl-$repl-$dist-$tree" \
                     -v arg1="$modl",arg2="$repl",arg3="$dist",arg4="$tree"
                echo "Submitted $modl $repl $dist $tree"
            done
        done
    done
done
