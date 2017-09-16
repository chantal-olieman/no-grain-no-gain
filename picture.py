import numpy as np
from PIL import Image
imgs = Image.open("img/stone.jpeg")
#print imgs.size
#print im.size
#im = imgs.resize((200, 300), Image.ANTIALIAS)
#im.show()
arr = np.array(imgs)
#print np.size(arr)
img = Image.fromarray(arr[2000:3000,0:3000], 'RGB')
img.show()
#img.save('img/graan2.jpeg')
