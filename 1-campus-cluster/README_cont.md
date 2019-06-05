Tutorial 1: Running batch analyses on the Campus Cluster, cont.
===============================================================
If you are in Champaign, you should be working on this assignment as a group between 9-11:20am in 3401 Siebel Center. Please go to 2405 Siebel Center by 11:30am for the weekly lunch seminar --- yay free lunch!

Everyone did a great job yesterday! I am so pleased with all of your progress -- epsecially in my absence! Before moving on to the next activity, we are going to be making some modifications to the scripts that we wrote yesterday.

**Ananya and Emma**: If you could clone this repository that would be great! I already added your scripts from yesterday. This will make it easier for me to see what you both are doing and it will make it easier for both of you to access the latest version of this repository.

Before you beginning this tutorial, take a look at your feedback: [Ananya](ananyay2/a_feedback.md), [Alan](binghui2/a_run_fastme.pbs), [Emma](ebhamel2/a_feedback.md), [Qikai](qikaiy2/a_feedback.md). You may want to edit your scripts before or after working on this tutorial.

To pull the latest changes to the repository, type

```
cd /projects/tallis/[YourUserName]/reu2019-tutorials
git pull
```

and to create a new file, type

```
cd 1-campus-cluster/[YourUserName]
vim b_compare_fastme_trees.pbs
```

At the top of this file, copy the following text

```
#!/bin/bash
#PBS -N "tutorial-1-campus-cluster"
#PBS -W group_list=tallis
#PBS -q secondary
#PBS -l nodes=1:ppn=12
#PBS -l walltime=00:10:00
#PBS -j oe
#PBS -M [YourNetID]@illinois.edu
#PBS -m be
```

Below these lines, write a bash script to run that uses [`compare_trees.py`](../tools/compare_trees.py) to compare the true tree to the estimated trees. Specifically, the script should output a CSV file, called `fastme.csv`, with the following header column:

```
MODL,REPL,DIST,TREE,NL,I1,I2,FP,FN,RF
```

where

+ `MODl` is the model condition (`100M1`, `100M2`, `100M3`)
+ `REPL` is the replicate number (`R0`, `R1`, `R2`, `R3`, `R4`)
+ `DIST` is the method used to compute distances between pairs of sequences
+ `TREE` is the method used to estimate a tree from the distance matrix
+ `NL,I1,I2,FP,FN,RF` are the output of [`compare_trees.py`](../tools/compare_trees.py)

Yesterday, you estimated four different trees on each of the fifteen dataset, so your CSV file should have 4 * 5 * 3 + 1 = 61 lines. To check the number of lines in your CSV file, type

```
wc -l fastme.csv
```

Suppose that FastME failed on the first replicate dataset for the first model condition when you ran it uses p-distances and Neighbor Joining. Then your CSV file should include the following row:

```
100M1,R0,P,NJ,NA,NA,NA,NA,NA,NA
```

To see a list of failures, type

```
grep "NA$" fastme.csv
```

When you finish writing your script, submit it as a job to the Campus Cluster queue; type

```
qsub b_compare_fastme_trees.pbs
```

To see that your job has been submitted, type

```
qstat -u [YourNetID]
```

To add your script to the repository, type

```
git add b_compare_fastme_trees.pbs
git commit -m "Add a message here"
git push
```

You will be asked to enter your Github user name and password.
