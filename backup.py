#!/usr/bin/env python
import numpy as np
from PIL import Image
from sklearn.svm import SVC

def maketxtfile(imname, x, y):
	filename = "../img/%s.jpeg" % imname
	imgs = Image.open(filename)
	im = imgs.resize((x, y), Image.ANTIALIAS)
	arr = np.array(im)
	#instead of a matrix make a vector
	arr2d = arr.reshape(arr.shape[2], -1)
	#Already halve x and y
	y = y/2
	x = x/2 
	#fill the rest of the array
	while x > 0 and y > 0:
		im = imgs.resize((x, y), Image.ANTIALIAS)
		arr = np.array(im)
		arr2dres = arr.reshape(arr.shape[2], -1)
		y = y/2 
		x = x/2 
		arr2d = np.concatenate((arr2d,arr2dres),axis = 1)

	#save the file 
	filename = "../data/%s.txt" % imname
	np.savetxt(filename, arr2d,fmt='% 4d' ,delimiter=' ')
	return arr2d
x = 32
y = 16
#read in 0 case 
X = maketxtfile("graan", x ,y)
m, n = X.shape
Y = 0 * np.ones((1,n),int)

#read in red case 
Xres = maketxtfile("red", x ,y)
m, n = Xres.shape
Yres = 1 * np.ones((1,n),int)

#merge red with X and Y 
X = np.concatenate((X, Xres),axis = 1)
Y = np.concatenate((Y, Yres),axis = 1)

#read in stones 
Xres = maketxtfile("stone", x ,y)
m, n = Xres.shape
Yres = 2 * np.ones((1,n),int)
#merge stone with X and Y 
X = np.concatenate((X, Xres),axis = 1)
Y = np.concatenate((Y, Yres),axis = 1)


clf = SVC()
clf.fit(X, Y) 
