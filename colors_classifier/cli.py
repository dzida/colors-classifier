# encoding: utf-8
import baker
from json import dumps

from colors_classifier import api
from colors_classifier.colors import ColorSpace


@baker.command(name="extract_colors")
def extract_colors_from_files(max_colors=1, scale_by=0.5, color_space=ColorSpace.LAB,  *args):
    """ Wraps api.extract_color as a command line command.

     Allows to specify many files for examination (*args).
     For parameters, consult with api.extract_color.

     Returns JSON-formated object mapping image path to list of colors detected by an algorithm.
    """
    results = {}

    for image_path in args:
        colors = api.extract_colors(image_path, max_colors=max_colors, scale_by=scale_by, color_space=color_space)
        results[image_path] = colors

    return dumps(results)


def main():
    baker.run()


if __name__ == "__main__":
    main()