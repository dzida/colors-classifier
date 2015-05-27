# encoding: utf-8
from dominant_color.colors import Color


# pallete of 16 commonly used web colors
# in accordance to HTML 4.01
# (http://en.wikipedia.org/wiki/Web_colors)
WEB_PALETTE = {
    "white":    Color.from_hex("#FFFFFF").rgb,
    "silver":   Color.from_hex("#C0C0C0").rgb,
    "gray":     Color.from_hex("#808080").rgb,
    "black":    Color.from_hex("#000000").rgb,
    "red":      Color.from_hex("#FF0000").rgb,
    "maroon":   Color.from_hex("#800000").rgb,
    "yellow":   Color.from_hex("#FFFF00").rgb,
    "olive":    Color.from_hex("#808000").rgb,
    "lime":     Color.from_hex("#00FF00").rgb,
    "green":    Color.from_hex("#008000").rgb,
    "aqua":     Color.from_hex("#00FFFF").rgb,
    "teal":     Color.from_hex("#008080").rgb,
    "blue":     Color.from_hex("#0000FF").rgb,
    "navy":     Color.from_hex("#000080").rgb,
    "fuchsia":  Color.from_hex("#FF00FF").rgb,
    "purple":   Color.from_hex("#800080").rgb
}

PALETTES = {
    "web": WEB_PALETTE
}


class PaletteColorsCounter(dict):

    @staticmethod
    def from_palette(palette):
        return PaletteColorsCounter(**{k:0 for k in palette.keys()})