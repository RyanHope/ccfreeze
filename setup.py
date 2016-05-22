#! /usr/bin/env python

import sys

from setuptools import setup

version = "1.1.5"


def main():
    install_requires = ["altgraph>=0.12", "ccfreeze-loader>=1.1.0"]

    if sys.platform == 'win32':
        install_requires.append("pefile")

    setup(name="bbfreeze",
          version=version,
          entry_points={
                       "console_scripts": ['bb-freeze = bbfreeze:main', 'bbfreeze = bbfreeze:main'],
                                          "distutils.commands": [
                                           "bdist_bbfreeze = bbfreeze.bdist_bbfreeze:bdist_bbfreeze"]},
          install_requires=install_requires,
          packages=['bbfreeze', 'bbfreeze.modulegraph'],
          zip_safe=False,
          maintainer="Josh Brown",
          maintainer_email="cars1189@aol.com",
          url="https://pypi.python.org/pypi/ccfreeze/",
          description="create standalone executables from python scripts",
          platforms="Linux Windows",
          license="zlib/libpng license",
          classifiers=[
                      "Development Status :: 5 - Production/Stable",
                      "License :: OSI Approved :: zlib/libpng License",
                      "Intended Audience :: Developers",
                      "Programming Language :: Python",
                      "Programming Language :: Python :: 2",
                      "Programming Language :: Python :: 2.7",
                      "Topic :: Software Development :: Build Tools",
                      "Topic :: System :: Software Distribution"],
          long_description=open("README.rst").read())

if __name__ == '__main__':
    main()
