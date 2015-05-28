# encoding: utf-8
import baker


@baker.command
def extract_colors(max_colors=1, *args):
    print max_colors
    print args


def main():
    baker.run()


if __name__ == "__main__":
    main()