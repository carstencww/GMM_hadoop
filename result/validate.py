#!/usr/bin/env python
import numpy as np
result_mu = [0]*10
result_pi = [0]*10
result_cov = [0]*10
def multinorm(x, mu, cov):

	COE = -float(len(mu)) * np.log(2* np.pi) / 2 - np.log(np.linalg.det(cov)) / 2
	EXP = (-0.5) * (np.dot(np.dot((x-mu),np.linalg.inv(cov)),(x-mu)))


	#print(COE)

	return COE + EXP
if __name__ == '__main__':
	with open("./paras_result.txt","r") as paras:
		for para in paras:
			para = para.strip()
			class_no , para = para.split('\t')
			if "__" not in class_no:
				class_no = int(class_no)
				pi, cov , mu = para.split(":")
				mu =mu.split(",")
				cov = cov.split(",")
				result_pi[class_no] = float(pi)
				result_mu[class_no] = [float(x) for x in mu]
				result_cov[class_no] = np.asarray([float(x) for x in cov]).reshape(25,25)
	result_mu = np.asarray(result_mu)
	gamma = np.zeros(10)
	class_cnt=[[] for x in range(10)]
	with open("../data/image_test.txt","r") as images:
		idx = 0
		for image in images:
			image = image.strip()
			coords = image.split(",")
			coords = [float(x) for x in coords]
			coords = np.asarray(coords)
			for i in range(0,10):
				gamma[i] = np.log(result_pi[i]) + multinorm(coords,result_mu[i],result_cov[i])
			class_no = gamma.argmax()
			class_cnt[class_no].append(idx)
			idx += 1

	true_label = []
	with open("../data/label_test.txt", "r") as f:
		for label in f:
			label = label.strip()
			label = int(label)
			true_label.append(label)

	major_labels = [0]*10
	correct_images = [0]*10
	Num_images = [0]*10
	
	for i in range(10):
		Num_images[i] = len(class_cnt[i])
		count = np.zeros(10)
		for j in range(len(class_cnt[i])):
			count[true_label[class_cnt[i][j]]]+=1
		print(str(i)+": "+str(count))
		major_labels[i] = count.argmax()
		correct_images[i] = count[major_labels[i]]
	Accuracy = [float(correct_images[i])/Num_images[i] for i in range(10)]
	for i in range(0,10):
		print(str(i)+'\t'+str(Num_images[i])+'\t'+str(major_labels[i])+'\t'+str(correct_images[i])+'\t'+"{0:0.2f}".format(Accuracy[i]*100)) 
	print("Total"+'\t'+str(sum(Num_images))+'\t'+'\t'+str(sum(correct_images))+'\t'+"{0:0.2f}".format(float(sum(correct_images))*100/sum(Num_images)))
	print("\n")

