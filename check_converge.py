#!/usr/bin/env python
import numpy as np

origin_q = [0]*10
origin_pi = [0]*10
with open("./train_paras.txt","r") as paras:
	for para in paras:
		para = para.strip()
		class_no , para  = para.split('\t')
		class_no = int(class_no)
		pi , q =  para.split(":")
		origin_pi[class_no] = float(pi)
		q = q.split(",")
		origin_q[class_no] = [float(x) for x in q]
origin_q = np.asarray(origin_q)
origin_pi = np.asarray(origin_pi)

result_q = [0]*10
result_pi = [0]*10
with open("./paras_result.txt","r") as paras:
	for para in paras:
		para = para.strip()
		class_no , para  = para.split('\t')
		class_no = int(class_no)
		pi , q =  para.split(":")
		result_pi[class_no] = float(pi)
		q = q.split(",")
		result_q[class_no] = [float(x) for x in q]
result_q = np.asarray(result_q)
result_pi = np.asarray(result_pi)

diff = np.linalg.norm(origin_q - result_q, axis=1)
dist = diff.sum()
dist += np.linalg.norm(origin_pi - result_pi)
if dist<0.00001:
	print("0")
else: 
	print("1")
print(dist)
