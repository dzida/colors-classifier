# encoding: utf-8
import baker
from json import dumps

from colors_classifier import api
from colors_classifier.colors import ColorSpace
from colors_classifier.palettes import PALETTES


@baker.command(name="extract_colors")
def extract_colors_from_files(max_colors=1, scale_by=0.5, color_space=ColorSpace.LAB,
                              palette_name="xkcd_49", fail_silently=True,  *args):
    """ Returns color: [files] mapping for a given set of files.

     Allows to specify many files for examination (*args).

     :param palette_name: colors palette name used for examination (web, xkcd_49 or xkcd_full)
     :param color_space: color space for which calculations are performed (either LAB or RGB)
     :param max_colors: maximum number of colors in palette (can be less if less number of colors has been identified)
     :param scale_by: ratio by which image is reduced before an examination, use this for optimization, number [0.0, 1.0]
     :param fail_silently: tells if program should continue on image read errors

     Returns JSON-formatted object mapping colors to a list of images used for examination.
    """
    results = {}

    # get palette by name
    palette = PALETTES[palette_name]

    for image_path in args:
        try:
            colors = api.extract_colors(image_path,
                                        palette=palette,
                                        max_colors=max_colors,
                                        scale_by=scale_by,
                                        color_space=color_space)
        except IOError:
            if not fail_silently:
                raise
        else:
            for color in colors:
                if color not in results:
                    results[color] = []
                results[color].append(image_path)

    return dumps(results)


def main():
    baker.run()


if __name__ == "__main__":
    main()