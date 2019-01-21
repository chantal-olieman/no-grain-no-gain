#!/usr/bin/env python
import numpy as np
from PIL import Image
imgs = Image.open("img/clean.jpeg")
#print im.size
im = imgs.resize((200, 300), Image.ANTIALIAS)
arr = np.array(im)
print np.size(arr)
img = Image.fromarray(arr[0:2,0:2], 'RGB')
#img.show()
img.save('img/newimg.png')
print arr[0,0]
print arr[0,1]
print arr[1,0]
print arr[1,1]
print "Dit gaat mis"
x = float(int(arr[0,0,0])+ int(arr[0,1,0]) + int(arr[1,0,0]) + int(arr[1,1,0]))
print x
print float(x/4)
im = imgs.resize((10, 15), Image.ANTIALIAS)
im.show()
arr = np.array(im)
print "The size is: " + repr(np.size(arr))
print arr[0,0]
x = int(arr[0,0,0])+ int(arr[0,1,0]) + int(arr[1,0,0]) + int(arr[1,1,0])

# 	np.savetxt('test.txt', arr, fmt='%.5f',delimiter=',')
##np.savetxt('img/arr.txt', arr, delimiter=',')

