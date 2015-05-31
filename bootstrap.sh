#! /bin/bash

virtualenv colors_classifier_env
source colors_classifier_env/bin/activate
pip install -r requirements.txt
python setup.py install