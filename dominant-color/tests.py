# encoding: utf-8
from unittest import TestCase

from api import dominant_color


class DominantColorTests(TestCase):

    def test_no_image(self):
        self.assertRaises(AssertionError, dominant_color, image_path=None)

