'''
Click command function 'edit'.
'''

import click

from posce.comms.base import group
from posce            import tools

@group.command(short_help='Edit note.')
@click.argument('name')
@click.option('-e', '--editor',
    help    = 'Editor program to use.',
    metavar = 'PROG',
    type    = str,
)
@click.pass_obj
def edit(book, name, editor):
    '''
    Open note NAME in editor.
    '''

    note = tools.clui.disambiguate(book, name)
    func = lambda note: click.edit(
        editor    = editor or None,
        extension = f'.{note.ext}',
        filename  = note.path,
    )

    if data := func(note):
        note.write(data)
