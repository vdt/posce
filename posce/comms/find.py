'''
Click command function 'find'.
'''

import re

import click

from posce.comms.base import group

@group.command(short_help='Search notes.')
@click.argument('term')
@click.option('-r', '--regex',
    help    = 'Use term as regular expression.',
    is_flag = True,
)
@click.pass_obj
def find(book, term, regex):
    '''
    List all notes matching TERM.
    '''

    term = term if regex else re.escape(term)
    for note in book.search(term):
        click.echo(note.name)
