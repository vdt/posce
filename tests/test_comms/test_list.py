'''
Tests for 'posce.comms.list'.
'''

from posce.comms.list           import list
from tests.test_items.test_book import book
from tests.tools                import out

def test_list(book):
    # success: defaults
    assert out(book, list) == [
        'alpha\n',
        'bravo\n',
        'charlie\n',
    ]

    # success: GLOB
    assert out(book, list, 'a*') == [
        'alpha\n',
    ]

    # success: --reverse --sort size
    assert out(book, list, '-r', '-s', 'size') == [
        'charlie\n',
        'bravo\n',
        'alpha\n',
    ]
