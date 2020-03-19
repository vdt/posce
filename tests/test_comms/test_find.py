'''
Tests for 'posce.comms.find'.
'''

from posce.comms.find           import find
from tests.test_items.test_book import book
from tests.tools                import out

def test_find(book):
    # success - defaults
    assert out(book, find, 'alpha') == [
        'alpha\n',
    ]

    # success - regular expressions
    assert out(book, find, r'a\w{3}a', '-r') == [
        'alpha\n',
    ]
