import dendropy
import numpy as np
import os
import sys
import string
from decimal import Decimal
import argparse

def matrix_builder(path):
	file = open(path)
	line = file.readline()
	num_line = int(line)
	res_Matrix = np.zeros([num_line,num_line])
	count = 0
	while count < num_line:
		line = file.readline()
		if not line:
			break
		list = line.split(" ")
		#print(list)
		for i in range(num_line*2):
			if i%2 == 1:       
				index = int(i/2)
				res_Matrix[count][index] = float(list[i])
		count = count + 1
	return res_Matrix


def main(args):
    true_path = args.true_Matrix
    estimated_path = args.estimated_Matrix
    output_path = args.output_path
    true_Mat = matrix_builder(true_path)
    estimated_Mat = matrix_builder(estimated_path)
    diff_Mat = true_Mat-estimated_Mat
    num = len(diff_Mat[0])
    diffset = diff_Mat[np.triu_indices(num)]
    file = open(output_path,"a+")
    file.write("%s,%s\n"%(np.mean(diffset),np.median(diffset)))
    #print(list)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="input path")
    parser.add_argument("-t","--true_Matrix",type=str,required=True)
    parser.add_argument("-e","--estimated_Matrix",type=str,required=True)
    parser.add_argument("-o","--output_path",type=str,required=True)
    main(parser.parse_args())
