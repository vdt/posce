'''
Filepath string manipulation functions.
'''

import os.path

EXPANSIONS = {
    '%': os.path.expandvars,
    '~': os.path.expanduser,
    '$': os.path.expandvars,
}

def base(path):
    '''
    Return a path's basename with the extension.
    '''

    return os.path.basename(path)

def clean(path):
    '''
    Return a normalised path.
    '''

    return os.path.normpath(path)

def expand(path):
    '''
    Return a clean variable-expanded path.
    '''

    for char, func in EXPANSIONS.items():
        if char in path:
            path = func(path)
    return path

def ext(path):
    '''
    Return a path's extension without a dot.
    '''

    part = os.path.splitext(path)
    return part[-1].lstrip('.')

def join(*elems):
    '''
    Return a clean joined filepath.
    '''

    return os.path.normpath(os.path.join(*elems))

def name(path):
    '''
    Return a path's basename without the extension.
    '''

    base = os.path.basename(path)
    return os.path.splitext(base)[0]
