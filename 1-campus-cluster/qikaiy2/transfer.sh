for i in {1..3}
do
	for j in {0..4}
	do
		python3 seqtools.py -f p -i ../../data/100M$i/R$j/rose.aln.true.fasta -o ../../data/100M$i/R$j/rose.aln.true.phy
	done
done	
