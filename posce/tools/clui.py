'''
Command-line user interface functions.
'''

import click

DYM_LIMIT = 5

class CustomGroup(click.Group):
    '''
    A custom Click Group that disambiguates Command names.
    '''

    def get_command(self, ctx, name):
        '''
        Return a Command matching an unambiguous name.
        '''

        comms = [
            comm for comm in self.list_commands(ctx)
            if comm.startswith(name)
        ]

        if len(comms) == 0:
            return None
        elif len(comms) == 1:
            return click.Group.get_command(self, ctx, comms[0])
        else:
            clist = ', '.join(map(repr, comms))
            ctx.fail(f'Ambiguous command. Did you mean: {clist}?')


def disambiguate(book, name):
    '''
    Return a Note matching an unambiguous name, or raise an error if
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
        error(f'Ambiguous note name. Did you mean: {nlist}?')

    else:
        error(f'Ambiguous note name, {len(notes)} notes match.')

def error(string):
    '''
    Raise a ClickException with an error string.
    '''

    raise click.ClickException(string)
