'''
Click command function 'show'.
'''

import textwrap

import click

from posce.comms.base import group
from posce            import tools

@group.command()
@click.argument('name')
@click.option('-w', '--wrap',
    help    = 'Wrap text to width.',
    default = 0,
    type    = int,
)
@click.pass_obj
def show(book, name, wrap):
    '''
    Print a note.
    '''

    note = tools.clui.disambiguate(book, name)
    if wrap:
        for line in textwrap.wrap(note.read(), width=wrap, tabsize=4):
            click.echo(line)
    else:
        click.echo(note.read())
