# Check: https://cython.readthedocs.io/en/latest/src/tutorial/numpy.html#
# import numpy as np
cimport numpy as cnp
import cython

# It's necessary to call "import_array" if you use any part of the
# numpy PyArray_* API. From Cython 3, accessing attributes like
# ".shape" on a typed Numpy array use this API. Therefore we recommend
# always calling "import_array" whenever you "cimport numpy"
cnp.import_array()

# We now need to fix a datatype for our arrays. I've used the variable
# DTYPE for this, which is assigned to the usual NumPy runtime
# type info object.
# DTYPE = np.int64

# "ctypedef" assigns a corresponding compile-time type to DTYPE_t. For
# every type in the numpy module there's a corresponding compile-time
# type with a _t-suffix.
# This is more clear than using just float/double as float in Python is float64 (not 32 bit like C)
ctypedef cnp.float64_t DTYPE_t

# Here we use the memoryviews syntax, e.g. double [:] array
# for improved speed accessing  numpy arrays
@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def compute_mandelbrot_cython(DTYPE_t [:] coords_ri,
                              DTYPE_t [:] canvas,
                              int width, 
                              int height,
                              int max_iter):
    """ """

    cdef DTYPE_t zabs
    cdef DTYPE_t zreal
    cdef DTYPE_t zimag
    cdef int cidx
    cdef int xi
    cdef int yi
    cdef int ni

    for yi in range(height):
        for xi in range(width):
            zabs = 0.0
            zreal = 0.0
            zimag = 0.0
            cidx = xi + height * yi
            ni = 0
            while ni <= max_iter and zabs <= 4:
                zreal = zreal + coords_ri[2 * cidx]
                zimag = zimag + coords_ri[2 * cidx + 1]
                zabs = zreal * zreal - zimag * zimag

                ni += 1

            canvas[cidx] = max_iter

    return None
