#! /usr/bin/env python

from setuptools import setup

setup(
    name='mdx_gridtables',
    version='1.1',
    author='Mihkel Selgal',
    author_email='kasvataja122@hot.ee',
    description='Python-Markdown extension to add grid_table support to Markdown',
    url='http://activearchives.org/',
    py_modules=['mdx_girdtables'],
    install_requires=['Markdown>=2.0',],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)