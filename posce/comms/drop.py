'''
Click command function 'drop'.
'''

import click
import send2trash

from posce.comms.base import group
from posce            import tools

@group.command()
@click.argument('name')
@click.pass_obj
def drop(book, name):
    '''
    Move a note to trash.
    '''

    note = tools.clui.disambiguate(book, name)
    send2trash.send2trash(note.path)
