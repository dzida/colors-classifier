# encoding: utf-8
from os import path
from unittest import TestCase

from colors_classifier.api import dominant_color, extract_palette


class DominantColorTests(TestCase):

    def test_no_image(self):
        self.assertRaises(AssertionError, dominant_color, image_path=None)

    def test_not_existing_image(self):
        self.assertRaises(IOError, dominant_color, image_path="/not-existing-image.jpg")

    def test_valid_image_red(self):
        image_path = path.join(path.dirname(path.realpath(__file__)), "images/1x1/ff0000.jpg")
        selected = dominant_color(image_path)
        self.assertEquals(selected, "red")

    def test_valid_image_white(self):
        image_path = path.join(path.dirname(path.realpath(__file__)), "images/1x1/ffffff.jpg")
        selected = dominant_color(image_path)
        self.assertEquals(selected, "white")

    def test_valid_image_black(self):
        image_path = path.join(path.dirname(path.realpath(__file__)), "images/1x1/000000.jpg")
        selected = dominant_color(image_path)
        self.assertEquals(selected, "black")

    def test_bag(self):
        image_path = path.join(path.dirname(path.realpath(__file__)), "images/bag.jpg")
        selected = dominant_color(image_path)
        self.assertEquals(selected, "white")


class PaletteExtractionTests(TestCase):

    def test_no_image(self):
        self.assertRaises(AssertionError, dominant_color, image_path=None)

    def test_not_existing_image(self):
        self.assertRaises(IOError, dominant_color, image_path="/not-existing-image.jpg")

    def test_valid_image_red(self):
        image_path = path.join(path.dirname(path.realpath(__file__)), "images/1x1/ff0000.jpg")
        palette = extract_palette(image_path)
        self.assertEquals(palette, ["red"])

    def test_valid_image_white(self):
        image_path = path.join(path.dirname(path.realpath(__file__)), "images/1x1/ffffff.jpg")
        palette = extract_palette(image_path)
        self.assertEquals(palette, ["white"])

    def test_valid_image_black(self):
        image_path = path.join(path.dirname(path.realpath(__file__)), "images/1x1/000000.jpg")
        palette = extract_palette(image_path)
        self.assertEquals(palette, ["black"])

    def test_bag(self):
        image_path = path.join(path.dirname(path.realpath(__file__)), "images/bag.jpg")
        palette = extract_palette(image_path, max_colors=2)
        self.assertEquals(palette, ["white", "dark pink"])