##############################################################################
#
# Copyright (c) 2010 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from setuptools import find_packages
from setuptools import setup


version = '4.0'

setup(
    name='Record',
    version=version,
    url='https://github.com/zopefoundation/Record',
    license='ZPL 2.1',
    description="Special Record objects used in Zope.",
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    long_description=open('README.rst').read() + '\n' +
        open('CHANGES.rst').read(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Web Environment",
        "Framework :: Zope :: 4",
        "Framework :: Zope :: 5",
        "License :: OSI Approved :: Zope Public License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    python_requires='>=3.7',
    install_requires=['ExtensionClass >= 4.1a1'],
    include_package_data=True,
    zip_safe=False,
)
