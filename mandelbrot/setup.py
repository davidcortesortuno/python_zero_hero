# https://cython.readthedocs.io/en/latest/src/userguide/numpy_tutorial.html#compilation-using-setuptools
from setuptools import Extension, setup
import numpy
from Cython.Build import cythonize
import Cython.Compiler.Options

Cython.Compiler.Options.annotate = True

extensions = [
    Extension(
        "*",
        ["*.pyx"],
        include_dirs=[numpy.get_include()],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
    )
]

setup(
    name="fractal_cythonized",
    ext_modules=cythonize(extensions, annotate=True),
)
