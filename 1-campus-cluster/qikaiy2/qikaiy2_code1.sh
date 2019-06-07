for i in {1..3}
do
	for j in {0..4}
	do
		fastme-2.1.5-linux64-omp -i ../../data/100M$i/R$j/rose.aln.true.phy -o ../../data/100M$i/R$j/K_U_tree.tre -d K -m U 
                fastme-2.1.5-linux64-omp -i ../../data/100M$i/R$j/rose.aln.true.phy -o ../../data/100M$i/R$j/K_I_tree.tre -p K -m I
                fastme-2.1.5-linux64-omp -i ../../data/100M$i/R$j/rose.aln.true.phy -o ../../data/100M$i/R$j/L_U_tree.tre -p L -m U
                fastme-2.1.5-linux64-omp -i ../../data/100M$i/R$j/rose.aln.true.phy -o ../../data/100M$i/R$j/L_I_tree.tre -p L -m I
	done
done
