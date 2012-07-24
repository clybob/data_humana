# encoding: utf-8

from distutils.core import setup
from setuptools import find_packages

setup(
    name='data_humana',
    version='0.1.0',
    author='Romulo Tavares',
    author_email='clybob@hotmail.com',
    packages=find_packages(),
    license='GPL',
    description='Dada uma determinada data, calcula a diferença entre ela ' +
                'e a data atual e apresenta em forma de texto, ex: 1 ano atrás'
)
