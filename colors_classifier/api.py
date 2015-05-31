# encoding: utf-8
import logging

# enabled logging generates huge overhead on color space conversions
logging.disable(logging.DEBUG)


from colors_classifier.image_utils import get_image_colors, load_image
from colormath.color_conversions import convert_color


from palettes import XKCD_49_PALETTE, PaletteColorsCounter, Palette


def classify_colors(image_colors, palette):
    """ Returns list of human-friendly color names, ordered by appearance in a given image. """

    # calculate dominant color based on distance from each image color to each color in palette (brute, kdtree?)
    palette_colors = PaletteColorsCounter.from_palette(palette)
    for color_count, color in image_colors:
        nearest_color_name, _ = palette.find_nearest(color)
        palette_colors[nearest_color_name] += color_count

    return palette_colors


def extract_colors(image_path, palette=XKCD_49_PALETTE, color_space="RGB", max_colors=8, scale_by=0.25):
    """ Returns list of most represented colors on image, ordered by number of appearances.

    Params:
    max_colors - maximum number of colors in palette (can be less if less number of colors has been identified)
    """
    # load image
    image = load_image(image_path, scale_by=scale_by)

    # get colors from image
    image_colors = get_image_colors(image)

    colors = classify_colors(image_colors, palette=Palette(**palette))

    # order by appearances
    colors = sorted([[k, v] for k, v in colors.items()], key=lambda x: -1 * x[1])
    # remove colors with no representation on image
    colors = filter(lambda x: x[1] > 0, colors)

    return [c[0] for c in colors][:max_colors]