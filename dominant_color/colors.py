# encoding: utf-8


class Color(object):

    def __init__(self, rgb):
        self.rgb = rgb

    @staticmethod
    def from_hex(hex_value):
        hex_value = hex_value.lstrip("#")
        l = len(hex_value)
        step = l // 3
        rgb = tuple(int(hex_value[i:i +step], 16) for i in range(0, l, step))
        return Color(rgb)