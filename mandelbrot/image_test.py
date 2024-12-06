# import PIL
from PIL import Image


image = Image.new('RGB', (100, 100), 'white')
image.putpixel((50, 50), (255, 0, 0))

image.show()
image.save('test.png')
