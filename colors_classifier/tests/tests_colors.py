# encoding: utf-8
from unittest import TestCase

from colors_classifier.colors import Color


class ColorTests(TestCase):

    def test_ffffff(self):
        self.assertEquals(Color.from_hex("#ffffff").values(), (255, 255, 255))

    def test_000000(self):
        self.assertEquals(Color.from_hex("#000000").values(), (0, 0, 0))

    def test_ff0100(self):
        self.assertEquals(Color.from_hex("#FF0100").values(), (255, 1, 0))