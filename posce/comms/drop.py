'''
Click command function 'drop'.
'''

import click
import send2trash

from posce.comms.base import group
from posce            import tools

@group.command(short_help='Trash note.')
@click.argument('name')
@click.pass_obj
def drop(book, name):
    '''
    Move note NAME to trash.
    '''

    note = tools.clui.disambiguate(book, name)
    send2trash.send2trash(note.path)
