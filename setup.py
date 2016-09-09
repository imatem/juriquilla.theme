# -*- coding: utf-8 -*-
"""Installer for the juriquilla.theme package."""

from setuptools import find_packages
from setuptools import setup

version = '1.0dev0'

setup(
    name='juriquilla.theme',
    version=version,
    description="Theme Package for campus Juriquilla",
    long_description="",
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='',
    author='Informática Académica',
    author_email='informatica.academica@matem.unam.mx',
    url='https://github.com/imatem/juriquilla.theme',
    license='GPL version 2',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['juriquilla'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
      'setuptools',
      'plone.app.theming',
      'plone.app.themingplugins'
      'z3c.jbot',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
        ],
    },
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
