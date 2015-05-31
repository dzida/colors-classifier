# encoding: utf-8
from os import path
from unittest import TestCase

from colors_classifier.api import extract_colors
from colors_classifier.palettes import Palette, WEB_PALETTE


class ImagesTests(TestCase):

    def _full_path(self, path_end):
        return path.join(path.dirname(path.realpath(__file__)), path_end)

    def test_simple_red(self):
        image_path = self._full_path("images/1x1/ff0000.jpg")
        image_palette = extract_colors(image_path)
        self.assertEquals(image_palette, ["red"])

    def test_simple_white(self):
        image_path = self._full_path("images/1x1/ffffff.jpg")
        image_palette = extract_colors(image_path)
        self.assertEquals(image_palette, ["white"])

    def test_simple_black(self):
        image_path = self._full_path("images/1x1/000000.jpg")
        image_palette = extract_colors(image_path)
        self.assertEquals(image_palette, ["black"])

    def test_bag(self):
        image_path = self._full_path("images/bag.jpg")
        palette = extract_colors(image_path, max_colors=2)
        self.assertEquals(palette, ["white", "dark pink"])

    def test_flag(self):
        image_path = self._full_path("images/flag.jpg")
        palette = extract_colors(image_path, max_colors=5)
        self.assertEquals(palette, ["blue", "red", "white"])

    def test_sign(self):
        image_path = self._full_path("images/flag.jpg")
        palette = extract_colors(image_path, max_colors=3)
        self.assertEquals(palette, ["yellow", "black", "teal"])