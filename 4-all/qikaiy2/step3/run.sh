for i in {0..4}
do
	for j in {0..5}
	do
		fastme-2.1.5-linux64-omp \
		-i ../data/align/alignment$i$j"_"TRUE.phy \
		-o ../data/tree/tree$i$j.tre \
		-d J \
		-m N \
		-T 12
	done
done
