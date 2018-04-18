import numpy as np
from random import sample
#np.random.seed(0)
imagefile = "./data/image_train.txt"
centroid_f = "train_paras.txt"
images= []

labels= [[] for i in range(10) ]
with open("./data/label_train.txt", "r") as f:
	i=0
	for line in f:
		line = line.strip()
		line = int(line)
		labels[line].append(i)
		i+=1
cans = [labels[i][np.random.randint(low=0,high=len(labels[i]))] for i in range(10)]

with open(imagefile, "r") as f:
	for line in f:
		line = line.strip()
		line = line.split(",")
		line = [int(x) for x in line]
		images.append(line)



candidates = [images[can] for can in cans]
print(candidates)
#print(np.linalg.norm(images - candidates[0],axis=1))
print(cans)
with open(centroid_f, "w") as cenf:
	i=0
	for candidate in candidates:
		for j in range(len(candidate)):
			if candidate[j] == 1:
				candidate[j] = 0.9
			else:
				candidate[j] = 0.1
		cenf.write(str(i)+'\t'+"0.1:"+",".join(str(x) for x in candidate)+'\n')
		i+=1
