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
	flow = []
	lr21 = []
	lr22 = []
	lr23 = []
	lr31 = []
	lr32 = []
	lr33 = []

	i = 0
	r21 = 0
	r22 = 0
	r23 = 0
	r31 = 0
	r32 = 0
	r33 = 0
	total = 0
	with open(filename) as f:
		for line in f:
			if line.find("r21throughput")!=-1:
				r21 = float(line.split(':')[1])
				lr21.append(r21/1000)
			elif line.find("r22throughput")!=-1:
				r22 = float(line.split(':')[1])
				lr22.append(r22/1000)
			elif line.find("r23throughput")!=-1:
				r23 = float(line.split(':')[1])
				lr23.append(r23/1000)
			elif line.find("r31throughput")!=-1:
				r31 = float(line.split(':')[1])
				lr31.append(r31/1000)
			elif line.find("r32throughput")!=-1:
				r32 = float(line.split(':')[1])
				lr32.append(r32/1000)
			elif line.find("r33throughput")!=-1:
				r33 = float(line.split(':')[1])
				lr33.append(r33/1000)
			elif line.find("total")!=-1:
				total = float(line.split(':')[1])
				flow.append(total/1000)
				tp.append((r21+r22+r23+r31+r32+r33)/1000)
			#print line
			
	return tp,flow,lr21,lr22,lr23,lr31,lr32,lr33

def draw(tp, flow,l1,l2,l3,l4,l5,l6):

	#print "l1 len"+str(len(l1))
	#print "tp len"+str(len(tp))
	#print "l1"+str(l1)

	lines = [tp,flow,l1,l2,l3,l4,l5,l6]
	
	plt.style.use('ggplot')#seaborn-white')

	timeline = np.linspace(1,3*len(tp),len(tp))
	colors = ['r','b','y','m','c','g','r','b','y']
	styles = ['-.', '--', ':', '-', ':', ':', ':',':']
	index = 0;
	line_index = 0;
	linelabels = ["Throughput", "Traffic income", "rt1","rt2","rt3","rt4","rt5","rt6"]
	for l in lines:
		l1 = plt.errorbar(timeline, l, fmt = styles[index], color=colors[index], label=linelabels[line_index])

		#l2 = plt.plot(runtimes, l, '^', color=colors[index])

		print l
		index+=1
		line_index+=1
		if line_index == 8:
			break

	plt.legend(loc='center right')
	plt.xlabel("Timeline(s)")
	plt.ylabel("Throughput(kpps)")
	plt.savefig("Scale.pdf")
	plt.show()
	return lines

def main():

	tp,flow,l1,l2,l3,l4,l5,l6 = read_log("dynamic_scale")

	print draw(tp,flow,l1,l2,l3,l4,l5,l6) 



if __name__ == "__main__" :
	main()