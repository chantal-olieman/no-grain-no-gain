import numpy as np
from PIL import Image
imgs = Image.open("img/conta.jpeg")
#print imgs.size
#print im.size
#im = imgs.resize((200, 300), Image.ANTIALIAS)
#im.show()
arr = np.array(imgs)
#print np.size(arr)
img = Image.fromarray(arr[300:1900,900:4100], 'RGB')
img.show()
img.save('img/conta.jpeg')
