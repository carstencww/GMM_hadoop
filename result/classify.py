#!/usr/bin/env python
import numpy as np

result_mu = [0]*10
result_pi = [0]*10
result_cov = [0]*10
def multinorm(x, mu, cov):
	COE = 1 / ( ((2* np.pi)**(len(mu)/2)) * (np.linalg.det(cov)**(1/2)) )
	EXP = (-0.5) * ((x-mu).T.dot(np.linalg.inv(cov))).dot((x-mu))
	#print(COE)
	#print(EXP)
	return COE * np.exp(EXP)
if __name__ == '__main__':
	with open("./paras_result.txt","r") as paras:
		for para in paras:
			para = para.strip()
			class_no , para = para.split('\t')
			class_no = int(class_no)
			pi, cov , mu = para.split(":")
			mu =mu.split(",")
			cov = cov.split(",")
			result_pi[class_no] = float(pi)
			result_mu[class_no] = [float(x) for x in mu]
			result_cov[class_no] = np.asarray([float(x) for x in cov]).reshape(25,25)
	result_mu = np.asarray(result_mu)
	gamma = np.zeros(10)
	class_cnt=[0]*10
	with open("../data/image_train.txt","r") as images:
		for image in images:
			image = image.strip()
			coords = image.split(",")
			coords = [float(x) for x in coords]
			coords = np.asarray(coords)
			for i in range(0,10):
				gamma[i] = result_pi[i] * multinorm(coords,result_mu[i],result_cov[i])
			class_no = gamma.argmax()
			class_cnt[class_no]+=1
	for i in range(0,10):
		print("Parameter "+str(i)+": "+"{0:0.2f}".format(result_pi[i])+": ["+", ".join("{0:0.2f}".format(y) for y in result_cov[i].reshape(-1))+"],  "+": ["+", ".join("{0:0.2f}".format(x) for x in result_mu[i])+"], "+str(class_cnt[i]))

