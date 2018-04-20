import numpy as np
from random import sample
#np.random.seed(0)
imagefile = "./data/image_train.txt"
centroid_f = "train_paras.txt"
images= []
pi_k=0.1 #1/10
with open(imagefile, "r") as f:
	for line in f:
		line = line.strip()
		line = line.split(",")
		line = [float(x) for x in line]
		images.append(line)

images = np.asarray(images)
cans = sample(xrange(0,len(images)),10)
candidates = np.asarray([images[can] for can in cans])
centered = images - np.mean(images,axis =0)
print(cans)
cov = np.matmul(np.transpose(centered),centered)
cov = np.reshape(cov,-1)
with open(centroid_f, "w") as cenf:
	for i in range(10):
		print(np.reshape(candidates[i],(-1,1)))
		cenf.write(str(i)+'\t'+str(pi_k)+":"+",".join(str(y) for y in cov)+":"+",".join(str(x) for x in candidates[i])+'\n')

