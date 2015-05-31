# encoding: utf-8
from PIL import Image

from colors_classifier.colors import Color


def load_image(image_path, scale_by=None):
    """ Loads and optionally resizes an image from image_path. """
    def _scaled(dim_size):
        return int(dim_size * scale_by) or 1

    image = Image.open(image_path)
    if scale_by:
        image.thumbnail((_scaled(image.size[0]), _scaled(image.size[1])))
    return image


def get_image_colors(image):
    """ Get colors from image.

    Returns list of two-tuples (count, Color()), where
    count - number of color occurrences on image
    Color() - instance of a color
    """
    _size = image.size
    return ((count, Color(*rgb_color_tuple, is_upscaled=True))
            for count, rgb_color_tuple
            in image.getcolors(_size[0] * _size[1]))
