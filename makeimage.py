from PIL import Image
import numpy
image1 = Image.open("img/graan.jpeg")
image2 = Image.open("img/red.jpeg")
image3 = Image.open("img/stone.jpeg")
    
(width1, height1) = image1.size
(width2, height2) = image2.size
(width3, height3) = image3.size

resw = width1 + width2 + width3
#resh = numpy.max(height1,height2)

result = Image.new('RGB', (resw, height3))
result.paste(im=image1, box=(0,0))
result.paste(im=image2, box=(width1, 0))
result.paste(im=image3, box=(width1+width2, 0))
result.show()
result.save('img/pic1.jpeg')
