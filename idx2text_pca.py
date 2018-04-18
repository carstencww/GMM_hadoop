import numpy as np
import os
import struct

#train-images-idx3-ubyte,t10k-images-idx3-ubyte,train-labels-idx1-ubyte,t10k-labels-idx1-ubyte
labelfile = "./raw_data/train-labels-idx1-ubyte" , "./raw_data/t10k-labels-idx1-ubyte"
imagefile = "./raw_data/train-images-idx3-ubyte" , "./raw_data/t10k-images-idx3-ubyte"
txtlabel = "./data/label_train.txt" , "./data/label_test.txt"
txtimage = "./data/image_train.txt" , "./data/image_test.txt"

num = [None, None]
data = [None, None]
with open(imagefile[0], 'rb') as idxim:
	magicn, num[0], rows, cols = struct.unpack(">IIII", idxim.read(16))
	print(num)
	data[0] = np.fromfile(idxim, dtype=np.uint8).reshape(num[0], rows * cols)

with open(imagefile[1], 'rb') as idxim:
        magicn, num[1], rows, cols = struct.unpack(">IIII", idxim.read(16))
        data[1] = np.fromfile(idxim, dtype=np.uint8).reshape(num[1], rows * cols)

dataarr = np.concatenate((data[0],data[1]),axis = 0)
dataarr = dataarr - np.mean(dataarr,axis = 0)
covmat = np.matmul(np.transpose(dataarr), dataarr)
eigva, eigve = np.linalg.eigh(covmat)
ind = np.argsort(eigva)[::-1]
evals = eigva[ind]
evecs = eigve[:,ind]
evals = np.transpose(evals)
evecs = np.transpose(evecs)
evecs = evecs[:25,:]
evecs = np.transpose(evecs)
dataarr = np.matmul(dataarr,evecs)
data[0] = dataarr[:60000,:]
data[1] = dataarr[60000:70000,:]
print(data[0].shape)
print(data[1].shape)

for i in range(0,2):
	with open(labelfile[i], 'rb') as idxlb:
		MagicN, Num = struct.unpack(">II", idxlb.read(8))
		labels = np.fromfile(idxlb, dtype=np.int8)
	print(MagicN)
	print(Num)
	with open(txtlabel[i],'w') as txtlbf:
		for label in labels:
			txtlbf.write(str(label)+'\n')
	with open(txtimage[i],'w') as txtima:
		for image in data[i]:
			imagetxt = ",".join(str(x) for x in image)
			txtima.write(imagetxt+'\n')

