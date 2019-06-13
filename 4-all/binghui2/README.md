**When you make one of these changes, add replace `-[ ]` with `-[X]` and commit this file.**

- [ ] Re-do steps 1, 2, and 3 so that the file structure is easily understandble for a reviewer of your paper. I would suggest making a folder called `output-data` and then replicating the directory structure of the input data.

For example,

```
/projects/tallis/[YourUserName]/reu2019-tutorials/4-all/data/100M3/R0/rose.mt
```
then your output data (control file, alignment, and fastme tree) should be written to
```
/projects/tallis/[YourUserName]/reu2019-tutorials/4-all/[YourUserName]/output-data/100M3/R0
```

Alternatively, you create a folder called `alignments` and a folder called `fastme-trees`. Then if your input is 
```
/projects/tallis/[YourUserName]/reu2019-tutorials/4-all/data/100M3/R0/rose.mt
```
you could write the control file and alignment to 
```
/projects/tallis/[YourUserName]/reu2019-tutorials/4-all/[YourUserName]/alignments/100M3/R0
```
and you could write the fastme files to 
```
/projects/tallis/[YourUserName]/reu2019-tutorials/4-all/[YourUserName]/fastme-trees/100M3/R0
```
- [ ] Write a README file for your data (e.g., `output-data/README.txt`); see example [here](https://databank.illinois.edu/datasets/IDB-1424746)
- [ ] Tar Gz the `output-data` directory and email it to me. This is what would happen in an actually publication, because I would need to upload this .tar.gz file to the Illinois Data Bank.
- [ ] In Step 3, it would nice if you saved the output of fastme in the same place that you saved the tree.
```
fastme-2.1.5-linux64-omp -i $name -o $resfile.tre -m U -d J -T 12 &> $resfile.log
```
- [ ] I don't think that you are running neighbor joining in Step 3. I think this should be `-m N`.
- [ ] It's hard for me to believe that your code for Step 6 is working.
For example,
```
100M3   R0.0    0.1 JC  NJ  0.392827364409  3.25933608693   17.5541 118.183
```
means that there is a branch of length `175.541` in the tree `data/100M3/R0/rose.mt`, because `175.541 * 0.1 = 17.5541`. However, this does not seem to be the case. I did
```
import dendropy
import numpy
tree = dendropy.Tree.get(path="reu2019-tutorials/data/100M3/R0/rose.mt",
                         schema="newick")
edges = [ e.length for e in tree.preorder_edge_iter() ]
edges = numpy.array(edges)
numpy.sort(edges)
```
And did not find a branch with length `175.541`.
- [ ] For figures, I would make sure all of the axes are labeled, the meaning of red / black dots, etc. Also, I would write a few sentences about what you think the figure means.
