import os
import string
import numpy as np
import argparse
import dendropy
import decimal
ctx = decimal.Context()
ctx.prec = 20

def float_to_str(f):
	"""
	Convert the given float to a string,
	without resorting to scientific notation
	"""
	d1 = ctx.create_decimal(repr(f))
	return format(d1, 'f')

def branch_lengths_2_decimals(str_newick_tree):
	"""replaces branch lengths in scientific notation with decimals"""
	colon_s = 0
	#comma_back_paren_s = 0
	num = ''
	new_tree = ''
	for count, char in enumerate(str_newick_tree):
		if char == ':':
			colon_s = count
			continue
		if char in (')', ','):
			#comma_back_paren_s = 1
			num = float_to_str(float(num)) 
			new_tree += ":" + num
			colon_s = 0
			num = ''
		if colon_s != 0:
			num = num + char
		if colon_s == 0:
			new_tree += char		
	new_tree = new_tree.strip('\'').strip('\"').strip('\'') + ";"
	return new_tree


####Reference: The functions above are from Qikai's code
####which is the combination of the following 2 sources
####source1:https://codeday.me/bug/20171224/112503.html
####source2:https://github.com/faircloth-lab/phyluce/blob/master/bin/genetrees/phyluce_genetrees_phybase
def sumToOne(baseArray):
	total = 0
	for i in range(4):
		total += float(baseArray[i+1])
	if total == 1:
		return baseArray
	else:
		factor = 1/total
		for i in range(4):
			baseArray[i+1] = float(baseArray[i+1])*factor
		return baseArray




def InfoParser(infoPath):
	file = open(infoPath)
	#orderArray = [None] * 6
	orderArray = np.zeros(6)
	#baseArray = [None] * 4
	baseArray = np.zeros(4)
	order = True
	base = True
	while order or base:
		line = file.readline()
		if not line:
			break
		list = line.split(':')
		if "alpha[0]" in list[0]:
			numlist = list[2].split(" ")
			numarray = np.asarray(numlist)
			#numarray = numlist
			orderArray[3] = numarray[1]
			orderArray[5] = numarray[2]
			orderArray[1] = numarray[3]
			orderArray[4] = numarray[4]
			orderArray[0] = numarray[5]
			orderArray[2] = numarray[6]
			factor = 1/(orderArray[5])
			orderArray = factor*orderArray
			order = False
		if "Base frequencies" in list[0]:
			freqlist = list[1].split(" ")
			baseArray = np.asarray(freqlist)
			baseArray = sumToOne(baseArray)
			#baseArray = list[1]
			base = False
	return (baseArray,orderArray) 
    #print("Something is wrong here!")
    #return None

def main(args):
	resPath = "/projects/tallis/binghui2/reu2019-tutorials/raxml/RAxML_Results"	
	inputTree = dendropy.Tree.get(path=args.tree,schema="newick")
	mrca = inputTree.mrca(taxon_labels=["cardinalis cardinalis ku21828", "cardinalis cardinalis ku25393"])
	inputTree.reroot_at_node(mrca, update_bipartitions=False)
	treeString = "%s"%(inputTree)
	#print(treeString)
	treeString = branch_lengths_2_decimals(treeString)
	#contents = inputTree.as_string(format="newick")
	#treePath = args.tree
	#treefile = open(treePath,"r")
	#contents = treefile.read()
	infoPath = args.info
	output_name = args.output_name
	
	file = open("%s/%s/control.txt"%(resPath,output_name),"w+")
	file.write("[TYPE] NUCLEOTIDE 1\n")
	file.write("[MODEL] mymodel\n")
	[baseArray,orderArray] = InfoParser(infoPath)
	file.write("\t[submodel] GTR %s %s %s %s %s\n"%(float_to_str(float(orderArray[0])),float_to_str(float(orderArray[1])),
	float_to_str(float(orderArray[2])),float_to_str(float(orderArray[3])),float_to_str(float(orderArray[4]))))
	file.write("\t[statefreq] %s %s %s %s\n"%(baseArray[1],baseArray[2],baseArray[3],baseArray[4]))
	file.write("[TREE] tree1 %s\n"%(treeString))
	file.write("[PARTITIONS] p0\n")
	file.write("\t[tree1 mymodel 2000]\n")
	file.write("[EVOLVE]\n")
	file.write("\tp0 1 EstimatedSeq/%s/Estimated\n"%(output_name))
	file.close()


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="input path name")
	parser.add_argument("-i","--info",type=str,required=True)
	parser.add_argument("-t","--tree",type=str,required=True)
	parser.add_argument("-o","--output_name",type=str,required=True)
	main(parser.parse_args())

