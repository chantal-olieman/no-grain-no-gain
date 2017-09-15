#!/usr/bin/env python
import numpy as np
from PIL import Image
im = Image.open("img/clean.jpeg")
#print im.size
im = im.resize((200, 300), Image.ANTIALIAS)
arr = np.array(im)
print np.size(arr)
img = Image.fromarray(arr, 'RGB')
img.save('img/newimg.png')
print arr[100,2]
print arr[2].size	
# 	np.savetxt('test.txt', arr, fmt='%.5f',delimiter=',')
##np.savetxt('img/arr.txt', arr, delimiter=',')

