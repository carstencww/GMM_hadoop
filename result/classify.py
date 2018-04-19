#!/usr/bin/env python
import numpy as np

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
with open("../data/image_train.txt","r") as images:
	for image in images:
		image = image.strip()
		image = image.split(",")
		image = [float(x) for x in image]
		image = np.asarray(image)
		class_no = np.linalg.norm(result_centroid - image, axis=1).argmin()
		class_cnt[class_no]+=1
for i in range(0,10):
	print("Centroid "+str(i)+": ["+", ".join("{0:0.2f}".format(x) for x in result_centroid[i])+"], "+str(class_cnt[i]))
#print(class_cnt)
