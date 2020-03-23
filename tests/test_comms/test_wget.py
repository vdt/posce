'''
Tests for 'posce.comms.wget'.
'''

import random

from posce.comms.wget           import wget
from tests.test_items.test_book import book
from tests.tools                import out

def test_wget(book):
    # success
    assert out(book, wget, 'alpha', 'example.com') == []
    assert '<title>Example Domain</title>' in book['alpha'].read()

    # failure - invalid address
    assert out(book, wget, 'alpha', 'nope.nope') == [
        "Error: Could not find 'http://nope.nope'.\n",
    ]

    # failure - nonexistent address
    num = random.randrange(1000000,2000000)
    assert out(book, wget, 'alpha', f'nope{num}.com') == [
        f"Error: Could not find 'http://nope{num}.com'.\n",
    ]
