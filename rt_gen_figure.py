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
	runtimes = []
	received = []
	dropped = []
	time = []
	with open(filename) as f:
		for line in f:
			if line.find("[RESULT]") != -1:
				numbers = line.split(' ')
				received.append(float(numbers[1]))
				dropped.append(float(numbers[2]))
				time.append(float(numbers[3]))

	return runtimes, received, dropped, time 

def draw(received, dropped, time):

	lines = []
	line = []
	loop = 0
	for i in range(0,len(received)):
		line.append(received[i]/(time[i]))
		loop+=1
		if loop ==6:
			loop = 0
			lines.append(line)
			line = []
	
	plt.style.use('ggplot')#seaborn-white')

	runtimes = [1,2,3,4,5,6,7,8,9,10,11,12]
	colors = ['r','b','y','m','c','g','r','b','y']
	styles = ['s-.', 'o--', '<:', '^:', 'D:', 'p:', 'x:','*:']
	linelabels = ["FM","HP", "FW", "FM,HP","HP,FW","FM,FW","FM,HP,FW"]

	index = 0;
	line_index = 0;
	for l in lines:
		l1 = plt.errorbar(runtimes[:-6], l, yerr=0.1, fmt = styles[index], color=colors[index], label=linelabels[line_index])

		#l2 = plt.plot(runtimes, l, '^', color=colors[index])

		index+=1
		line_index+=1
		if line_index == 7:
			break

	plt.legend(loc="lower right")
	plt.xlabel("# of runtimes")
	plt.ylabel("Throughput(kpps)")
	plt.show()
	plt.savefig("ReplicaTP.pdf")


	return lines

def main():

	runtimes,received,dropped,time = read_log("rttemp")

	print draw(received, dropped, time) 



if __name__ == "__main__" :
	main()