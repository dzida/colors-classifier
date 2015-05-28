# encoding: utf-8
from os import path
from unittest import TestCase

from colors_classifier.palettes import PaletteColorsCounter, WEB_PALETTE


class PaletteColorCounterTests(TestCase):

    def test_create_from_web_palette(self):
        pcc = PaletteColorsCounter.from_palette(WEB_PALETTE)
        self.assertEquals(sorted(pcc.keys()), sorted(WEB_PALETTE.keys()))