'''
File I/O and discovery functions.
'''

import glob
import os
import shutil

OPTIONS = {
    'encoding': 'utf-8',
}

def append(path, string, *, sep='\n'):
    '''
    Append a string to a file.
    '''

    with open(path, 'a', **OPTIONS) as file:
        file.write(sep + string)

def copy(path, name):
    '''
    Copy a file to another name in the same directory.
    '''

    dire = os.path.dirname(path)
    ext  = os.path.splitext(path)[-1]
    dest = os.path.join(dire, name + ext)
    shutil.copyfile(path, dest)

def create(path, string):
    '''
    Write a string to a new file.
    '''

    with open(path, 'x', **OPTIONS) as file:
        file.write(string)

def exists(path):
    '''
    Return true if a file or directory exists.
    '''

    return os.path.exists(path)

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

def reext(path, ext):
    '''
    Move a file to a different extension in the same directory.
    '''

    dire = os.path.dirname(path)
    name = os.path.splitext(os.path.basename(path))[0]
    dest = os.path.join(dire, f'{name}.{ext}')
    shutil.move(path, dest)

def rename(path, name):
    '''
    Move a file to a different name in the same directory.
    '''

    dire = os.path.dirname(path)
    ext  = os.path.splitext(path)[-1].lstrip('.')
    dest = os.path.join(dire, f'{name}.{ext}')
    shutil.move(path, dest)

def write(path, string):
    '''
    Write a string to a file.
    '''

    with open(path, 'w', **OPTIONS) as file:
        file.write(string)
