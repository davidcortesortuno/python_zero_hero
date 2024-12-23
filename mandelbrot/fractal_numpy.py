import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import numba


def make_canvas(width: int = 1000, height: int = 1000) -> np.ndarray:
    image = np.zeros((height, width), dtype=np.uint16)
    return image



def make_coords_pixel_arrays(Image: np.ndarray) -> np.ndarray:
    """Create 1D arrays for complex coords and pixels

    Arguments
    ---------
    Image
        Numpy array in 2D as a canvas

    Returns
    -------
    A 1D numpy array with complex coordinates
    """

    height = Image.shape[0]
    width = Image.shape[1]

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

# @numba.jit(nopython=True, parallel=True)
@numba.njit(parallel=True)
def compute_mandelbrot_numba_parallel(npImage: np.ndarray,
                                      coords: np.ndarray,
                                      max_iterations : int = 100
                                      ) -> None:
    """
    Arguments
    ---------
    npImage
        Canvas as a 2D numpy array
    coords
        1D list with coordinates
    max_iterations
        Max number of iterations per pixel to compute mandelbrot set
    colorise
        string with two options: 'grey' or 'colormap'
    """

    width = npImage.shape[1]

    for i in numba.prange(coords.shape[0]):
        z = 0.0 + 0.0 * 1j
        c = coords[i]
        for iter in range(max_iterations):
            zp = z * z + c
            if abs(zp) >= 2:
                break
            z = zp

        # coords_ij = i + width * j
        pixel_col = i % width
        pixel_row = i // width 

        npImage[pixel_row, pixel_col] = iter

    return None

@numba.njit()
def compute_mandelbrot_numba(npImage: np.ndarray,
                             coords: np.ndarray,
                             max_iterations : int = 100
                             ) -> None:
    """
    Arguments
    ---------
    npImage
        Canvas as a 2D numpy array
    coords
        1D list with coordinates
    max_iterations
        Max number of iterations per pixel to compute mandelbrot set
    colorise
        string with two options: 'grey' or 'colormap'
    """

    width = npImage.shape[1]

    for i, c in enumerate(coords):
        z = 0.0 + 0.0 * 1j

        for iter in range(max_iterations):
            zp = z * z + c
            if abs(zp) >= 2:
                break
            z = zp

        # coords_ij = i + width * j
        pixel_col = i % width
        pixel_row = i // width 

        npImage[pixel_row, pixel_col] = iter

    return None


def compute_mandelbrot(npImage: np.ndarray,
                       coords: np.ndarray,
                       max_iterations : int = 100
                       ) -> None:
    """
    Arguments
    ---------
    npImage
        Canvas as a 2D numpy array
    coords
        1D list with coordinates
    max_iterations
        Max number of iterations per pixel to compute mandelbrot set
    colorise
        string with two options: 'grey' or 'colormap'
    """

    width = npImage.shape[1]

    for i, c in enumerate(coords):
        z = 0.0 + 0.0 * 1j

        for iter in range(max_iterations):
            zp = z * z + c
            if abs(zp) >= 2:
                break
            z = zp

        # coords_ij = i + width * j
        pixel_col = i % width
        pixel_row = i // width 

        npImage[pixel_row, pixel_col] = iter

    return None


# def compute_mandelbrot_vectorized(npImage: np.ndarray,
#                                   coords: np.ndarray,
#                                   max_iterations : int = 100
#                                   ) -> None:
#     """
#     Arguments
#     ---------
#     npImage
#         Canvas as a 2D numpy array
#     coords
#         1D list with coordinates
#     max_iterations
#         Max number of iterations per pixel to compute mandelbrot set
#     colorise
#         string with two options: 'grey' or 'colormap'
#     """
# 
#     width = npImage.shape[1]
# 
#     # z = 0.0 + 0.0 * 1j
#     z = np.zeros(coords.shape[0], dtype=np.complex128)
# 
#     for iter in range(max_iterations):
#         zp = z * z + coords
#         npMask = np.abs(zp) >= 2
#         z[npMask] += 1
# 
#         if np.abs(zp) >= 2:
#             break
#         z = zp
# 
#     # coords_ij = i + width * j
#     pixel_col = i % width
#     pixel_row = i // width 
# 
#     npImage[pixel_row, pixel_col] = iter
# 
#     return None


if __name__ == '__main__':

    image = make_canvas(7000, 7000)  # create numpy array canvas
    coords = make_coords_pixel_arrays(image)
    # compute_mandelbrot(image, coords, 200, colorise='colormap')
    # compute_mandelbrot_numba(image, coords, max_iterations=200)
    # compute_mandelbrot_numba_parallel.parallel_diagnostics(level=4)
    compute_mandelbrot_numba_parallel(image, coords, max_iterations=200)

    f, ax = plt.subplots()
    ax.imshow(image, cmap='plasma', origin='lower')
    # plt.savefig('test_parallel.png', bbox_inches='tight')
    plt.show()
