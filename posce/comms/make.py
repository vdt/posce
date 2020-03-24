'''
Click command function 'make'.
'''

import click

from posce.comms.base import group
from posce            import tools

@group.command(short_help='Create note.')
@click.argument('name')
@click.option('-f', '--file',
    help    = 'Copy note from FILE.',
    default = '',
    metavar = 'FILE',
)
@click.pass_obj
def make(book, name, file):
    '''
    Create new note NAME.
    '''

    if name in book:
        tools.clui.error(f'Note {name!r} already exists.')
    else:
        if file:
            try:
                path = tools.path.clean(file)
                data = tools.file.read(path)
                book.create(name, data)
            except Exception:
                tools.clui.error(f'Cannot read file {file!r}.')
        else:
            book.create(name, '')
