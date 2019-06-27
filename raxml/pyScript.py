import os
import string
import numpy as np
import argparse

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
			#baseArray = list[1]
			base = False
	return (baseArray,orderArray) 
    #print("Something is wrong here!")
    #return None

def main(args):
	treePath = args.tree
	treefile = open(treePath,"r")
	contents = treefile.read()
	infoPath = args.info
	output_name = args.output_name
	file = open("control.txt","w")
	file.write("[TYPE] NUCLEOTIDE 1\n")
	file.write("[MODEL] mymodel\n")
	[baseArray,orderArray] = InfoParser(infoPath)
	file.write("\t[submodel] GTR %s %s %s %s %s %s\n"%(orderArray[0],orderArray[1],orderArray[2],orderArray[3],orderArray[4],orderArray[5]))
	file.write("\t[statefreq] %s %s %s %s\n"%(baseArray[1],baseArray[2],baseArray[3],baseArray[4]))
	file.write("[TREE] tree1 %s"%(contents))
	file.write("[PARITITIONS] p0\n")
	file.write("\t[tree1 mymodel 2000]\n")
	file.write("[EVOLVE]\n")
	file.write("\tp0 1 EstimatedSeq/%s/Estimated"%(output_name))
	file.close()


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="input path name")
	parser.add_argument("-i","--info",type=str,required=True)
	parser.add_argument("-t","--tree",type=str,required=True)
	parser.add_argument("-o","--output_name",type=str,required=True)
	main(parser.parse_args())

