#!/usr/bin/env python2.7
import os
import optparse
import sys
import subprocess
import signal
import time

import numpy as np
import matplotlib.pyplot as plt


def read_log(filename):
	numbers = []
	with open(filename) as f:
		for line in f:
			number = []
			if line.find("[RESULT]") != -1:
				number = map(float, line.split(' ')[1:-1])
				numbers.append(number)
	return numbers

def draw(numbers):
	n = []
	for i in range(0,len(numbers)):
		n.append(sum(numbers[i])/len(numbers[i]))
	
	print n
	plt.style.use('ggplot')#seaborn-white')
	labels= ["10K","20K","30K","40K","50K"]
	colors = ['r','b','y','m','c','g','r','b','y']
	styles = ['-.', '--', ':', '-', '--', ':', '-','--']
	index = 0;
	line_index = 0;

	x = np.arange(5)
	width = 0.25
	plt.bar(x, n, width, color='r')
	plt.xticks(x, labels)
	plt.xlabel("# of flows")
	plt.ylabel("Time (ms)")
	plt.savefig("Recover.pdf")

	plt.show()
	
	return n

def main():

	numbers = read_log("r_test.txt")

	print draw(numbers)	 



if __name__ == "__main__" :
	main()