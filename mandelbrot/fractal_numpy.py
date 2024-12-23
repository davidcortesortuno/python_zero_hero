from PIL import Image
import matplotlib.cm as cm
import numpy as np

max_iterations = 100


def make_canvas(width: int = 1000, height: int = 1000) -> Image.Image:
    # width, height = 1000, 1000
    image = Image.new('RGB', (width, height), 'white')
    return image



def make_coords_pixel_arrays(pilImage: Image.Image) -> np.ndarray:
    """Create 1D arrays for complex coords and pixels

    Arguments
    ---------
    width, height
        integers with width and height

    Returns
    -------
    A tuple with 2 numpy arrays: coordinates and canvas
    """
    width = pilImage.width
    height = pilImage.height

    # Tile and repeat approach
    # xi = np.linspace(-2, 2, width)
    # yi = np.linspace(-2, 2, height)
    # X = np.tile(xi, height)
    # Y = np.repeat(yi, width)
    # coords = X + Y * 1j

    # Tile and repeat approach
    xi = np.linspace(-2, 2, width)
    yi = np.linspace(-2, 2, height)
    X, Y = np.meshgrid(xi, yi)
    coords = X + Y * 1j  # 2D
    coords.shape = -1  # flat to 1D

    return coords

# canvas1d = []
# for y in range(height):
#     for x in range(width):
#         canvas1d.append((x, y))

def compute_mandelbrot(pilImage: Image.Image,
                       coords: np.ndarray,
                       max_iterations : int = 100,
                       colorise: str ='grey'
                       ) -> None:
    """
    Arguments
    ---------
    pilImage
        xxxx
    coords
        1D list with coordinates
    max_iterations
        Max number of iterations per pixel to compute mandelbrot set
    colorise
        string with two options: 'grey' or 'colormap'
    """

    width = pilImage.width
    height = pilImage.height
    # NOTE: coords array has dimensions = width x height

    for i, c in enumerate(coords):
        z = 0.0 + 0.0 * 1j

        for iter in range(max_iterations):
            zp = z * z + c
            if abs(zp) >= 2:
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

        # coords_ij = i + width * j
        pixel_col = i % width
        pixel_row = i // width 

        pilImage.putpixel((pixel_col, pixel_row), color) 

    return None


if __name__ == '__main__':

    image = make_canvas(500, 500)
    coords = make_coords_pixel_arrays(image)
    # compute_mandelbrot(image, coords, 200, colorise='colormap')
    compute_mandelbrot(image, coords, max_iterations=100)
    image.save('test_fn.png')
