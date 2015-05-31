# encoding: utf-8
import baker
from json import dumps

from colors_classifier import api
from colors_classifier.colors import ColorSpace
from colors_classifier.palettes import PALETTES


@baker.command(name="extract_colors")
def extract_colors_from_files(max_colors=1, scale_by=0.5, color_space=ColorSpace.LAB,
                              palette_name="xkcd_49", fail_silently=True,  *args):
    """ Wraps api.extract_color as a command line command.

     Allows to specify many files for examination (*args).
     For parameters, consult with api.extract_color.

     If an image cannot be read it is omitted from results, unless fail_silently flag is set to False.

     Returns JSON-formatted object mapping image path to list of colors detected by an algorithm.
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
            results[image_path] = colors

    return dumps(results)


def main():
    baker.run()


if __name__ == "__main__":
    main()