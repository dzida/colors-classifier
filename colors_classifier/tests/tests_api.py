# encoding: utf-8
from os import path
from unittest import TestCase

from colors_classifier.api import find_dominant_color


class DominantColorTests(TestCase):

    def test_no_image(self):
        self.assertRaises(AssertionError, find_dominant_color, image_path=None)

    def test_not_existing_image(self):
        self.assertRaises(IOError, find_dominant_color, image_path="/not-existing-image.jpg")

    def test_valid_image_red(self):
        image_path = path.join(path.dirname(path.realpath(__file__)), "images/1x1/ff0000.jpg")
        selected = find_dominant_color(image_path)
        self.assertEquals(selected, "red")

    def test_valid_image_black(self):
        image_path = path.join(path.dirname(path.realpath(__file__)), "images/1x1/000000.jpg")
        selected = find_dominant_color(image_path)
        self.assertEquals(selected, "black")

    def test_4k(self):
        image_path = path.join(path.dirname(path.realpath(__file__)), "images/4k/white.jpg")
        selected = find_dominant_color(image_path)
        self.assertEquals(selected, "blue")