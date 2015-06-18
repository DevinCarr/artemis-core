"""A setuptools based setup module for artemis-core"""
import sys

if sys.version < '3.4':
    print('Sorry, this is not a compatible version of Python. Use 3.4 or later.')
    exit(1)

from setuptools import setup, find_packages
from artemis import VERSION

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='artemis-core',
    version=VERSION,
    description='A simple inline configurable shell bot in python.',
    long_description=long_description,
    url='https://github.com/DevinCarr/artemis-core',
    author='Devin Carr',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='shell commands build tool',
    packages=find_packages(),
    install_requires=[],
    extras_require={
        'dev': [],
        'test': [],
    },
    entry_points={
        'console_scripts': [
            'arty=artemis:main',
        ],
    },
)
