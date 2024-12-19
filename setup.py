#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    desc = f.read()

setup(
    name='wappalyzer',
    version='0.9.0',
    description='Wappalyzer-based tech stack detection library',
    long_description=desc,
    long_description_content_type='text/markdown',
    author='Somdev Sangwan',
    author_email='s0md3v@gmail.com',
    license='GNU General Public License v3 (GPLv3)',
    url='https://github.com/s0md3v/wappalyzer',
    download_url='https://github.com/s0md3v/wappalyzer/archive/0.9.0.zip',
    packages=find_packages(),
    package_data={'wappalyzer': ['data/*']},
    install_requires=[
        'requests',
        'huepy',
        'selenium'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Topic :: Security',
        'License :: OSI Approved :: GNU General Public License v3',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points={
        'console_scripts': [
            'wappalyzer = wappalyzer.__main__:main'
        ]
    },
    keywords=['wappalyzer', 'bug bounty', 'pentesting', 'security'],
)
