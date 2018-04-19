#!/usr/bin/env python
import numpy as np
from operator import itemgetter
import collections
xs = [0.05, 0.1, 0.5, 1]
#xs = [ 1 ]
for x in xs:
	result_centroid = [0]*10

	with open("./centroid_result.txt","r") as cens:
		for cen in cens:
			cen = cen.strip()
			class_no , centroid = cen.split('\t')
			class_no = int(class_no)
			centroid = centroid.split(",")
			result_centroid[class_no] = [float(pt) for pt in centroid]
	result_centroid = np.asarray(result_centroid)
	
	true_label = []
	with open("../data/label_test.txt", "r") as f:
		for label in f:
			label = label.strip()
			label = int(label)
			true_label.append(label)
	
	dist = [{} for i in range(10)]
	with open("../data/image_test.txt","r") as images:
		idx = 0
		for image in images:
			image = image.strip()
			image = image.split(",")
			image = [float(im) for im in image]
			image = np.asarray(image)
			error = np.linalg.norm(result_centroid - image, axis=1)
			result = error.argmin()
			dist[result][idx] = error[result]
			idx += 1
	major_labels = [0]*10
	correct_images = [0]*10
	Num_images = [0]*10
	m = [0]*10
	
	#print(true_label)
	for i in range(10):
		elements=sorted(dist[i].items(), key=itemgetter(1),reverse=False)
	#	print(elements)
		Num_images[i] = len(elements)
	
		m[i] = int(x * Num_images[i])
	
		count = np.zeros(10)
		for j in range(m[i]):
			count[true_label[elements[j][0]]]+=1
		print(count)
		major_labels[i] = count.argmax()
		for j in range(Num_images[i]):
			if major_labels[i] == true_label[elements[j][0]]:
				correct_images[i]+=1
	Accuracy = [float(correct_images[i])/Num_images[i] for i in range(10)]
	print("x = "+ str(x))
	for i in range(10):
		print(str(i)+'\t'+str(Num_images[i])+'\t'+str(m[i])+'\t'+str(major_labels[i])+'\t'+str(correct_images[i])+'\t'+"{0:0.2f}".format(Accuracy[i]*100)) 
	print("Total"+'\t'+str(sum(Num_images))+'\t'+str(sum(m))+'\t'+'\t'+str(sum(correct_images))+'\t'+"{0:0.2f}".format(float(sum(correct_images))*100/sum(Num_images)))
	print("\n")





