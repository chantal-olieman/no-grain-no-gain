#!/usr/bin/env python
import numpy as np
from PIL import Image
from sklearn import svm
import matplotlib.pyplot as plt

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

def plot(results, labels):
	sizes = results*100
	colors = ['yellowgreen', 'gold', 'lightskyblue', 'red', 'purple', 'blue', 'gray']
	explode = (0, 0, 0, 0, 0, 0, 0)  # explode a slice if required

	plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        	autopct='%1.1f%%', shadow=True)
        
	#draw a circle at the center of pie to make it look like a donut
	centre_circle = plt.Circle((0,0),0.40,color='black', fc='white',linewidth=0.75)
	fig = plt.gcf()
	fig.gca().add_artist(centre_circle)
	outside = plt.Circle((0,0),1.0,color='black', linewidth=0.75, fill=False)
	fig.gca().add_artist(outside)

	# Set aspect ratio to be equal so that pie is drawn as a circle.
	plt.axis('equal')
	plt.show()


types = ["graan", "red", "green", "stro", "stone", "black", "dried"] 
x = 128
y = 64


#read in data 
(X, Y) = createXY(types)
#preprocess Y
Y = Y.ravel()


#train model
clf = svm.LinearSVC()
clf.fit(X, Y) 

#read in test file
x = 160
y = 320
Z = makearray("conta", x, y)

#classify test data
results = classify(clf, Z, len(types))
labels = 'Grain', 'Red Beans', 'Green', 'Stro', 'Stone', 'Black', 'Dried'

plot(results, labels)

