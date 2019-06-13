**When you make one of these changes, add replace `-[ ]` with `-[X]` and commit this file.**

- [X] Use conditionals to check if the output files exist before running seqtools.py or FastME.
- [X] Try not to reset the environment variables, for example, `PBS_O_WORKDIR`. Either avoid using the variable `PBS_O_WORKDIR` like Emma did [here](https://github.com/ekmolloy/reu2019-tutorials/blob/master/1-campus-cluster/ebhamel2/a_run_fastme.pbs) or use the variable like Qikai did [here](https://github.com/ekmolloy/reu2019-tutorials/blob/master/1-campus-cluster/qikaiy2/a_run_fastme.pbs).
- [X] Looping over `$data/*` does not work in general. I just uploaded an additional files to the `data` directory, which may cause your script to throw errors. Although we avoid "magic variables" when coding, it is perfectly okay to hardcode directory names when running computational experiments, for example, `for modl in "100M1" "100M2" "100M3"`.
- [X] Remove `-u` option. IRL, we will not have access to the true tree topology, so we do not want to give the true tree to FastME as input.
- [X] Right now, you are running FastME with 16 threads (default). Because we request 12 cores, let's specify the number of threads to be 12 (e.g., `-T 12`).
- [X] Add some short comments.
