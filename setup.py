#!/usr/bin/env python
# Setup.py file helps to set up the environment
from setuptools import setup
from web import __version__

setup(name='web.py',
      version=__version__,
      description='web.py: makes web apps',
      author='Aaron Swartz',
      author_email='me@aaronsw.com',
      maintainer='Anand Chitipothu',
      maintainer_email='anandology@gmail.com',
      url='http://webpy.org/',
      packages=['web', 'web.contrib'],
      install_requires=[
          'cheroot',
      ],
      long_description="Think about the ideal way to write a web app. Write the code to make it happen.",
      license="Public domain",
      platforms=["any"],
     )
