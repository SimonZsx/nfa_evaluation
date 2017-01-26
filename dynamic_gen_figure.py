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
	tp = []
	i = 0
	with open(filename) as f:
		for line in f:
			i+=1
			print line
			tp.append(float(line)/1000)
			if i==50 :
				break
	return tp 

def draw(l1, l2):

	lines = [l1,l2]
	
	plt.style.use('ggplot')#seaborn-white')

	timeline = np.linspace(1,150,50)
	colors = ['r','b','y','m','c','g','r','b','y']
	styles = ['-.', '--', ':', '-', 'D:', 'p:', 'x:','*:']
	index = 0;
	line_index = 0;
	linelabels = ["with DU", "without DU", "dynamic","HP,FW","FM,FW","FM,HP,FW"]
	for l in lines:
		l1 = plt.errorbar(timeline, l, fmt = styles[index], color=colors[index], label=linelabels[line_index])

		#l2 = plt.plot(runtimes, l, '^', color=colors[index])

		index+=1
		line_index+=1
		if line_index == 2:
			break

	plt.legend(loc='center right')
	plt.xlabel("Timeline(s)")
	plt.ylabel("Throughput(kpps)")
	plt.savefig("Dynamic.pdf")
	plt.show()
	return lines

def main():

	tp1 = read_log("with_dynamic_update_throughput")
	tp2 = read_log("without_dynamic_update_throughput")

	print draw(tp1,tp2) 



if __name__ == "__main__" :
	main()