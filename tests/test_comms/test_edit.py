'''
Tests for 'posce.comms.edit'.
'''

import click

from posce.comms.edit           import edit
from tests.test_items.test_book import book
from tests.tools                import out

def test_edit(monkeypatch, book):
    # setup
    editargs = {}
    monkeypatch.setattr(click, 'edit', lambda **k: editargs.update(k))
    book.create('bravo2', '')

    # success - existing note
    assert out(book, edit, 'alpha') == []
    assert editargs == {
        'editor':    None,
        'extension': '.txt',
        'filename':  book['alpha'].path,
    }

    # success - existing note, custom editor
    assert out(book, edit, 'alpha', '-e', 'test') == []
    assert editargs == {
        'editor':    'test',
        'extension': '.txt',
        'filename':  book['alpha'].path,
    }

    # success - new note with --new
    assert out(book, edit, 'new1', '-n') == []
    assert editargs == {
        'editor':    None,
        'extension': '.txt',
        'filename':  book['new1'].path,
    }

    # failure - new note without --new
    assert out(book, edit, 'new2') == [
        "Error: Note 'new2' does not exist.\n",
    ]

    # failure - ambiguous
    assert out(book, edit, 'bravo') == [
        "Error: Ambiguous name. Did you mean: 'bravo', 'bravo2'?\n",
    ]
