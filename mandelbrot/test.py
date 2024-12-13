import fractal as fr


image = fr.make_canvas(400, 400)
(coords, canv1d) = fr.make_coords_pixel_arrays(image)
# fr.compute_mandelbrot(image, coords, canv1d, 200, colorise='colormap')
fr.compute_julia(image, coords, canv1d, c=-0.7 + 0.27015j, max_iterations=200)
image.show()
