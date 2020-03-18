'''
Tests for 'posce.tools.path'.
'''

import os

from posce.tools import path

def s(path):
    return path.replace('/', os.sep)

def test_base():
    # success
    assert path.base('/dir/file.ext') == 'file.ext'

def test_clean():
    # success
    assert path.clean('/././file.ext') == s('/file.ext')

def test_expand():
    # setup
    os.environ.update({'HOME': '/home', 'TEST': 'test'})

    # success
    assert path.expand('$HOME/$TEST/file.ext') == '/home/test/file.ext'

def test_ext():
    # success
    assert path.ext('/dir/file.ext') == 'ext'

def test_join():
    # success
    assert path.join('one', 'two', 'file.ext') == s('one/two/file.ext')

def test_name():
    # success
    assert path.name('/dir/file.ext') == 'file'
