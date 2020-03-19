'''
Command-line user interface functions.
'''

import click

DYM_LIMIT = 5

def disambiguate(book, name):
    '''
    Return a Note matching an abbreviated name, or raise an error if
    there are zero or multiple matching Notes.
    '''

    notes = list(book.disambiguate(name))

    if len(notes) == 0:
        error(f'Note {name!r} does not exist.')

    elif len(notes) == 1:
        return notes[0]

    elif len(notes) <= DYM_LIMIT:
        names = sorted(note.name for note in notes)
        nlist = ', '.join(map(repr, names))
        error(f'Ambiguous name. Did you mean: {nlist}?')

    else:
        error(f'Ambiguous name, {len(notes)} notes match.')

def error(string):
    '''
    Raise a ClickException with an error string.
    '''

    raise click.ClickException(string)
