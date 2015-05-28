# colors-classifier
Image analysis tools that allows to get the most dominant color name from image.

## Problem
Having an image, what are the most dominant colors represented on it?
There are a few concerns that need to be examined before addressing this issue.

### Base colors palette
A color palette can be more or less precise. Each person can have different 'sense' when naming colors.

Base colors palette (understood as a mapping between base colors and their human-readable names) is an entry point for
this analysis. There are some popular palettes defined in software systems, eg. web palette (http://en.wikipedia.org/wiki/Web_colors),
X11 palette (http://en.wikipedia.org/wiki/X11_color_names), however is doubtful if those correspond to human perception.

There are some experiments in regard to find values of given colors. An interesting
one is a survey based experiment, created by xkcd (http://blog.xkcd.com/2010/05/03/color-survey-results/). Over 5M of
colors were named, during 220k+ sessions. It resulted in a quality dataset of color name-value pairs.

One of the goals of the program is to left base color palette configured by user. By default a few color palettes are
provided (eg. web, xkcd).

### Human perception vs. digital colors
Colors perception is subjective by it's nature. Additionally there are some technical limitations that affects colors perception
when using digital devices (eg. RGB vs natural color perception). This might be significant matter in a solution that
implements colors comparison algorithms.

To provide best results in various cases it is configurable which color space is used for analysis.
- RGB
- L*a*b*

## API

### CLI
Mentioned functions are also available from a command line interface:

```
colors-classifier dominant_colors <IMAGE_PATHS> --palette web --color_space rgb
```

## Dependencies
colormath - 2.2.1  (RGB-LAB conversion)
numpy - 1.9.2  (colormath dependency)
baker - 1.3  (CLI helper)

