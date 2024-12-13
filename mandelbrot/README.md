# Mandelbrot exercise

1. Test the `PIL` library by plotting pixels in an empty canvas

2. Start defining mandelbrot set problem looking at a grid in the complex plane

3. Define grid coordinates, grid pixel indices, as 1D lists

4. Wrap every calculation in functions. Use typing to get used to types.

5. Make function to compute mandelbrot set in pixel grid. Color pixels according to iteration to check if complex number in set. Use this protocol: start with a white pixel, and make it darker with larger iterations; max iterations reached means point in set (black); zero or small number of iterations (lighter color) means not in set.

6. Make program a module

7. Add function to compute Julia sets using same canvas as before (example to modularize program)

8. Use matplotlib's colormap module to color fractals more nicely

9. Optimisation. Use numpy arrays instead of lists. Use meshgrid functions to quickly generate coordinate grids.

10. Use `numba` to parallelize code.

11. Vectorize code.

12. Separate everything in functions.
