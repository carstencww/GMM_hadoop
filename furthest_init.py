import numpy as np
#np.random.seed(0)
imagefile = "./data/image_train.txt"
centroid_f = "train_centroid.txt"
images= []
candidates = []
with open(imagefile, "r") as f:
    for line in f:
        line = line.strip()
        line = line.split(",")
        line = [float(x) for x in line]
        images.append(line)
images = np.asarray(images)
ran = np.random.randint(low=0,high=len(images))
print(ran)
candidates.append(images[ran])
cans = [ran]
#print(np.linalg.norm(images - candidates[0],axis=1))
for i in range(1,10):
    di = np.zeros(len(images))
    for j in range(0,i):
        di += np.linalg.norm(images - candidates[j],axis=1)
    can = di.argmax()
    cans.append(can)
    candidates.append(images[can])
print(cans)
with open(centroid_f, "w") as cenf:
    i=0
    for candidate in candidates:
        cenf.write(str(i)+'\t'+",".join(str(x) for x in candidate)+'\n')
        i+=1
