Introduction
============

This is the theme package of Institute of Mathematics, campus Juriquilla
(http://www.matem.unam.mx/juriquilla) site.

The project
===========

Based on Plone 4.3.10


Installation
============

.. code:: bash

    $ git clone https://github.com/gil-cano/cnga.core.git
    $ cd cnga.core
    $ virtualenv-2.7 --no-site-packages .
    $ bin/pip install --upgrade pip
    $ bin/pip install -r requirements.txt
    $ bin/python bootstrap-buildout.py
    $ bin/buildout


Theme preview
=============

**plone.themepreview** is a special Selenium and Robot Framework -powered
Sphinx-documentation base to take screenshots tour of your Plone in various
browser window sizes to highlight each theme's responsive design.

.. code:: bash

    $ ROBOT_CONFIGURE_PACKAGES=plone.app.widgets,cnga.core ROBOT_APPLY_PROFILES=cnga.core:default bin/sphinx-build src/plone.themepreview/source build

Code analysis
=============

.. code:: bash

    $ bin/code-analysis