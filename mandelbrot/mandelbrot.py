from PIL import Image

max_iterations = 100


def make_canvas(width: int = 1000, height: int = 1000) -> Image.Image:
    # width, height = 1000, 1000
    image = Image.new('RGB', (width, height), 'white')
    return image



def make_coords_pixel_arrays(pilImage: Image.Image) -> tuple[list, list]:
    """Create 1D arrays for complex coords and pixels

    Arguments
    ---------
    width, height
        integers with width and height
    """
    width = pilImage.width
    height = pilImage.height

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

    return coords, canvas1d
    
# canvas1d = []
# for y in range(height):
#     for x in range(width):
#         canvas1d.append((x, y))

def compute_mandelbrot(pilImage: Image.Image,
                       coords: list,
                       canvas1d: list,
                       max_iterations: int) -> None:
    """
    """

    width = pilImage.width
    height = pilImage.height

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

        tone = int(255 * (1 - iter / max_iterations))
        color = (tone, tone, tone)
        pilImage.putpixel(canvas1d[i], color) 

    return None


image = make_canvas(1200, 1200)
(coords, canv1d) = make_coords_pixel_arrays(image)
compute_mandelbrot(image, coords, canv1d, 200)

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
