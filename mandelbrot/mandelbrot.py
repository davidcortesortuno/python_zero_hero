from PIL import Image

width, height = 10, 10
# image = Image.new('RGB', (width, height), 'white')

coords = []
deltax = 4. / (width - 1)
deltay = 4. / (height - 1)

# 1D approach
for y in range(height):
    yc = -2. + deltay * y
    for x in range(width):
        xc = -2. + deltax * x
        coords.append(xc + yc * 1j)
