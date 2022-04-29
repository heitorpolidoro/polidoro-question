"""
Setup to create the package
"""
import polidoro_question
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='polidoro-question',
    version=polidoro_question.VERSION,
    description='Polidoro Question.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/heitorpolidoro/polidoro-question',
    author='Heitor Polidoro',
    license='unlicense',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    install_requires=['polidoro_terminal<=1.0',
                      'python_dateutil==2.8.2'],
    include_package_data=True
)
