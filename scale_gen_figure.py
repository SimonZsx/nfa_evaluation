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
	lr24 = []
	lr25 = []
	lr26 = []
	lr31 = []
	lr32 = []
	lr33 = []
	lr34 = []
	lr35 = []
	lr36 = []

	i = 0
	r21 = 0
	r22 = 0
	r23 = 0
	r24 = 0
	r25 = 0
	r26 = 0
	r31 = 0
	r32 = 0
	r33 = 0
	r34 = 0
	r35 = 0
	r36 = 0
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
			elif line.find("r24throughput")!=-1:
				r24 = float(line.split(':')[1])
				lr24.append(r24/1000)
			elif line.find("r25throughput")!=-1:
				r25 = float(line.split(':')[1])
				lr25.append(r25/1000)
			elif line.find("r26throughput")!=-1:
				r26 = float(line.split(':')[1])
				lr26.append(r26/1000)
			elif line.find("r31throughput")!=-1:
				r31 = float(line.split(':')[1])
				lr31.append(r31/1000)
			elif line.find("r32throughput")!=-1:
				r32 = float(line.split(':')[1])
				lr32.append(r32/1000)
			elif line.find("r33throughput")!=-1:
				r33 = float(line.split(':')[1])
				lr33.append(r33/1000)
			elif line.find("r34throughput")!=-1:
				r34 = float(line.split(':')[1])
				lr34.append(r34/1000)
			elif line.find("r35throughput")!=-1:
				r35 = float(line.split(':')[1])
				lr35.append(r35/1000)
			elif line.find("r36throughput")!=-1:
				r36 = float(line.split(':')[1])
				lr36.append(r36/1000)
			elif line.find("total")!=-1:
				total = float(line.split(':')[1])
				flow.append(total/1000)
				tp.append((r21+r22+r23+r24+r25+r26+r31+r32+r33+r34+r35+r36)/1000)
			#print line
			
	return tp,flow,lr21,lr22,lr23,lr24,lr25,lr26,lr31,lr32,lr33,lr34,lr35,lr36

def draw(tp, flow,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12):

	#print "l1 len"+str(len(l1))
	#print "tp len"+str(len(tp))
	#print "l1"+str(l1)

	lines = [tp,flow,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12]
	
	plt.style.use('ggplot')#seaborn-white')

	timeline = np.linspace(1,3*len(tp),len(tp))
	colors = ['r','b','y','m','c','g','r','b','y','m','c','b','m','y']
	styles = ['-.', '--', ':', '-', ':', ':', ':',':','-.','--',':','-','-.','--','--']
	index = 0;
	line_index = 0;
	linelabels = ["Throughput", "Traffic income", "rt1","rt2","rt3","rt4","rt5","rt6","rt7","rt8","rt9","rt10","rt11","rt12"]
	for l in lines:
		l1 = plt.errorbar(timeline, l, fmt = styles[index], color=colors[index], label=linelabels[line_index])

		#l2 = plt.plot(runtimes, l, '^', color=colors[index])

		print l
		index+=1
		line_index+=1
		if line_index == 14:
			break

	plt.legend(loc='center right')
	plt.xlabel("Timeline(s)")
	plt.ylabel("Throughput(kpps)")
	plt.savefig("Scale.pdf")
	plt.show()
	return lines

def main():

	tp,flow,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12 = read_log("dynamic_scale2.log")

	print draw(tp,flow,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12) 



if __name__ == "__main__" :
	main()