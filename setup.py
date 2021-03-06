#! /usr/bin/env python

'''
author: Nicolas JEANNE
email: jeanne.n@chu-toulouse.fr
Created on 22 jan. 2020
'''

import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='viro-seq-utils',
    version='1.2.0',
    author='Nicolas Jeanne',
    author_email='jeanne.n@chu-toulouse.fr',
    description='Utilities modules for sequences, alignments and phylogeny from Toulouse virology laboratory.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://srvhpccode.icr.local/njeanne/viro-seq-utils',
    packages=setuptools.find_packages(),
    classifiers=[
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Science/Research'],
    keywords='alignment sequence net_charge',
    license='GNU General Public License',
    install_requires=[
        'biopython',
        'numpy',
        'pandas',
        'viro_seq_utils'
    ],
    zip_safe=False)
