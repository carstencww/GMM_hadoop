#!/usr/bin/env python
import numpy as np
origin_logli = None
with open("./train_paras.txt","r") as paras:
	for para in paras:
		para = para.strip()
		key , para  = para.split('\t')
		if "__" in key:
			origin_logli = float(para)
result_logli = 0
with open("./paras_result.txt","r") as paras:
	for para in paras:
		para = para.strip()
		key , para  = para.split('\t')
		if "__" in key:
			result_logli = float(para)
if origin_logli is not None:
	if result_logli < origin_logli + 0.0001:
		print("0")
	else: 
		print("1")
else:
	print("1")
print(result_logli)
