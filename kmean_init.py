#!/usr/bin/env python
import numpy as np
paras_f = "train_paras.txt"
result_centroid = [0]*10

with open("./centroid_result.txt","r") as cens:
	for cen in cens:
		cen = cen.strip()
		class_no , centroid = cen.split('\t')
		class_no = int(class_no)
		centroid = centroid.split(",")
		result_centroid[class_no] = [float(x) for x in centroid]
result_centroid = np.asarray(result_centroid)

class_cnt=[0]*10
class_data = [[] for x in range(10)]
class_cov = [0] *10
class_mean = [0]*10
with open("./data/image_train.txt","r") as images:
	for image in images:
		image = image.strip()
		image = image.split(",")
		image = [float(x) for x in image]
		image = np.asarray(image)
		class_no = np.linalg.norm(result_centroid - image, axis=1).argmin()
		class_cnt[class_no]+=1
		class_data[class_no].append(image)

for i in range(0,10):
	class_data[i] = np.asarray(class_data[i])
	class_mean[i] = np.mean(class_data[i], axis =0)
	class_data[i] = class_data[i] - class_mean[i]
	class_cov[i] = np.matmul(np.transpose(class_data[i]),class_data[i]) / (class_cnt[i])
total = float(sum(class_cnt))

with open(paras_f, "w") as cenf:
	for i in range(10):
		cov = np.reshape(class_cov[i],-1)
		cenf.write(str(i)+'\t'+str(class_cnt[i]/total)+":"+",".join(str(y) for y in cov)+":"+",".join(str(x) for x in class_mean[i])+'\n')

