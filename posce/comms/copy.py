'''
Click command function 'copy'.
'''

import click

from posce.comms.base import group
from posce            import tools

@group.command()
@click.argument('name')
@click.argument('dest')
@click.pass_obj
def copy(book, name, dest):
    '''
    Copy a note.
    '''

    note = tools.clui.disambiguate(book, name)
    note.copy(dest)
