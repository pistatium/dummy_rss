# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='dummy_rss',
    version='0.0.1',
    packages=find_packages('src'),
    install_requires=[
        'flask',
        'pytz',
    ],
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'dummy_rss=app.main:main'
        ]
    },
)
