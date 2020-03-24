'''
Click command function 'repl'.
'''

import code

import click

from posce            import VERSION_STRING
from posce.comms.base import group

@group.command(hidden=True, short_help='Open REPL.')
@click.pass_obj
def repl(book):
    '''
    Open a debug REPL.
    '''

    args = {'book': book, 'group': group}
    code.interact(banner=VERSION_STRING, local=args, exitmsg='')
