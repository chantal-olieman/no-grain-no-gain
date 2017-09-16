#!/usr/bin/env python
import numpy as np
from PIL import Image


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

	print arr2d
	print arr2d.shape
	#save the file 
	filename = "../data/%s.txt" % imname
	np.savetxt(filename, arr2d,fmt='% 4d' ,delimiter=' ')

x = 32
y = 16
maketxtfile("clean", x ,y)
print "hi"
