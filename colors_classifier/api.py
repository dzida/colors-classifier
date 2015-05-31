# encoding: utf-8
import logging

# enabled logging generates huge overhead on color space conversions
logging.disable(logging.DEBUG)


from colors_classifier.image_utils import get_image_colors, load_image
from colors_classifier.palettes import XKCD_49_PALETTE, PaletteColorsCounter, Palette
from colors_classifier.colors import ColorSpace


def classify_colors(image_colors, palette):
    """ Returns a dictionary object that maps color name with number of occurrences on image. """
    palette_colors = PaletteColorsCounter.from_palette(palette)
    for color_count, color in image_colors:
        nearest_color_name, _ = palette.find_nearest(color)
        palette_colors[nearest_color_name] += color_count

    return palette_colors


def extract_colors(image_path, palette=XKCD_49_PALETTE, color_space=ColorSpace.LAB, max_colors=8, scale_by=0.25):
    """ Returns list of most represented colors on image, ordered by number of appearances.

    Params:
    image_path - image location
    palette - colors palette used for examination (either dict or Palette instance)
    color_space - color space for which calculations are performed (either LAB or RGB)
    max_colors - maximum number of colors in palette (can be less if less number of colors has been identified)
    scale_by - ratio by which image is reduced before an examination, use this for optimization, number [0.0, 1.0]

    Returns:
    list of color names from a palette specification, ordered by number of occurrences in an image.
    """
    # load image
    image = load_image(image_path, scale_by=scale_by)

    # get colors from image
    image_colors = get_image_colors(image)

    # create palette
    if isinstance(palette, dict):
        palette = Palette(color_space=color_space, **palette)
    else:
        # TODO: better handle mismatch between provided color_space arg and palette configuration
        assert palette.color_space == color_space

    colors = classify_colors(image_colors, palette=palette)

    # order by the most significant
    colors = sorted([[k, v] for k, v in colors.items()], key=lambda x: -1 * x[1])

    # remove colors with no representation on image
    colors = filter(lambda x: x[1] > 0, colors)

    return [c[0] for c in colors][:max_colors]