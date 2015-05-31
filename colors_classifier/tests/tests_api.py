# encoding: utf-8
from os import path
from unittest import TestCase

from colors_classifier.api import extract_colors


class PaletteExtractionTests(TestCase):

    def test_no_image(self):
        self.assertRaises(AssertionError, extract_colors, image_path=None)

    def test_not_existing_image(self):
        self.assertRaises(IOError, extract_colors, image_path="/not-existing-image.jpg")

    def test_valid_image(self):
        image_path = path.join(path.dirname(path.realpath(__file__)), "images/1x1/ff0000.jpg")
        image_palette = extract_colors(image_path)
        self.assertEquals(image_palette, ["red"])