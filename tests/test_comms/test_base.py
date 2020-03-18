'''
Tests for 'posce.comms.base'.
'''

import click

from posce.comms.base           import group
from tests.test_items.test_book import book
from tests.tools                import out

@group.command()
@click.argument('arg')
@click.pass_obj
def mock(book, arg):
    click.echo(book.dire)
    click.echo(arg)

def test_group(book):
    # success
    assert out(book, mock, 'test') == [f'{book.dire}\n', 'test\n']
