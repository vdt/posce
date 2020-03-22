'''
Tests for 'posce.comms.repl'.
'''

import code

from posce                      import VERSION_STRING
from posce.comms.base           import group
from posce.comms.repl           import repl
from tests.test_items.test_book import book
from tests.tools                import out

def test_repl(monkeypatch, book):
    # setup
    codeargs = {}
    monkeypatch.setattr(code, 'interact', lambda **k: codeargs.update(k))

    # success
    assert out(book, repl) == []
    assert codeargs == {
        'banner':  VERSION_STRING,
        'local':   {'book': book, 'group': group},
        'exitmsg': '',
    }
