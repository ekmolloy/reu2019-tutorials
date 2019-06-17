array=('1' '0.1' '0.05' '0.01' '0.005' '0.001')
h=(' ')
echo MODL REPL MULT DIST TREE NL I1 I2 FP FN RF
for j in {0..4}
do
	for k in {0..5}
	do
		echo -n 100M3 R$j ${array[k]} JC NJ 
		echo -n \ ${h[0]}
		python3 ../../../tools/compare_trees.py \
		../../../data/100M3/R$j/rose.tt \
		../data/tree/tree$j$k.tre
	done
done
