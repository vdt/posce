'''
Command-line user interface functions.
'''

import click

def error(string):
    '''
    Raise a ClickException with an error string.
    '''

    raise click.ClickException(string)
