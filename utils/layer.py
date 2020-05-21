import os
from .clean import clean_layer


def layer():
    clean_layer()
    os.system('pip3 install --isolated --disable-pip-version-check -Ur requirements.txt -t ./layer/')

