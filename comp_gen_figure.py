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

def draw():

	opennf=[350,360,500,660]
	opennf=map(float,opennf)
	nfa=[100,110,118,122]
	nfa=map(float,nfa)
	
	plt.style.use('ggplot')#seaborn-white')

	runtimes = [1,2,3,4,5,6,7,8,9,10,11,12]
	colors = ['r','b','y','m','c','g','r','b','y']
	styles = ['-.', '--', ':', '-', '--', ':', '-','--']
	index = 0;

	x = np.arange(4)
	#labels= ["2.5K","5K","7.5K","10K"]

	
	plt.plot(x, opennf, 'x:', label="OpenNF")
	plt.plot(x, nfa, '^-.', label="NFA")

	#plt.xticks(x,labels)
	plt.legend(loc='upper left')
	plt.xlabel("Packet Rate")
	plt.ylabel("Move time")
	plt.savefig("Compare.pdf")
	plt.show()

def main():

	#runtimes,received,dropped,time = read_log("temp")

	print draw() 



if __name__ == "__main__" :
	main()