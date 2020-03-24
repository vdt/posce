'''
Click command function 'list'.
'''

import click

from posce.comms.base import group

@group.command(short_help='List notes.')
@click.argument('glob',
    default = '*',
)
@click.option('-r', '--reverse',
    help    = 'Reverse sort order.',
    is_flag = True,
)
@click.option('-s', '--sort',
    help    = 'Sort notes by attribute.',
    default = 'name',
    type    = click.Choice(['name', 'size']),
)
@click.pass_obj
def list(book, glob, sort, reverse):
    '''
    List all notes matching GLOB (default "*").
    '''

    key = {
        'name': lambda note: note.name,
        'size': lambda note: len(note),
    }[sort]

    for note in sorted(book.match(glob), key=key, reverse=reverse):
        click.echo(note.name)
