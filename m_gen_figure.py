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
	labels= ["25000","50000","75000","100000","125000"]
	colors = ['r','b','y','m','c','g','r','b','y']
	styles = ['-.', '--', ':', '-', '--', ':', '-','--']
	index = 0;
	line_index = 0;

	fig,ax1 = plt.subplots()
	loss = [10,20,30,40,50]
	x = np.arange(5)
	width = 0.25
	ax1.bar(x, n, width, color='r')
	plt.xticks(x+0.5*width, labels)
	ax1.set_xlabel("# of flows")
	ax1.set_ylabel("Time (ms)")

	ax2 =ax1.twinx()
	ax2.set_ylim([0,1000])
	ax2.bar(x+width, loss, width, color='b')
	ax2.set_ylabel("Packet Loss")
	plt.savefig("Migration.pdf")
	plt.show()
	
	return n

def main():

	numbers = read_log("m_test.txt")

	print draw(numbers)	 



if __name__ == "__main__" :
	main()