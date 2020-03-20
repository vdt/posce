'''
Class definition for 'Note'.
'''

import fnmatch
import re

from posce import tools

class Note:
    '''
    A single plaintext note file.
    '''

    __slots__ = ['ext', 'name', 'path']

    def __init__(self, path):
        '''
        Initialise a new Note.
        '''

        self.path = str(path)
        self.ext  = tools.path.ext(self.path)
        self.name = tools.path.name(self.path)

    def __contains__(self, string):
        '''
        Return True if the Note contains a string.
        '''

        return string in self.read()

    def __eq__(self, note):
        '''
        Return True if the Note is equal to another Note.
        '''

        return all([
            isinstance(note, Note),
            self.path == getattr(note, 'path', None),
        ])

    def __hash__(self):
        '''
        Return the Note's unique hash code.
        '''

        return hash(self.path)

    def __iter__(self):
        '''
        Yield the Note's contents as lines.
        '''

        yield from self.read().splitlines(keepends=True)

    def __len__(self):
        '''
        Return the length of the Note's contents.
        '''

        return len(self.read())

    def __repr__(self):
        '''
        Return the Note as a code-representative string.
        '''

        return f'Note({self.path!r})'

    def append(self, string, *, sep='\n'):
        '''
        Append a string to the Note's contents.
        '''

        tools.file.append(self.path, string, sep=sep)

    def copy(self, name):
        '''
        Copy the Note to another name in the same directory.
        '''

        tools.file.copy(self.path, name)

    def exists(self):
        '''
        Return True if the Note's path exists.
        '''

        return tools.file.exists(self.path)

    def match(self, pattern):
        '''
        Return True if the Note's name matches a glob pattern.
        '''

        return fnmatch.fnmatch(self.name, pattern)

    def read(self):
        '''
        Return the contents of the Note as a string.
        '''

        return tools.file.read(self.path)

    def reext(self, ext):
        '''
        Move the Note to a different extension in the same directory.
        '''

        tools.file.reext(self.path, ext)

    def rename(self, name):
        '''
        Move the Note to a different name in the same directory.
        '''

        tools.file.rename(self.path, name)

    def search(self, pattern):
        '''
        Return True if the Note's contents matches a regular expression.
        '''

        return re.search(pattern, self.read())

    def write(self, string):
        '''
        Overwrite the Note's contents with a string.
        '''

        tools.file.write(self.path, string)
