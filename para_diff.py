#!/usr/bin/env python
import numpy as np

origin_mu = [0]*10
origin_pi = [0]*10
origin_cov = [0]*10
with open("./train_paras.txt","r") as paras:
	for para in paras:
		para = para.strip()
		class_no , para  = para.split('\t')
		class_no = int(class_no)
		pi ,cov, mu =  para.split(":")
		origin_pi[class_no] = float(pi)
		mu = mu.split(",")
		cov = cov.split(",")
		origin_cov[class_no] = [float(y) for y in cov]
		origin_mu[class_no] = [float(x) for x in mu]
origin_mu = np.asarray(origin_mu)
origin_pi = np.asarray(origin_pi)
origin_cov = np.asarray(origin_cov)

result_mu = [0]*10
result_pi = [0]*10
result_cov = [0]*10
with open("./paras_result.txt","r") as paras:
	for para in paras:
		para = para.strip()
		class_no , para  = para.split('\t')
		class_no = int(class_no)
		pi ,cov ,mu =  para.split(":")
		result_pi[class_no] = float(pi)
		mu = mu.split(",")
		cov = cov.split(",")
		result_mu[class_no] = [float(x) for x in mu]
		result_cov[class_no] = [float(y) for y in cov]
result_mu = np.asarray(result_mu)
result_pi = np.asarray(result_pi)
result_cov = np.asarray(result_cov)

diff = np.linalg.norm(origin_mu - result_mu, axis=1)
dist = diff.sum() / 25
dist += np.linalg.norm(origin_pi - result_pi)
dist += np.linalg.norm(origin_cov - result_cov, axis = 1).sum() / 625
if dist<0.1 or np.isnan(dist):
	print("0")
else: 
	print("1")
print(dist)
