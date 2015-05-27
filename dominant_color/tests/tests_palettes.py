# encoding: utf-8
from os import path
from unittest import TestCase

from dominant_color.palettes import PaletteColorsCounter, WEB_PALETTE


class PaletteColorCounterTests(TestCase):

    def test_from_web_palette(self):
        pcc = PaletteColorsCounter.from_palette(WEB_PALETTE)
        self.assertEquals(sorted(pcc.keys()), sorted(WEB_PALETTE.keys()))