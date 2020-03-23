'''
Tests for 'posce.comms.show'.
'''

from posce.comms.show           import show
from tests.test_items.test_book import book
from tests.tools                import out

def test_show(book):
    # setup
    book['bravo'].write('test ' * 25)

    # success: defaults
    assert out(book, show, 'alpha') == [
        'alpha\n',
    ]

    # success: --wrap 40
    assert out(book, show, 'bravo', '-w', 40) == [
        'test test test test test test test test\n',
        'test test test test test test test test\n',
        'test test test test test test test test\n',
        'test\n',
    ]
