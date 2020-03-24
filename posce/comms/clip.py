'''
Click command function 'clip'.
'''

import click
import pyperclip

from posce.comms.base import group
from posce            import tools

@group.command(short_help='Clipboard note.')
@click.argument('name')
@click.pass_obj
def clip(book, name):
    '''
    Copy note NAME to clipboard.
    '''

    note = tools.clui.disambiguate(book, name)
    pyperclip.copy(note.read())
