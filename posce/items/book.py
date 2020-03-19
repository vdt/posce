'''
Class definition for 'Book'.
'''

import click

from posce.items.note import Note
from posce            import tools

class Book:
    '''
    A directory of plaintext note files.
    '''

    __slots__ = ['dire', 'ext', 'notes']

    def __init__(self, dire, ext):
        '''
        Initialise a new Book.
        '''

        self.dire  = tools.path.expand(str(dire))
        self.ext   = str(ext)
        self.notes = {
            note.name: note for note in
            map(Note, tools.file.find(self.dire, f'*.{self.ext}'))
        }

    def __contains__(self, name):
        '''
        Return True if the Book contains a Note name.
        '''

        return name in self.notes.keys()

    def __eq__(self, book):
        '''
        Return True if the Book is equal to another Book.
        '''

        return all([
            isinstance(book, Book),
            self.dire == getattr(book, 'dire', None),
            self.ext  == getattr(book, 'ext',  None),
        ])

    def __getitem__(self, name):
        '''
        Return a Note in the Book by name.
        '''

        return self.notes[name]

    def __hash__(self):
        '''
        Return the Book's unique hash code.
        '''

        return hash(self.dire + self.ext)

    def __iter__(self):
        '''
        Yield each Note in the Book.
        '''

        yield from self.notes.values()

    def __len__(self):
        '''
        Return the number of Notes in the Book.
        '''

        return len(self.notes)

    def __repr__(self):
        '''
        Return the Book as a code-representative string.
        '''

        return f'Book({self.dire!r}, {self.ext!r})'

    def create(self, name, string):
        '''
        Create and return a new Note in the Book.
        '''

        dest = tools.path.join(self.dire, f'{name}.{self.ext}')
        tools.file.create(dest, string)
        self.notes[name] = Note(dest)
        return self.notes[name]

    def disambiguate(self, name):
        '''
        Yield each Note matching an unambiguous name.
        '''

        key = lambda note: note.name.startswith(name)
        yield from self.filter(key)

    def exists(self):
        '''
        Return True if the Book's directory exists.
        '''

        return tools.file.exists(self.dire)

    def filter(self, func):
        '''
        Yield each Note in the Book passing a filter function.
        '''

        for note in self.notes.values():
            if func(note):
                yield note

    def match(self, pattern):
        '''
        Yield each Note with a name matching a glob pattern.
        '''

        yield from self.filter(lambda note: note.match(pattern))

    def search(self, pattern):
        '''
        Yield each Note with contents matching a regular expression.
        '''

        yield from self.filter(lambda note: note.search(pattern))
