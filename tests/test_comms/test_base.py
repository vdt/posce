'''
Tests for 'posce.comms.base'.
'''

import click

from posce                      import VERSION_STRING
from posce.comms.base           import group, version
from tests.test_items.test_book import book
from tests.tools                import out

@group.command()
@click.argument('arg')
@click.option('-v', '--version',
    callback     = version,
    expose_value = False,
    is_eager     = True,
    is_flag      = True,
)
@click.pass_obj
def mock(book, arg):
    click.echo(book.dire)
    click.echo(arg)

def test_group(book):
    # success
    assert out(book, mock, 'test') == [f'{book.dire}\n', 'test\n']

    # success - version callback
    assert out(book, mock, '-v') == [f'{VERSION_STRING}\n']
