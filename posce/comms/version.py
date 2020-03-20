'''
Click command function 'version'.
'''

import click

from posce            import VERSION_STRING
from posce.comms.base import group

@group.command()
def version():
    '''
    Show the current version.
    '''

    click.echo(VERSION_STRING)
