'''
Click command function 'dump'.
'''

import zipfile
import zlib

import click

from posce.comms.base import group

@group.command(short_help='Archive notes.')
@click.argument('file')
@click.option('-l', '--level',
    help    = 'Compression level (0-9).',
    default = 5,
    metavar = 'INT',
    type    = click.IntRange(0, 9),
)
@click.pass_obj
def dump(book, file, level):
    '''
    Create notes archive at FILE.
    '''

    opts = {
        'compression':   zipfile.ZIP_DEFLATED,
        'compresslevel': level,
    }

    with zipfile.ZipFile(file, 'w', **opts) as zipf:
        for note in book:
            zipf.write(note.path, note.base)
