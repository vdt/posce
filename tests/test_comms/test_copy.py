'''
Tests for 'posce.comms.copy'.
'''

import os.path

from posce.comms.copy           import copy
from tests.test_items.test_book import book
from tests.tools                import out

def test_copy(book):
    # setup
    dest = book['alpha'].path.replace('alpha', 'dest')

    # success - defaults
    assert out(book, copy, 'alpha', 'dest') == []
    assert os.path.exists(dest)
    assert os.path.exists(book['alpha'].path)
