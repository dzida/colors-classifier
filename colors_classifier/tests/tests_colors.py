# encoding: utf-8
from os import path
from unittest import TestCase

from colors_classifier.colors import Color


class ColorTests(TestCase):

    def test_ffffff(self):
        self.assertEquals(Color.from_hex("#ffffff").rgb, (255, 255, 255))

    def test_000000(self):
        self.assertEquals(Color.from_hex("#000000").rgb, (0, 0, 0))