'''
Click command function 'edit'.
'''

import click

from posce.comms.base import group
from posce            import tools

@group.command()
@click.argument('name')
@click.option('-e', '--editor',
    help    = 'Editor to open in.',
    default = '',
    type    = str,
)
@click.option('-n', '--new',
    help    = 'Create new note.',
    is_flag = True,
)
@click.pass_obj
def edit(book, name, editor, new):
    '''
    Edit a note.
    '''

    notes = list(book.disambiguate(name))
    efunc = lambda note: click.edit(
        editor    = editor or None,
        extension = f'.{note.ext}',
        filename  = note.path,
    )

    if len(notes) == 0:
        if new:
            note = book.create(name, '')
            if data := efunc(note):
                note.write(data)
        else:
            tools.clui.error(f'Note {name!r} does not exist.')

    elif len(notes) == 1:
        if data := efunc(notes[0]):
            notes[0].write(data)

    else:
        tools.clui.disambiguate(book, name)
