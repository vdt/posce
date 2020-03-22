'''
Tests for 'posce.comms.move'.
'''

import os.path

from posce.comms.move           import move
from tests.test_items.test_book import book
from tests.tools                import out

def test_move(book):
    # setup
    dest = book['alpha'].path.replace('alpha', 'dest')

    # success - defaults
    assert out(book, move, 'alpha', 'dest') == []
    assert     os.path.exists(dest)
    assert not os.path.exists(book['alpha'].path)

    # failure - dest exists
    assert out(book, move, 'bravo', 'charlie') == [
        "Error: Note 'charlie' already exists.\n",
    ]
