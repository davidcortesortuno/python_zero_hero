from PIL import Image
import matplotlib.cm as cm

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
                       max_iterations: int,
                       colorise: str ='grey'
                       ) -> None:
    """
    Arguments
    ---------
    pilImage
        xxxx
    coords
        1D list with coordinates
    canvas1d
        1D list with corresponding pixel coordinates in PIL canvas
    max_iterations
        Max number of iterations per pixel to compute mandelbrot set
    colorise
        string with two options: 'grey' or 'colormap'
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

        if colorise == 'grey':
            tone = int(255 * (1 - iter / max_iterations))
            color = (tone, tone, tone)
        elif colorise == 'colormap':
            color = cm.magma_r(iter / max_iterations, bytes=True)
        else:
            # raise Exception('color needs to be one of two options: grey or colormap')
            raise ValueError('colorise needs to be one of two options: grey or colormap')

        pilImage.putpixel(canvas1d[i], color) 

    return None


def compute_julia(pilImage: Image.Image,
                  coords: list,
                  canvas1d: list,
                  c: complex = 1. + 1. * 1j,
                  max_iterations: int = 200
                  ) -> None:
    """
    """

    width = pilImage.width
    height = pilImage.height

    # mandelbrot = [1 for i in range(width * height)]
    julia = [1] * (width * height)
    for i in range(len(coords)):
        z = coords[i]
        iter = 0
        while abs(z) <= 2 and iter <= max_iterations:
            zp = z * z + c
            iter += 1
            z = zp

        shade = int(255 * (1 - iter / max_iterations))
        color = (shade, shade, shade)
        pilImage.putpixel(canvas1d[i], color)

    return None



if __name__ == '__main__':

    image = make_canvas(100, 100)
    (coords, canv1d) = make_coords_pixel_arrays(image)
    compute_mandelbrot(image, coords, canv1d, 200, colorise='colormap')
    image.show()
