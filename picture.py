import numpy as np
from PIL import Image
imgs = Image.open("img/stone.jpeg")
#print imgs.size
#print im.size
#im = imgs.resize((200, 300), Image.ANTIALIAS)
#im.show()
arr = np.array(imgs)
#print np.size(arr)
img = Image.fromarray(arr[1300:1600,2200:2500], 'RGB')
img.show()
img.save('img/stone.jpeg')
