# encoding: utf-8
from sys import maxint
from PIL import Image
import logging

# enabled logging generates huge overhead on color space conversions
logging.disable(logging.DEBUG)

from colors_classifier.colors import Color
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie1976

from palettes import XKCD_49_PALETTE, PaletteColorsCounter


def _load_image(image_path):
    return Image.open(image_path)


def _get_image_colors(image):
    _size = image.size
    return ((count, Color(*rgb_color_tuple, is_upscaled=True)) for count, rgb_color_tuple in image.getcolors(_size[0] * _size[1]))


def classify_colors(image_path, palette=XKCD_49_PALETTE, color_space="RGB"):
    """ Returns list of human-friendly color names, ordered by appearance in a given image. """
    assert image_path is not None
    # load image
    image = _load_image(image_path)

    image.thumbnail((400, 300))

    # get colors from image
    image_colors = _get_image_colors(image)

    # calculate dominant color based on distance from each image color to each color in palette (brute, kdtree?)
    palette_colors = PaletteColorsCounter.from_palette(palette)
    for color_count, color in image_colors:
        nearest_color_name, _ = palette.find_nearest(color)
        palette_colors[nearest_color_name] += color_count

    return palette_colors


def extract_colors(image_path, palette=XKCD_49_PALETTE, color_space="RGB", max_colors=8):
    """ Returns list of most represented colors on image, ordered by number of appearances.

    Params:
    max_colors - maximum number of colors in palette (can be less if less number of colors has been identified)
    """
    colors = classify_colors(image_path, palette=palette, color_space=color_space)

    # order by appearances
    colors = sorted([[k, v] for k, v in colors.items()], key=lambda x: -1 * x[1])
    # remove colors with no representation on image
    colors = filter(lambda x: x[1] > 0, colors)

    return [c[0] for c in colors][:max_colors]