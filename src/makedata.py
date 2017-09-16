#!/usr/bin/env python
import numpy as np
from PIL import Image
from sklearn import svm

def makearray(imname, x, y):
	filename = "../img/%s.jpeg" % imname
	imgs = Image.open(filename)
	im = imgs.resize((x, y), Image.ANTIALIAS)
	arr = np.array(im)
	#instead of a matrix make a vector
	arr2d = arr.reshape(-1,arr.shape[2])
	return arr2d

def maketxtfile(imname, x, y):
	filename = "../img/%s.jpeg" % imname
	imgs = Image.open(filename)
	im = imgs.resize((x, y), Image.ANTIALIAS)
	arr = np.array(im)
	#instead of a matrix make a vector
	arr2d = arr.reshape(-1,arr.shape[2])
	#Already halve x and y
	y = y/2
	x = x/2 
	#fill the rest of the array
	while x > 0 and y > 0:
		im = imgs.resize((x, y), Image.ANTIALIAS)
		arr = np.array(im)
		arr2dres = arr.reshape(-1,arr.shape[2])
		y = y/2 
		x = x/2 
		arr2d = np.concatenate((arr2d, arr2dres))

	#save the file 
	filename = "../data/%s.txt" % imname
	np.savetxt(filename, arr2d,fmt='% 4d' ,delimiter=' ')
	return arr2d

def createXY(types):
	X = maketxtfile(types[0], x ,y)
	m, n = X.shape
	Y = 0 * np.ones((m,1),int)
	for i in range(1, len(types)):
		#read in i case 
		Xres = maketxtfile(types[i], x ,y)
		m, n = Xres.shape
		Yres = i * np.ones((m,1),int)
		#merge red with X and Y 
		X = np.concatenate((X, Xres))
		Y = np.concatenate((Y, Yres))
	return (X, Y)

def classify(clf, Z, n):
	result = 0 * np.ones((n,1))
	for i in range(len(Z)):
    		label = clf.predict(Z[i])
		result[label] = result[label] + 1 
	return result/len(Z)


types = ["graan", "red", "stone"] 
x = 32
y = 16


#read in data 
(X, Y) = createXY(types)
#preprocess Y
Y = Y.ravel()


#train model
clf = svm.LinearSVC()
clf.fit(X, Y) 

#read in test file
x = 32
y = 16
Z = makearray("pic", x, y)

#classify test data
results = classify(clf, Z, len(types))

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Grain', 'Red Beans', 'Stones'
sizes = results*100
explode = (0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()



