for i in {0..4}
do
	for j in {0..5}
	do
		echo -n 100M$i R$j K2P NJ
	        echo -n \
		python3 ../../tools/compare_trees.py \
		../../data/100M$i/R$j/rose.tt \
		../../data/100M$i/R$j/K_U_tree.tre
	        echo -n 100M$i R$j K2P BIONJ
		echo -n \
		python3 ../../tools/compare_trees.py \
		../../data/100M$i/R$j/rose.tt \
		../../data/100M$i/R$j/K_I_tree.tre
		echo -n 100M$i R$j LogDet NJ
		echo -n \
		python3 ../../tools/compare_trees.py \
		../../data/100M$i/R$j/rose.tt \
		../../data/100M$i/R$j/L_U_tree.tre
		echo -n 100M$i R$j LogDet BIONJ
	        echo -n	\
		python3 ../../tools/compare_trees.py \
		../../data/100M$i/R$j/rose.tt \
		../../data/100M$i/R$j/L_I_tree.tre
	done
done
