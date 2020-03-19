'''
Click command function 'find'.
'''

import re

import click

from posce.comms.base import group

@group.command()
@click.argument('term')
@click.option('-r', '--regex',
    help    = 'Use regular expressions.',
    is_flag = True,
)
@click.pass_obj
def find(book, term, regex):
    '''
    Search all notes.
    '''

    term = term if regex else re.escape(term)
    for note in book.search(term):
        click.echo(note.name)
