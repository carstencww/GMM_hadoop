#!/usr/bin/env python
import sys
import numpy as np
cnt = 0
origin_mu = [0]*10
origin_pi = [0]*10
origin_cov = [0] * 10
new_mu = [0]*10
def multinorm(x, mu, cov):
	COE = -float(len(mu)) * np.log(2* np.pi) / 2 - np.log(np.linalg.det(cov)) / 2
	#print((x - mu).shape)
	#print(np.transpose(x-mu).shape)
	#COE = -np.log(((2* np.pi)**(len(mu)/2)) * (np.linalg.det(cov)**(1/2)))
	EXP = (-0.5) * (np.dot(np.dot((x-mu),np.linalg.inv(cov)),(x-mu)))
	#print(EXP.shape)
	#print(COE+EXP)
	#print(EXP)
	return COE + EXP

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

	with open("./supp_result.txt","r") as cens:
		for cen in cens:
			cen = cen.strip()
			class_no, paras = cen.split("\t")
			class_no = int(class_no)
			paras = paras.split(",")
			new_mu[class_no] = [float(x) for x in paras]
		new_mu = np.asarray(new_mu)

	#mu_numer_sum = [np.zeros(origin_mu[0].shape) for x in range(10)]
	pi_numer_sum = [0] * 10
	cov_numer_sum = [np.zeros(origin_cov[0].shape) for x in range(10)]
	#print(mu_numer_sum[0].shape)
	for line in sys.stdin:
		partial_gamma = [0]*10
		cnt+=1
		line = line.strip()
		coords = line.split(",")
		coords = [float(x) for x in coords]
		coords = np.asarray(coords)
		for i in range(0,10):
			partial_gamma[i] = origin_pi[i] * np.exp(multinorm(coords,origin_mu[i],origin_cov[i]))
	
		total = sum(partial_gamma)
		for i in range(10):
			if np.isinf(partial_gamma[i]): 
				partial_gamma[i] = 1
			else:
				partial_gamma[i] = partial_gamma[i] / total
		#print(partial_gamma)
		for i in range(0,10):
			pi_numer_sum[i] += partial_gamma[i]
			#mu_numer_sum[i] += gamma[i] * coords
			cov_numer_sum[i] += partial_gamma[i] * np.matmul(np.reshape(coords - new_mu[i],(-1,1)),np.reshape(coords - new_mu[i],(1,-1)))
	#print(pi_numer_sum)
	#print(cov_numer_sum)
	for i in range(0,10):
		covmat = np.reshape(cov_numer_sum[i],-1)
		print(str(i)+"\t"+str(cnt)+":"+str(pi_numer_sum[i])+":"+",".join(str(y) for y in covmat)+":"+",".join(str(x) for x in new_mu[i]))

	#print(sum(pi_numer_sum))


