'''
Tests for 'posce.comms.drop'.
'''

from posce.comms.drop           import drop
from tests.test_items.test_book import book
from tests.tools                import out

def test_copy(book):
    # success: defaults
    assert out(book, drop, 'alpha') == []
    assert not book['alpha'].exists()
