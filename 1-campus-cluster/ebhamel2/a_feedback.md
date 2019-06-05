- [ ] Use conditionals to check if the output files exist before running seqtools.py or FastME.
- [ ] Looping over `$data/*` does not work in general. I just uploaded an additional files to the `data` directory, which may cause your script to throw errors. Although we avoid "magic variables" when coding, it is perfectly okay to hardcode directory names when running computational experiments, for example, `for modl in "100M1" "100M2" "100M3"`.
- [ ] Remove `-u` option. IRL, we will not have access to the true tree topology, so we do not want to give the true tree to FastME as input.
- [ ] Right now, you are running FastME with 16 threads (default). Because we request 12 cores, let's specify the number of threads to be 12 (e.g., `-T 12`).
- [ ] Currently, you compute two trees (one with NJ and one with BioNJ) both given F84-corrected distances as input. You also compute two matrices one with p-distances and one with log-det distances. Revise the command so that you create four trees total by running NJ and BioNJ on matrices of p-distances and matrices of log-distances.
- [ ] Try to keep the length of each line shorter (under 80 characters or so) by dividing the command across on multiple lines
```
fastme-2.1.5-linux64-omp \
    -i $rep/rose.aln.true.phy \
    -o $output/NJ_on_p_dist_${entry}_${name}.tre \
    -m N --dna=p-distance
```
- [ ] Add some short comments.
