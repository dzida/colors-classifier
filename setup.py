from setuptools import setup

setup(name='colors_classifier',
      version='0.1',
      description='Image analysis tools that allows to get the most dominant color name from image',
      url='https://github.com/dzida/colors-classifier',
      author='Lukasz Dziedzia',
      author_email='l.dziedzia@gmail.com',
      license='MIT',
      packages=['colors_classifier'],
      setup_requires = [
          'numpy'
      ],
      install_requires=[
          'numpy',
          'colormath',
          'baker',
          'Pillow'
      ],
      entry_points = {
          'console_scripts': [
              'colors-classifier=colors_classifier.cli:main'
          ],
      },
      zip_safe=False)