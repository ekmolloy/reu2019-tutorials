Tutorial 1: Campus Cluster
==========================
**If you are in Champaign, you should be working on this assignment as a group between 3-6pm in 3401 Siebel Center. Although you may work together, each of you should write and commit your own script to Github. Message the group slack in channel #tutorials with any questions/issues.**

In order to complete this assignment, you will need to access the Campus Cluster remotely. If you are using a Windows system, you may need to download an application for this purpose. If you are using a Mac or Linux system, then you can remotely access the Campus Cluster; just open the terminal the [Terminal](https://en.wikipedia.org/wiki/Terminal_(macOS)) application and type

```
ssh [YourNetId]@golub.campuscluster.illinois.edu
```

To see your present working directory, type

```
pwd
```

The output should be your home directory on the Campus Cluster: `/home/[YourNetID]`.

In the assignment, we will be running a software package called [FastME](http://www.atgc-montpellier.fr/fastme/). To see the help message for FastME, type

```
fastme-2.1.5-linux64-omp -h
```

The output should include `command not found`. This means that you need to specify *where* the FastME software is installed on the Campus Cluster by updating the `PATH` variable in your bash profile. To edit the bash profile using [vim](https://www.vim.org), type

```
module load vim
vim ~/.bash_profile
```

Press the "i" key to insert text, and then copy the following lines at the end of your bash profile.

```
# Modules to load automatically
module load vim
module load git

# Paths to phylogenetic software packages
PATH="/projects/tallis/reu2019/software/fastme-2.1.5/binaries/:$PATH"
```

To save these updates, press the following keys: ":" and "w" and "q". The "w" key writes (i.e., saves) the file and the "q" key quits vim. At this point, you should have updated your bash profile and exited vim. When you log onto the Campus Cluster, your bash profile is automatically sourced. Because you just edited your bash profile, you need to manually source it; type

```
source ~/.bash_profile
```

To see the path to the FastME software (i.e., *where* the FastMe software is installed on the Campus Cluster), type

```
which fastme-2.1.5-linux64-omp
```

The output should match the `PATH` variable in your bash profile, i.e., `/projects/tallis/reu2019/software/fastme-2.1.5/binaries/fastme-2.1.5-linux64-omp`. I have installed several phylogenetic software packages for the REU program in `/projects/tallis/reu2019/software/`. If you need to use software that is not currently installed in this directory, please ask me to install it for you; please do not install any software on the Campus Cluster! Now make a second attempt to see the help message for FastME; type

```
fastme-2.1.5-linux64-omp -h
```

The first line of the output should be ``. You will be completing this assignment in the TALLIS project directory. To change directories, type

```
cd /projects/tallis/reu2019-tutorials/1-campus-cluster
```

To see the files/directories that are in your tutorial directory, type

```
ls
```

The output should include the directory `data`. 
