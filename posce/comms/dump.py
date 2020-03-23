'''
Click command function 'dump'.
'''

import time
import zipfile
import zlib

import click

from posce.comms.base import group
from posce            import tools

@group.command()
@click.argument('dest')
@click.option('-l', '--level',
    help    = 'Compression level (0-9).',
    default = 5,
    metavar = 'LEVEL',
    type    = click.IntRange(0, 9),
)
@click.pass_obj
def dump(book, dest, level):
    '''
    Create note archive.
    '''

    opts = {
        'compression':   zipfile.ZIP_DEFLATED,
        'compresslevel': level,
    }

    with zipfile.ZipFile(dest, 'w', **opts) as zipf:
        for note in book:
            zipf.write(note.path, note.base)
