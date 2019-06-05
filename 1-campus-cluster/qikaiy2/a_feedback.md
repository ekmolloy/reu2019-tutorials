- [ ] Use conditionals to check if the output file `rose.aln.true.phy` exists before running seqtools.py and if the output file `K_U_tree.tre` exists before running FastME.
- [ ] Instead of writing the output files (alignments in phylip format and trees in newick format) are being written to `/projects/tallis/qikaiy2/reu2019-tutorials/data`, could you write them to `/projects/tallis/qikaiy2/reu2019-tutorials/1-campus-cluster/qikaiy2`?
- [ ] Add the commands from the `transfer.sh` script into the `a_run_fastme.pbs` that would be great! It is a good idea to keep commands for the same analysis together, so that we don't need to look through multiple files to understand how the analysis was performed.
- [ ] Try to keep the length of each line shorter (under 80 characters or so) by dividing the command across on multiple lines
```
fastme-2.1.5-linux64-omp \
    -d K -m U \
    -i /projects/tallis/qikaiy2/reu2019-tutorials/data/100M$i/R$j/rose.aln.true.phy \
    -o /projects/tallis/qikaiy2/reu2019-tutorials/data/100M$i/R$j/K_U_tree.tre
```
or using variables
```
datapath="/projects/tallis/qikaiy2/reu2019-tutorials/data/"

input="$datapath/100M$i/R$j/rose.aln.true.phy "
output="$datapath/100M$i/R$j/K_U_tree.tre"
fastme-2.1.5-linux64-omp -d K -m U -i $input -o $output
```
- [ ] Add some short comments.
