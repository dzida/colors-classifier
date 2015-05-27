# encoding: utf-8
from os import path
from unittest import TestCase

from dominant_color.api import dominant_color


class DominantColorTests(TestCase):

    def test_no_image(self):
        self.assertRaises(AssertionError, dominant_color, image_path=None)

    def test_not_existing_image(self):
        self.assertRaises(IOError, dominant_color, image_path="/not-existing-image.jpg")

    def test_valid_image(self):
        image_path = path.join(path.dirname(path.realpath(__file__)), "images/1x1/ff0000.jpg")
        selected = dominant_color(image_path)
        self.assertEquals(selected, "red")