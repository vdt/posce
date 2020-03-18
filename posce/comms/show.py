'''
Click command function 'show'.
'''

import click

from posce.comms.base import group

@group.command()
@click.argument('name')
@click.pass_obj
def show(book, name):
    '''
    Print a note.
    '''

    note = clui.disambiguate(book, name)
    click.echo(note.read())
