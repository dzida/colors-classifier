# encoding: utf-8
import baker

from colors_classifier import api

@baker.command
def extract_colors(max_colors=1, *args):

    results = {}
    for image_path in args:
        colors = api.extract_colors(image_path, max_colors=max_colors)
        results[image_path] = colors

    return results


def main():
    baker.run()


if __name__ == "__main__":
    main()