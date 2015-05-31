# encoding: utf-8
from os import path
from unittest import TestCase

from colors_classifier.api import extract_colors


class ImagesTests(TestCase):

    def test_valid_image_red(self):
        image_path = path.join(path.dirname(path.realpath(__file__)), "images/1x1/ff0000.jpg")
        image_palette = extract_colors(image_path)
        self.assertEquals(image_palette, ["red"])

    def test_valid_image_white(self):
        image_path = path.join(path.dirname(path.realpath(__file__)), "images/1x1/ffffff.jpg")
        image_palette = extract_colors(image_path)
        self.assertEquals(image_palette, ["white"])

    def test_valid_image_black(self):
        image_path = path.join(path.dirname(path.realpath(__file__)), "images/1x1/000000.jpg")
        image_palette = extract_colors(image_path)
        self.assertEquals(image_palette, ["black"])

    def test_bag(self):
        image_path = path.join(path.dirname(path.realpath(__file__)), "images/bag.jpg")
        palette = extract_colors(image_path, max_colors=2)
        self.assertEquals(palette, ["white", "dark pink"])