Tutorial 2: Working with phylogenetic datasets using Dendropy
=============================================================
***If you are in Champaign, you should be working on this assignment as a group between 3-6pm in 3401 Siebel Center. Although you may work together, each of you should write and commit your own code to Github. Any questions/issues with the tutorial should also be posted to slack in the channel #tutorials.***

You may do this tutorial on the campus cluster or on your laptop, as long as you write code that is compatible with Python v3.7.0 and [Dendropy v4.4.0](https://dendropy.org/).

In order to analyze phylogenetic datasets using Dendropy, you should read the [primer](https://dendropy.org/primer/index.html) and work through some of the examples, especially the sections on Taxon Namespaces and Trees. If you have not yet read Chapter 2 in Tandy's textbook, then it may be helpful to read this chapter as well. When you are done reading, you will be working on writing some code that uses dendropy. ***NOTE: I do not expect you to fully complete this tutorial today just commit the code that you have written at the end of the day.***

If you are working on the campus cluster, type
```
cd /projects/tallis/[YourNetID]/reu2019-tutorials/2-dendropy
mkdir [YourNetID]
cd [YourNetID]
vim sum_branch_lengths.py
```

This Python script should take as input a rooted tree with branch lengths (in newick format) and output a rooted tree with branch lengths (in newick format). However, the branch lengths in the output tree should be the distance between the branch and the root (including the branch length). For example, if the input tree was 
```
((((A:1,B:2):6,C:3):7,D:4):8,E:5);
```
then the output tree should be
```
((((A:22,B:23):21,C:18):15,D:12):8,E:5);
```

To add your script to the repository, type

```
git add sum_branch_lengths.py
git commit -m "Add a message here"
git push
You will be asked to enter your Github user name and password.
```

I would be surprised if you needed more work today, but if you do, then try to write a script that compares two trees in terms of their the branch lengths. Specifically, create a CSV file with the rows being bipartitions in the two trees, the first column being the length of the branch corresponding to the bipartition in tree 1, and the second column being the length of the branch corresponding to the bipartition in tree 2. If a bipartition is in tree 1 but not tree 2, then the length of the branch in tree 2 is `NA`. 

For example, if these are the two input trees
```
((A:7,(B:7,C:7):1):2,(D:7,E:7):3);
(((A:7,B:7):4,C:7):5,(D:7,E:7):6);
```

then the output should be

```
1,NA
NA,4
2,5
3,6
```

Note that the ordering of the rows does not matter.
