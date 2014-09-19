import math
import blinkcomponents
import colorsys


def linear_color_gradient(freq, phase_red, phase_green, phase_blue, center=None, width=None, length=10):
    if center is None:
        center = 128
    if width is None:
        width = 127

    colors = []
    for i in range(0, length):
        r = int(math.sin(freq*i + 2 + phase_red) * width + center)
        g = int(math.sin(freq*i + 0 + phase_green) * width + center)
        b = int(math.sin(freq*i + 4 + phase_blue) * width + center)
        colors.append((r, g, b))
    return colors


def sine_cosine(grid_size, num_frames, duration, value, saturation,
                function="sin(x)+cos(y) + 0.001*f"):
    frames = []
    for f in range(0, num_frames):
        colors = []
        for x in range(0, grid_size.width):
            for y in range(0, grid_size.height):
                scope = {"sin": math.sin, "cos": math.cos, "x": x, "y": y, "f": f}
                v = eval(function, scope) % 1
                rgb = tuple(map(lambda val: int(val*255), colorsys.hsv_to_rgb(v, saturation, value)))
                colors.append(rgb)
        frames.append(blinkcomponents.Frame(duration, colors))
    return frames