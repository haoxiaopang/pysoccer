#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import soccer

from setuptools import setup, find_packages

with open('README.rst', 'rb') as f_readme:
    readme = f_readme.read().decode('utf-8')

packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

setup(
    name='soccerdata',
    version=soccer.__version__,
    keywords=['soccer', 'football', 'football-data'],
    description='Soccer data for python programmers.',
    long_description=readme,
    author='haoxiaopang',
    author_email='yanshia@163.com',
    license='MIT',
    url='https://github.com/haoxiaopang/soccerdata',
    install_requires=['requests'],
    packages=packages,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Information Technology',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 3 :: Only',
    ],
    entry_points={
        'console_scripts': [
            'soccer = soccer.main:main'
        ]
    }
)
