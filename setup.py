import imp
import os
import json
from setuptools import setup, find_packages

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

setup(
        name = 'vectorize',
        description = (
            "Vectorize images in Python"),
        version = '0.1.0',
        packages = find_packages(),
        include_package_data = True,
        zip_safe = False,
        install_requires = [
            'Pillow==3.4.2'
        ],
        test_requires = [
            'coverage',
            'mock',
            'nose'
        ],
        author = 'Karl Ding',
        author_email = 'karlding@users.noreply.github.com',
        url = 'https://github.com/karlding/vectorize',
)
