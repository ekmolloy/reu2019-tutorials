Tutorial 4: Putting it all together
====================================
**If you are in Champaign, you should be working on this assignment as a group between 9am-12pm and 3-6pm in 3401 Siebel Center. If you do not have a github account, please make one now and share your Github user name on slack . Any questions/issues with the tutorial should also be posted to slack in the channel #tutorials.**

In order to complete this assignment, you will need to access the Campus Cluster remotely. 

```
ssh [YourNetId]@golub.campuscluster.illinois.edu
/projects/tallis/[YourNetID]/reu2019-tutorials/4-all
mkdir [YourNetID]
cd [YourNetID]
```

In this assignment, you will be running a computational experiment to evaluate the impact of branch length on gene tree estimation using Neighbor Joining.

In order to run these experiments, you will need to do the following steps.

1. Write a bash script that uses INDELible to generate multiple sequence alignments for each model tree in `/projects/tallis/[YourUserName]/reu2019-tutorials/4-all/data/100M3/` (5 replicates). Specifically, replace `[TREE] treename  (A:0.1,B:0.1);` in [`example-control.txt`](data/example-control.txt) with the model tree for each replicate dataset, labelled `rose.mt`. Note that in order to run INDELible, you need to copy the binary `/projects/tallis/reu2019/software/INDELibleV1.03/src/indelible` into the same directory as the control file. You should submit this as a job to the campus cluster; it should run in less than 5 minutes.

2. Write a bash script and python script (optional) that repeats a modified version of Step 1. SPecifically, it should modify the branch lengths of the tree in [`rose.mt`](/projects/tallis/[YourUserName]/reu2019-tutorials/4-all/data/100M3/R0/rose.mt) (maybe write a Python script) by multiple each of the branch lengths with the following numbers: 0.1, 0.05, 0.01, 0.005, and 0.001. The first two steps will produce 6 model conditions (1 for each of the scaling factors) each with 5 replicate datasets (30 datasets total). You should submit this as a job to the campus cluster; it should run in ~10 minutes. If you may want to write a tool in Python (that scales the branch lengths and writes the INDELible control file) that your bash script can run.

3. Write a bash script that runs Neighbor Joining on each of these datasets (30 total) using FastME (`fastme-2.1.5-linux64`) with Jukes-Cantor (JC) corrected distances. You should submit this as a job to the campus cluster; it should run in ~15 minutes.

4. Write a bash script that uses the [`compare_trees.py`](../tools/compare_trees.py) script to create a CSV file with the following columns.

```
MODL,REPL,MULT,DIST,TREE,NL,I1,I2,FP,FN,RF
```

where

+ `MODl` is the model condition (`100M3`)
+ `REPL` is the replicate number (`R0`, `R1`, `R2`, `R3`, `R4`)
+ `MULT` is the muliplier (0.1, 0.05, 0.01, 0.005, and 0.001)
+ `DIST` is the method used to compute distances between pairs of sequences (`JC`)
+ `TREE` is the method used to estimate a tree from the distance matrix (`NJ`)
+ `NL,I1,I2,FP,FN,RF` are the output of [`compare_trees.py`](../tools/compare_trees.py)

5. Write a Python script to create a boxplot of the RF error rate each model condition. How is accuracy impacted by the branch length multiplier?

6. Write a Python script to create a scatter plot with the following properties. Each point in the scatterplot represents a bipartition (and branch) in the estimated tree with the x-axis being the length of the branch and the y-axis being the depth of the branch, that is, the sum of branch lengths going from the root to (and including) that branch. Color the dot black if the bipartition is in the true tree and color the dot red if the bipartition is NOT in the true tree. Note that if you have not finished the tutorial on Dendropy; you should do that first. Plot the bipartitions from the first replicate for each model condition (in the same figure). How is accuracy impacted by the branch length and branch depth?

If you still have time, you write up a list of questions / comments that you want to discuss during my office hours or during our group meetings next week. You may also want to work on any homework assignments from Tandy or improving the assignments (especially the Python code) from this week (e.g., writing more test cases, adding docstrings to document functions, using pycodestyle/pep8 to format the code, etc). Finally, please message me the number of hours that you worked this week. I know that each of you was in the tutorials for 18 hours this week, but some of you may have worked more hours. Also, don't forget to submit the hours to the time system. Hope you have a great weekend!!!!!
