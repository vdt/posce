'''
File I/O and discovery functions.
'''

import glob
import os

OPTIONS = {
    'encoding': 'utf-8',
}

def append(path, string, *, sep='\n'):
    '''
    Append a string to a file.
    '''

    with open(path, 'a', **OPTIONS) as file:
        file.write(sep + string)

def create(path, string):
    '''
    Write a string to a new file.
    '''

    with open(path, 'x', **OPTIONS) as file:
        file.write(string)

def exists(path):
    '''
    Return true if a file (not a directory) exists.
    '''

    return os.path.isfile(path)

def find(dire, term):
    '''
    Yield all files in a directory with names matching a glob pattern.
    '''

    pattern = os.path.normpath(os.path.join(dire, term))
    yield from glob.iglob(pattern)

def read(path):
    '''
    Return the contents of a file as a string.
    '''

    with open(path, 'r', **OPTIONS) as file:
        return file.read()

def write(path, string):
    '''
    Write a string to a file.
    '''

    with open(path, 'w', **OPTIONS) as file:
        file.write(string)
