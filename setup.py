from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='draph',
    version='0.0.1',
    description='Python dependency graph builder',
    long_description=long_description,
    url='https://github.com/akoskaaa/draph',
    author='Akos Hochrein',
    author_email='hoch.akos@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'argparse',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'draph=src:run',
        ],
    },
)
