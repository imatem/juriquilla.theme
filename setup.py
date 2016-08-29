from setuptools import setup, find_packages

version = '1.0dev0'

setup(name='jurilla.theme',
      version=version,
      description="Diazo Theme Package for campus Juriquilla",
      long_description="",
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='',
      author='Informática Académica',
      author_email='informatica.academica@matem.unam.mx',
      url='https://github.com/imatem/juriquilla.theme',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['juriquilla'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
          'z3c.jbot',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
