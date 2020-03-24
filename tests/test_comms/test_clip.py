'''
Tests for 'posce.comms.clip'.
'''

import pyperclip

from posce.comms.clip           import clip
from tests.test_items.test_book import book
from tests.tools                import out

def test_clip(book):
    # setup (to preserve pre-test clipboard)
    pre = pyperclip.paste()

    # success: defaults
    assert out(book, clip, 'alpha') == []
    assert pyperclip.paste() == 'alpha'

    # teardown
    pyperclip.copy(pre)
