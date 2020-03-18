'''
Tests for 'posce.tools.path'.
'''

import os

from posce.tools import path

def s(path):
    return path.replace('/', os.sep)

def test_base():
    # success
    assert path.base('/dire/file.txt') == 'file.txt'

def test_clean():
    # success
    assert path.clean('/././file.txt') == s('/file.txt')

def test_expand():
    # setup
    os.environ.update({'HOME': '/home', 'TEST': 'test'})

    # success
    assert path.expand('$HOME/$TEST/file.txt') == '/home/test/file.txt'

def test_ext():
    # success
    assert path.ext('/dire/file.txt') == 'txt'

def test_join():
    # success
    assert path.join('alpha', 'bravo', 'file.txt') == s('alpha/bravo/file.txt')

def test_name():
    # success
    assert path.name('/dire/file.txt') == 'file'
