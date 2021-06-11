"""Script for wheel generation."""
from setuptools import setup, find_packages

setup(
    name='heuro_wheel',
    version='1.0',
    packages=find_packages(),
    package_data={'src': ['heuro/po/ru/LC_MESSAGES/heuro.mo',
                          'heuro/po/en/LC_MESSAGES/heuro.mo', ]},
)
