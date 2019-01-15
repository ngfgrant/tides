# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from admiralty_tides import __version__
from setuptools import setup, find_packages


with open("README.md") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.md") as history_file:
    history = history_file.read()

setup(
    name='admirality-tides',
    version=__version__,
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={
        "admiralty-tides": "admiralty-tides"
    },
    description='An wrapper for the Admiralty tides API',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Niall Grant',
    license='Apache2',
    author_email='ngfgrant@gmail.com',
    url='https://github.com/ngfgrant/admiralty-tides',
    keywords=['admiralty', 'tides', 'api-wrapper'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    python_requires='>=3',
)
