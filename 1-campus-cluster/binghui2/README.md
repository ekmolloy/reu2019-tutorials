**When you make one of these changes, add replace `-[ ]` with `-[X]` and commit this file.**

- [ ] Use conditionals to check if the output files exist before running seqtools.py or FastME.
- [X] Instead of writing the output files (alignments in phylip format and trees in newick format) are being written to `/projects/tallis/binghui2/reu2019-tutorials/data`, could you write them to `/projects/tallis/binghui2/reu2019-tutorials/1-campus-cluster/binghui2`?
- [X] Try not to reset the environment variables, for example, `PBS_O_WORKDIR`. Either avoid using the variable `PBS_O_WORKDIR` like Emma did [here](https://github.com/ekmolloy/reu2019-tutorials/blob/master/1-campus-cluster/ebhamel2/a_run_fastme.pbs) or use the variable like Qikai did [here](https://github.com/ekmolloy/reu2019-tutorials/blob/master/1-campus-cluster/qikaiy2/a_run_fastme.pbs).
- [X] Right now, you are running FastME with 16 threads (default). Because we request 12 cores, let's specify the number of threads to be 12 (e.g., `-T 12`).
- [X] Try to keep the length of each line shorter (under 80 characters or so) by dividing the command across on multiple lines
```
fastme-2.1.5-linux64-omp \
    -m N -d L \
    -i ../../data/100M$i/R$j/rose.aln.true.phy \
    -o ../../data/NJ+LogDetM$i$j
```
or using variables
```
input="../../data/100M$i/R$j/rose.aln.true.phy"
output="../../data/NJ+LogDetM$i$j"
fastme-2.1.5-linux64-omp -m N -d L -i $input -o $output
```
- [ ] Add some short comments.
