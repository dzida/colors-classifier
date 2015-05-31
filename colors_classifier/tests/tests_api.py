# encoding: utf-8
from os import path
from unittest import TestCase

from colors_classifier.api import extract_colors


class PaletteExtractionTests(TestCase):
    EXAMPLE_IMAGE = path.join(path.dirname(path.realpath(__file__)), "images/lenna.jpg")

    def test_not_existing_image(self):
        self.assertRaises(IOError, extract_colors, image_path="/not-existing-image.jpg")

    def test_valid_image(self):
        image_palette = extract_colors(self.EXAMPLE_IMAGE)
        self.assertTrue(image_palette)

    def test_scale_down_does_not_change_results_if_small(self):
        palette_from_scale_1 = extract_colors(self.EXAMPLE_IMAGE, max_colors=4, scale_by=1.0)
        palette_from_scale_2 = extract_colors(self.EXAMPLE_IMAGE, max_colors=4, scale_by=0.9)
        self.assertEquals(palette_from_scale_1, palette_from_scale_2)

    def test_scale_change_results_if_significant(self):
        palette_from_scale_1 = extract_colors(self.EXAMPLE_IMAGE, max_colors=4, scale_by=1.0)
        palette_from_scale_2 = extract_colors(self.EXAMPLE_IMAGE, max_colors=4, scale_by=0.1)
        self.assertNotEquals(palette_from_scale_1, palette_from_scale_2)

    def test_max_colors_1(self):
        image_palette = extract_colors(self.EXAMPLE_IMAGE, max_colors=1)
        self.assertEquals(len(image_palette), 1)

    def test_max_colors_3(self):
        image_palette = extract_colors(self.EXAMPLE_IMAGE, max_colors=3)
        self.assertEquals(len(image_palette), 3)
