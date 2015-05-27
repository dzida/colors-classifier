# encoding: utf-8
from sys import maxint
from PIL import Image

from palettes import WEB_PALETTE, PaletteColorsCounter


def manhattan(p1, p2):
    return sum((abs(p1[i] - p2[i])) for i in range(len(p1)))

def _load_image(image_path):
    return Image.open(image_path)


def _get_image_colors(image):
    _size = image.size
    return image.getcolors(_size[0] * _size[1])


def dominant_color(image_path, palette=WEB_PALETTE, color_space="RGB"):
    """ Returns the most dominant color for a given image path.
    """
    assert image_path is not None
    # load image
    image = _load_image(image_path)

    # get colors from image
    image_colors = _get_image_colors(image)
    print image_colors

    # transcode to other space (image and palette)
    palette = palette
    image_in_space = image_colors

    def _get_nearest_color(color, palette):
        nearest_color = None
        nearest_distance = maxint
        for color_name, color_value in palette.iteritems():
            print color, color_value
            distance = manhattan(color, color_value)
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_color = color_name

        return nearest_color

    # calculate dominanat color based on distance from each image color to each color in palette (brute, kdtree?)
    palette_colors = PaletteColorsCounter.from_palette(palette)
    for color_count, color in image_colors:
        nearest_color_name = _get_nearest_color(color, palette)
        palette_colors[nearest_color_name] += color_count

    print "Palete colors", palette_colors
    # return the most dominant color
    return sorted([[k, v] for k, v in palette_colors.items()], key=lambda x: -1 * x[1])[0][0]