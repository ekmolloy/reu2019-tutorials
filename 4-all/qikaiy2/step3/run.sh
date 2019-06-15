for i in {0..4}
do
	for j in {0..5}
	do
		fastme-2.1.5-linux64-omp \
		-i /projects/tallis/qikaiy2/reu2019-tutorials/4-all/qikaiy2/alignment$i$j"_"TRUE.phy \
		-o /projects/tallis/qikaiy2/reu2019-tutorials/4-all/qikaiy2/step3/trees/tree$i$j.tre \
		-d J \
		-m N \
		-T 12
	done
done
