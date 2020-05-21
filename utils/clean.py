import os


def clean_layer():
    os.system('rm -fr layer/ dist/ htmlcov/ site/ .eggs/ .tox/')
    os.system("find . -name '*.egg-info' -exec rm -fr {} +")
    os.system("find . -name '.DS_Store' -exec rm -fr {} +")
    os.system("find . -name '*.egg' -exec rm -f {} +")
    os.system("find . -name '*.pyc' -exec rm -f {} +")
    os.system("find . -name '*.pyo' -exec rm -f {} +")
    os.system("find . -name '*~' -exec rm -f {} +")
    os.system("find . -name '__pycache__' -exec rm -fr {} +")


def clean():
    os.system('rm -fr build/ dist/ htmlcov/ site/ .eggs/ .tox/')
    os.system("find . -name '*.egg-info' -exec rm -fr {} +")
    os.system("find . -name '.DS_Store' -exec rm -fr {} +")
    os.system("find . -name '*.egg' -exec rm -f {} +")
    os.system("find . -name '*.pyc' -exec rm -f {} +")
    os.system("find . -name '*.pyo' -exec rm -f {} +")
    os.system("find . -name '*~' -exec rm -f {} +")
    os.system("find . -name '__pycache__' -exec rm -fr {} +")


def clean_all():
    clean()
    clean_layer()