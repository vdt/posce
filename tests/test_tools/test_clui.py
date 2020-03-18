'''
Tests for 'posce.tools.clui'.
'''

import click
import pytest

from posce.tools                import clui
from tests.test_items.test_book import book

def test_disambiguate(book):
    # setup
    book.notes['bravo2'] = book['bravo']
    for n in range(clui.DYM_LIMIT):
        book.notes[f'charlie{n}'] = book['charlie']

    # success - one match
    assert clui.disambiguate(book, 'al') == book['alpha']

    # failure - zero matches
    with pytest.raises(click.ClickException) as exc:
        clui.disambiguate(book, 'nope')
    exc.match("Note 'nope' does not exist.")

    # failure - multiple notes, less than DYM_LIMIT
    with pytest.raises(click.ClickException) as exc:
        clui.disambiguate(book, 'bravo')
    exc.match("Ambiguous name. Did you mean: 'bravo', 'bravo2?'")

    # failure - multiple notes, more than DYM_LIMIT
    with pytest.raises(click.ClickException) as exc:
        clui.disambiguate(book, 'charlie')
    exc.match(f"Ambiguous name, {clui.DYM_LIMIT+1} notes match.")

def test_error():
    # success
    with pytest.raises(click.ClickException) as exc:
        clui.error('test')
    assert exc.exconly() == 'click.exceptions.ClickException: test'
