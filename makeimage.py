def merge_images():
    from PIL import Image
    image1 = Image.open("img/graan.jpeg")
    image2 = Image.open("img/red.jpeg")
    
(width1, height1) = image1.size
(width2, height2) = image2.size

resw = width1 + width2
resh = max(height1 + heigth2)

result = Image.new('RGB', (resw, resh))
result.paste(im=image1, box=(0,0))
result.paste(im=image2, box=(width1, 0))
print result
