import dendropy
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import sys
from enum import Enum
import datetime
class Column_ID(Enum):
	MODL = 0
	NTAX = 1
	NGEN = 2
	TRLN = 3
	REPL = 4
	DATA = 5
	MTHD = 6
	SMAX = 7
	DMAT = 8
	STRE = 9
	SENL = 10
	SEI1 = 11
	SEI2 = 12
	SEFP = 13
	SEFN = 14
	SERF = 15
	TIME = 16

def ils_bar_grapher(method1, method2):
	N = 2
	ind = np.arange(N)  # the x locations for the groups
	width = 0.35       # the width of the bars

	fig = plt.figure()
	ax = fig.add_subplot(111)

	method1_values = get_comprehensive_ils_mean_from_method(method1)
	method1_stds = get_comprehensive_ils_std_from_method(method1)
	rects1 = ax.bar(ind, method1_values, width, yerr=method1_stds, color='b')
	method2_values = get_comprehensive_ils_mean_from_method(method2)
	method2_stds = get_comprehensive_ils_std_from_method(method2)
	rects2 = ax.bar(ind+width, method2_values, width, yerr=method2_stds, color='g')

	ax.set_ylabel('Species Tree Error')
	ax.set_xticks(ind+width)
	plt.yticks(np.arange(0, 1, step=0.1))
	ax.set_xticklabels(('Low/Mod ILS \n n=20, 20', 'High ILS \n n=20, 20'))
	ax.legend((rects1[0], rects2[0]), (method1, method2))

	autolabel(rects1, ax)
	autolabel(rects2, ax)

	plt.show()

def autolabel(rects, ax):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

def ils_boxplot_grapher(method1, method2):
	data1 = make_numpy_array(csv_file_reader("/Users/emmahamel/Research/Phylogeny/tutorials/data-species-trees.csv", "10M", method1, Column_ID.SERF),
		csv_file_reader("/Users/emmahamel/Research/Phylogeny/tutorials/data-species-trees.csv", "10M", method2, Column_ID.SERF))

	print(data1)
	data2 = make_numpy_array(csv_file_reader("/Users/emmahamel/Research/Phylogeny/tutorials/data-species-trees.csv", "500K", method1, Column_ID.SERF),
		csv_file_reader("/Users/emmahamel/Research/Phylogeny/tutorials/data-species-trees.csv", "500K", method2, Column_ID.SERF))

	fig, ax = plt.subplots()
	bp1 = ax.boxplot(data1, positions=[1,4], widths=0.35)
	bp2 = ax.boxplot(data2, positions=[2,5], widths=0.35)

	ax.set_xlim(0,6)
	plt.show()

def csv_file_reader(file_path, ils, method, column_id):
	column_id_value = column_id.value
	data = []

	reader = open(file_path, "r+")
	for line in reader:
		line_split = line.split(",")
		if line_split[3] == ils and line_split[9] == method and line_split[column_id_value] != "NA\n":
			data.append(float(line_split[column_id_value]))

	return data

def make_numpy_array(array1, array2):
	iterations = 0
	if len(array1) > len(array2):
		iterations = len(array2)
	else:
		iterations = len(array1)

	new_array = []

	for x in range(0, iterations):
		array = []
		array.append(array1[x])
		array.append(array2[x])
		new_array.append(array)

	return np.array(new_array)

def get_comprehensive_ils_mean_from_method(method):
	means = []

	low_ils_data = csv_file_reader("/Users/emmahamel/Research/Phylogeny/tutorials/data-species-trees.csv", "10M", method, Column_ID.SERF)
	high_ils_data = csv_file_reader("/Users/emmahamel/Research/Phylogeny/tutorials/data-species-trees.csv", "500K", method, Column_ID.SERF)

	low_ils_total = 0
	high_ils_total = 0

	for  number in low_ils_data:
		low_ils_total = low_ils_total + number

	for number in high_ils_data:
		high_ils_total = high_ils_total + number

	means.append(float(low_ils_total)/len(low_ils_data))
	means.append(float(high_ils_total)/len(high_ils_data))

	return means

def get_comprehensive_ils_std_from_method(method):
	stds = []

	low_ils_data = csv_file_reader("/Users/emmahamel/Research/Phylogeny/tutorials/data-species-trees.csv", "10M", method, Column_ID.SERF)
	high_ils_data = csv_file_reader("/Users/emmahamel/Research/Phylogeny/tutorials/data-species-trees.csv", "500K", method, Column_ID.SERF)

	stds.append(np.std(low_ils_data))
	stds.append(np.std(high_ils_data))

	return stds

ils_boxplot_grapher("ASTRAL", "NJ")

