##############################################################################
#
# Copyright (c) 2004 Zope Corporation and Contributors.
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

from setuptools import setup

__version__ = '0.0.1'

setup(
    name='zope.recursionissue',
    version=__version__,
    description='Test package to diagnose a Zope crash',
    long_description="",
    keywords='',
    author='Eric Steele',
    author_email='esteele@plone.org',
    url='',
    license='ZPL 2.1',
    packages=['zope', 'zope.recursionissue'],
    package_dir={'': ''},
    namespace_packages=['zope'],
    include_package_data=True,
    platforms='Any',
    zip_safe=False,
    install_requires=[
        'Products.Five',
    ],
    extras_require={
        'test': []
    },
    classifiers=[
    ],
)
