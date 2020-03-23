'''
Tests for 'posce.comms.dump'.
'''

import os.path
import zipfile

from posce.comms.dump           import dump
from tests.test_items.test_book import book
from tests.tools                import out

def test_dump(book, tmpdir):
    # setup
    dest = tmpdir.join('test.zip')

    # success: defaults
    assert out(book, dump, str(dest)) == []
    with zipfile.ZipFile(dest, 'r') as zipf:
        assert zipf.namelist() == ['alpha.txt', 'bravo.txt', 'charlie.txt']
        assert zipf.open('alpha.txt').read()   == b'alpha'
        assert zipf.open('bravo.txt').read()   == b'bravobravo'
        assert zipf.open('charlie.txt').read() == b'charliecharliecharlie'

    # success: --level 0
    assert out(book, dump, str(dest), '-l', '0') == []
    with zipfile.ZipFile(dest, 'r') as zipf:
        assert os.stat(dest).st_size == 359
