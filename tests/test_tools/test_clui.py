'''
Tests for 'posce.tools.clui'.
'''

import click
import pytest

from posce.tools      import clui
from posce.items.book import Book
from posce.items.note import Note

def test_CustomGroup():
    # setup
    @click.group(cls=clui.CustomGroup)
    def group(): pass

    @group.command()
    def alpha(): pass

    @group.command()
    def bravo(): pass

    @group.command()
    def bravo2(): pass

    ctx = click.Context(group)

    # success - one match
    assert group.get_command(ctx, 'a')     == alpha
    assert group.get_command(ctx, 'alpha') == alpha

    # success - zero matches
    assert group.get_command(ctx, 'nope') == None

    # failure - multiple matches
    with pytest.raises(click.UsageError) as exc:
        group.get_command(ctx, 'bravo')
    exc.match("Ambiguous command. Did you mean: 'bravo', 'bravo2'?")

def test_disambiguate():
    # setup
    book = Book('/test', 'txt')

    for name in ['alpha', 'bravo1', 'bravo2']:
        book.notes[name] = Note(name)

    for n in range(clui.DYM_LIMIT+1):
        book.notes[f'charlie{n}'] = Note(f'charlie{n}')

    # success - one match
    assert clui.disambiguate(book, 'al') == book['alpha']

    # failure - zero matches
    with pytest.raises(click.ClickException) as exc:
        clui.disambiguate(book, 'nope')
    exc.match("Note 'nope' does not exist.")

    # failure - multiple notes, less than DYM_LIMIT
    with pytest.raises(click.ClickException) as exc:
        clui.disambiguate(book, 'bravo')
    exc.match("Ambiguous note name. Did you mean: 'bravo1', 'bravo2?'")

    # failure - multiple notes, more than DYM_LIMIT
    with pytest.raises(click.ClickException) as exc:
        clui.disambiguate(book, 'charlie')
    exc.match(f"Ambiguous note name, {clui.DYM_LIMIT+1} notes match.")

def test_error():
    # success
    with pytest.raises(click.ClickException) as exc:
        clui.error('test')
    assert exc.exconly() == 'click.exceptions.ClickException: test'
