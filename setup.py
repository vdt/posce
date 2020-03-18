'''
PyPi setup script.
'''

from setuptools import find_packages, setup

from posce import VERSION_NUMBER

setup(
    # Basic information.
    name         = 'posce',
    version      = VERSION_NUMBER,
    keywords     = 'cli notes note-taking',
    description  = 'A note-taking toolkit for your command line.',
    author       = 'Stephen Malone',
    author_email = 'mail@posce.org',

    # Project description.
    long_description = open('readme.md').read(),
    long_description_content_type = 'text/markdown',

    # Package specifications.
    packages         = find_packages(exclude=['*tests*']),
    python_requires  = '>=3.8.0',
    install_requires = ['click>=7.1.1'],

    # Console executables.
    entry_points = {
        'console_scripts': ['posce=posce.__main__:main'],
    },

    # Project URLs.
    project_urls = {
        'Homepage': 'https://github.com/posce/posce',
        'Issues':   'https://github.com/posce/posce/issues',
    },

    # Project classifiers.
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Topic :: Office/Business :: News/Diary',
        'Topic :: Office/Business',
    ],
)
