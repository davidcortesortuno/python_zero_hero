from PIL import Image

width, height = 1000, 1000
max_iterations = 100
image = Image.new('RGB', (width, height), 'white')

coords = []
deltax = 4. / (width - 1)
deltay = 4. / (height - 1)

# 1D approach
for y in range(height):
    yc = -2. + deltay * y
    for x in range(width):
        xc = -2. + deltax * x
        coords.append(xc + yc * 1j)

canvas1d = [(x, y) for y in range(height) for x in range(width)]
# canvas1d = []
# for y in range(height):
#     for x in range(width):
#         canvas1d.append((x, y))

# mandelbrot = [1 for i in range(width * height)]
mandelbrot = [1] * (width * height)
for i, c in enumerate(coords):
    z = 0.0 + 0.0 * 1j
    for iter in range(max_iterations):
        zp = z * z + c
        if abs(zp) >= 2:
            mandelbrot[i] = 0  # point c not in Mset
            break
        z = zp

for i, pix in enumerate(canvas1d):
    if mandelbrot[i] == 1:
        color = (255, 0, 0)
    else:
        color = (255, 255, 255)
    image.putpixel(pix, color) 

image.show()

    # zp = z * z + c
    # iter = 0
    # while abs(zp) <= 2:
    #     zp = z * z + c
    #     iter += 1
        
# 2D approach
# for y in range(height):
#     yc = -2. + deltay * y
#     row = [(-2. + deltax * x) + yc * 1j for x in range(width)]
#     coords.append(row)
