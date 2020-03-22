'''
Click command function 'move'.
'''

import click

from posce            import tools
from posce.comms.base import group

@group.command()
@click.argument('name')
@click.argument('dest')
@click.pass_obj
def move(book, name, dest):
    '''
    Move a note.
    '''

    note = tools.clui.disambiguate(book, name)

    if dest in book:
        tools.clui.error(f'Note {dest!r} already exists.')
    else:
        note.rename(dest)
