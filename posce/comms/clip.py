'''
Click command function 'clip'.
'''

import click
import pyperclip

from posce.comms.base import group
from posce            import tools

@group.command()
@click.argument('name')
@click.pass_obj
def clip(book, name):
    '''
    Copy a note to clipboard.
    '''

    note = tools.clui.disambiguate(book, name)
    pyperclip.copy(note.read())
