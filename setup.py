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

from os.path import join
from setuptools import setup, find_packages, Extension

setup(name='Record',
    version='2.13.1dev',
    url='http://pypi.python.org/pypi/Record',
    license='ZPL 2.1',
    description="Special Record objects used in Zope2.",
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    long_description=open('README.txt').read() + '\n' +
        open('CHANGES.txt').read(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    ext_modules=[Extension(
        name='Record._Record',
        include_dirs=['include', 'src'],
        sources=[join('src', 'Record', '_Record.c')],
        depends=[join('include', 'ExtensionClass', 'ExtensionClass.h')]),
    ],
    install_requires=['ExtensionClass'],
    include_package_data=True,
    zip_safe=False,
)
