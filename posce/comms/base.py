'''
Click base group function.
'''

import click

from posce            import VERSION_STRING
from posce.items      import Book
from posce.tools.clui import CustomGroup

SETTINGS = {
    'help_option_names': ['-h', '--help'],
}

def version(ctx, param, value):
    '''
    Print the current version.
    '''

    if value:
        click.echo(VERSION_STRING)
        ctx.exit()

@click.group(cls=CustomGroup, context_settings=SETTINGS)
@click.option('--dir', envvar='POSCE_DIR', hidden=True)
@click.option('--ext', envvar='POSCE_EXT', hidden=True)
@click.option('-v', '--version',
    help         = 'Show current version and exit.',
    callback     = version,
    expose_value = False,
    is_eager     = True,
    is_flag      = True,
)
@click.pass_context
def group(ctx, dir, ext):
    '''
    Posce: a note-taking toolkit for your command line.
    See github.com/posce/posce for help and issues.
    '''

    ctx.obj = Book(dir, ext.lstrip('.'))
