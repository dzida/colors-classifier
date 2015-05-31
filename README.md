# colors-classifier
Image analysis tools that allows to get the most dominant human friendly color names from an image.

## Problems
Having an image, what are the most dominant colors on it?
Would two different people name colors the same way?
How all possible colors that could be displayed (eg. 24bit RGB = 65536 colors) should be assigned to
a "human friendly name" of a color.
How to interpret a difference between color and how it should be calculated?

### Model colors palette
A color palette can be more or less precise. Each person can have different 'sense' when naming colors.

Model colors palette (understood as a mapping between base colors and their human-readable names) is an entry point for
this analysis. There are some popular palettes defined in software systems, eg. web palette (http://en.wikipedia.org/wiki/Web_colors),
X11 palette (http://en.wikipedia.org/wiki/X11_color_names), however is doubtful if those correspond to human perception.

There are some experiments which aim to create a palette closer to a general human perception. An interesting
one is a survey based experiment, created by xkcd (http://blog.xkcd.com/2010/05/03/color-survey-results/). Over 5M of
color records were named, during 220k+ user sessions. It resulted in a quality dataset for colors name-value pairs.

One of the goals of the program is to left base color palette to be configured by an user. By default a few color palettes are
provided (web, xkcd). Interesting results were achieved on a palette of 49 top colors from xkcd set.

### Human perception vs. digital colors
Colors perception is subjective by it's nature. Additionally there are some technical limitations that affect colors perception
when using digital devices (eg. RGB vs. natural color perception). This might be significant matter in a solution that
implements colors comparison algorithms.

To provide best results in various cases it is configurable which color space is used for analysis.
- RGB - popular technical colors encoding
- L*a*b* - colors encoding that is considered as the closest one to the human perception

## Program interface

### CLI
Upon installation, main entry point is a 'colors-classifier extract_colors' program:

```
colors-classifier extract_colors flag.jpg bag.jpg --max_colors 4 --palette_name xkcd_49 --color_space LAB --scale_by 0.25
{"dark pink": ["bag.jpg"], "navy blue": ["flag.jpg"], "salmon": ["bag.jpg"], "grey": ["flag.jpg"], "maroon": ["bag.jpg"], "white": ["flag.jpg", "bag.jpg"], "red": ["flag.jpg"]}
```

For more information about program options:
```
colors-classifier extract_colors --help
```

Output is a JSON-formatted string mapping a file names to list of colors.

### Python package
Program can be also used as a dependency for other Python programs:

```
from colors_classifier.api import extract_colors
from colors_classifier.palettes import Palette, WEB_PALETTE
from colors_classifier.colors import ColorSpace

extract_colors("lenna.jpg",
               palette=WEB_PALETTE,
               max_colors=4,
               scale_by=0.5,
               color_space=ColorSpace.LAB)
```

## Optimization notes
Optimization techniques used to increase program's performance:
* KD-tree used as an algorithm for finding nearest color (kNN, k=1)
* it can be assumed in majority of cases that scaling down image size will not have negative effect on colors information, and will positively impact computation time (scale_by parameter)
* image data is aggregated into a set, grouped by a color value (each color value has assigned a count of occurrences in image). THanks to this number of pixels that need to be examined is reduced.


## Dependencies
Version numbers refer to dependencies versions used in tests.
* colormath - 2.1.1  (RGB-LAB conversion)
* numpy - 1.9.2  (colormath dependency)
* baker - 1.3  (CLI helper)
* Pillow - 2.8.1 (imaging library)
* scikit-learn - 0.16.1 (knn algorithm implementation)
* scipy - 0.15.1 (scikit-learn dependency)