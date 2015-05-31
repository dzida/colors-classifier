# encoding: utf-8
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color


class ColorSpace(object):
    """ Available spaces. """
    LAB = "LAB"
    RGB = "RGB"


class Color(sRGBColor):
    """ Colors wrapper.

    Provides a simple interface for creating images and representing them as a space coordinates.

    Wraps functionality from colormath.color_objects
    """
    def __eq__(self, other):
        return self.values() == other.values()

    @staticmethod
    def from_hex(hex_str):
        """ Creates a color instance from hex rgb notation. """
        return Color(*sRGBColor.new_from_rgb_hex(hex_str).get_value_tuple())

    def values(self, color_space=ColorSpace.RGB):
        """ Returns color values tuple in a given space.

         By default color_space is RGB, if None it's also coerced to RGB.
        """
        color_space = color_space or ColorSpace.RGB

        if color_space == ColorSpace.RGB:
            return self.get_upscaled_value_tuple()
        elif color_space == ColorSpace.LAB:
            # use __lab_color attr as a cache for converted color to LAB space
            color = getattr(self, "__lab_color", None)
            if color is None:
                color = convert_color(self, LabColor)
                setattr(self, "__lab_color", color)

            return color.get_value_tuple()
