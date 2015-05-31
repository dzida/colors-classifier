# encoding: utf-8
from unittest import TestCase

from colors_classifier.palettes import PaletteColorsCounter, Palette, WEB_PALETTE, XKCD_49_PALETTE
from colors import Color


class PaletteColorCounterTests(TestCase):

    def test_create_from_web_palette(self):
        palette = Palette(**WEB_PALETTE)
        pcc = PaletteColorsCounter.from_palette(palette)
        self.assertEquals(sorted(pcc.keys()), sorted(palette.names))


class PaletteTests(TestCase):

    def test_color_names(self):
        self.assertEquals(len(Palette(**WEB_PALETTE).names), len(WEB_PALETTE.keys()))

    def test_nearest_web_white(self):
        palette = Palette(**WEB_PALETTE)
        white = Color.from_hex("#FFFFFF")
        self.assertEquals(palette.find_nearest(white)[0], "white")
        self.assertEquals(palette.find_nearest(white)[1], white)

    def test_nearest_web_almost_white(self):
        palette = Palette(**WEB_PALETTE)
        almost_white = Color.from_hex("#FFFFFe")
        white = Color.from_hex("#FFFFFF")
        self.assertEquals(palette.find_nearest(almost_white)[0], "white")
        self.assertEquals(palette.find_nearest(almost_white)[1], white)

    def test_nearest_web_red(self):
        palette = Palette(**WEB_PALETTE)
        red = Color.from_hex("#FF0000")
        self.assertEquals(palette.find_nearest(red)[0], "red")
        self.assertEquals(palette.find_nearest(red)[1], red)

    def test_palette_has_index(self):
        palette = Palette(a=Color.from_hex("#FF0000"))

        index = palette._tree
        self.assertTrue(index is not None)

    # def test_rebuild_changes_index(self):
    #     palette = Palette()
    #     palette["a"] = (1, 2)
    #
    #     index = palette.distance_index
    #     palette["b"] = (2, 4)
    #
    #     self.assertNotEquals(palette.distance_index, index)