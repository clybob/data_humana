# encoding: utf-8

from distutils.core import setup

setup(
    name='data_humana',
    version='0.1.1',
    author='Romulo Tavares',
    author_email='clybob@hotmail.com',
    packages=['data_humana'],
    license='GPL',
    url='https://github.com/clybob/data_humana.git',
    description='Dada uma determinada data, calcula a diferença entre ela e ' +
                'a data atual e apresenta em forma de texto, ex: 1 ano',
    long_description=open('README.txt').read(),
    install_requires=[]
)
