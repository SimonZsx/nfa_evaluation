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
	per_received = []
	per_dropped = []
	
	received = []
	dropped = []
	
	time = []

	before_rtemp = []
	after_rtemp = []
	before_dtemp = []
	after_dtemp = []
	with open(filename) as f:
		for line in f:
			if line.find("BEFORE") != -1:
				before_rtemp.append(float(line.split(' ')[4]))
				before_dtemp.append(float(line.split(' ')[6]))
			if line.find("AFTER") != -1:
				after_rtemp.append(float(line.split(' ')[4]))				
				after_dtemp.append(float(line.split(' ')[6]))
			if line.find("[RESULT]") != -1:
				numbers = line.split(' ')
				received.append(float(numbers[1]))
				#print received
				dropped.append(float(numbers[2]))
				#print dropped
				#print "after "+str(after_rtemp)
				per_received.append(list(map(lambda x: x[0]-x[1], zip(after_rtemp, before_rtemp)))) 
				per_dropped.append(list(map(lambda x: x[0]-x[1], zip(after_dtemp, before_dtemp)))) 
				print per_received
				before_rtemp=[]
				before_dtemp=[]
				after_rtemp=[]
				after_dtemp=[]

				time.append(float(numbers[3]))

	return received, dropped, time, per_received,per_dropped 

def draw(flow, pr, pr_std, pd, pd_std):

	nfa=[5,10]
	nfa=map(float,nfa)
	
	plt.style.use('ggplot')#seaborn-white')

	runtimes = [1,2,3,4,5,6,7,8,9,10,11,12]
	colors = ['r','b','y','m','c','g','r','b','y']
	styles = ['-.', '--', ':', '-', '--', ':', '-','--']
	index = 0;

	x = np.arange(4)
	labels= ["3","6","9","12"]

	width = 0.125
	plt.bar(x, flow,width, label="Traffic")
	plt.bar(x+width,pr,width, yerr=pr_std, label="Per runtime received")
	plt.bar(x+2*width,pd,width, yerr=pd_std, label="Per runtime dropped")

	plt.xticks(x+0.75*width,labels)
	plt.legend(loc='upper left')
	plt.xlabel("# of runtimes")
	plt.ylabel("Packets(kpps)")
	plt.savefig("Mixtest.pdf")
	plt.show()

def main():

	received,dropped,time, per_received, per_dropped = read_log("mixtest")

	received = list(map(lambda x: x[0]/x[1], zip(received, time))) 
	dropped = list(map(lambda x: x[0]/x[1], zip(dropped, time))) 
    
	pr = []
	pd = []
	pr_std = []
	pd_std = []
    
	for i in range(0,len(per_received)):
		per_received[i] = list(map(lambda x: x/time[i], per_received[i])) 
		per_dropped[i] = list(map(lambda x: x/time[i], per_dropped[i]))

		pr.append(sum(per_received[i])/(3*i+3))
		pd.append(sum(per_dropped[i])/(3*i+3))
		temp1 = []
		temp2 = []
		for j in range(0, len(per_received[i])):
			if per_received[i][j]>0 :
				temp1.append(per_received[i][j])
				temp2.append(per_dropped[i][j])
		print "temp1"+str(temp1)
		print "temp2"+str(temp2)

		pr_std.append(np.std(temp1))
		pd_std.append(np.std(temp2))		
	flow = list(map(lambda x: x[0]+x[1], zip(received, dropped)))
	print flow, pr, pr_std, pd, pd_std 
	
	print draw(flow, pr, pr_std, pd, pd_std) 



if __name__ == "__main__" :
	main()