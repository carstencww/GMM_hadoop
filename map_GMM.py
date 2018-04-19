#!/usr/bin/env python
import sys
import numpy as np
cnt = 0
origin_mu = [0]*10
origin_pi = [0]*10
origin_cov = [0] * 10

def multinorm(x, mu, cov):
	COE = 1 / ( ((2* np.pi)**(len(mu)/2)) * (np.linalg.det(cov)**(1/2)) )
	EXP = (-0.5) * ((x-mu).T.dot(np.linalg.inv(cov))).dot((x-mu))
	#print(COE)
	#print(EXP)
	return COE * np.exp(EXP)

if __name__ == '__main__':
	with open("./train_paras.txt","r") as cens:
		for cen in cens:
			cen = cen.strip()
			class_no , paras = cen.split('\t')
			class_no = int(class_no)
			pi,cov ,mu  = paras.split(":")
			mu =mu.split(",")
			cov = cov.split(",")
			origin_pi[class_no] = float(pi)
			origin_mu[class_no] = [float(x) for x in mu]
			origin_cov[class_no] = np.asarray([float(x) for x in cov]).reshape(25,25)
	origin_mu = np.asarray(origin_mu)
	#print(origin_mu[0].shape)
	#print(origin_cov[0].shape)
	q_numer_sum = np.zeros((10,origin_mu.shape[1]))
	pi_numer_sum = [0] * 10
	cov_numer_sum = [0] * 10
	for line in sys.stdin:
		partial_gamma = [0]*10
		cnt+=1
		line = line.strip()
		coords = line.split(",")
		coords = [float(x) for x in coords]
		coords = np.asarray(coords)
		print(coords.shape)
		for i in range(0,10):
			partial_gamma[i] = multinorm(coords,origin_mu[i],origin_cov[i])
	
		total = sum(partial_gamma)

		gamma = [x / total for x in partial_gamma]	
		print(gamma)
		for i in range(0,10):
			pi_numer_sum[i] += gamma[i]
			q_numer_sum[i] += gamma[i] * coords
		
	#for i in range(0,10):
	#	print(str(i)+"\t"+str(cnt)+":"+str(pi_numer_sum[i])+":"+",".join(str(x) for x in q_numer_sum[i]))




