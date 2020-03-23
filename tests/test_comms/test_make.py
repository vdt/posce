'''
Tests for 'posce.comms.make'.
'''

import os.path

from posce.comms.make           import make
from tests.test_items.test_book import book
from tests.tools                import out

def test_make(book, tmpdir):
    # setup
    file = tmpdir.join('test.txt')
    file.write('test')

    # success: default
    assert out(book, make, 'make') == []
    assert 'make' in book
    assert book['make'].path.endswith('make.txt')
    assert book['make'].read() == ''

    # success: --file FILE
    assert out(book, make, 'make2', '-f', str(file)) == []
    assert book['make2'].read() == 'test'

    # failure: note already exists
    assert out(book, make, 'alpha') == [
        "Error: Note 'alpha' already exists.\n",
    ]

    # failure: cannot read file
    assert out(book, make, 'make3', '-f', 'nope.txt') == [
        "Error: Cannot read file 'nope.txt'.\n",
    ]
