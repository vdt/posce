'''
Click command function 'edit'.
'''

import click

from posce.comms.base import group
from posce            import tools

@group.command()
@click.argument('name')
@click.option('-e', '--editor',
    help    = 'Editor program to open in.',
    metavar = 'PROG',
    type    = str,
)
@click.pass_obj
def edit(book, name, editor):
    '''
    Edit a note.
    '''

    note = tools.clui.disambiguate(book, name)
    func = lambda note: click.edit(
        editor    = editor or None,
        extension = f'.{note.ext}',
        filename  = note.path,
    )

    if data := func(note):
        note.write(data)
