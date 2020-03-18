'''
Tests for 'posce.items.note'.
'''

import pytest

from posce.items.note import Note

@pytest.fixture
def note(tmpdir):
    path = tmpdir.join('foo.txt')
    path.write('foo\nbar')
    return Note(path)

def test_init(note):
    # success
    assert note.path.endswith('foo.txt')
    assert note.ext  == 'txt'
    assert note.name == 'foo'

def test_contains(note):
    # success
    assert 'foo'      in note
    assert 'nope' not in note

def test_eq(note):
    # success
    assert note == note
    assert note != Note('/nope.txt')
    assert note != 'not a note'

def test_hash(note):
    # success
    assert {note, note} == {note}

def test_iter(note):
    # success
    assert list(note) == ['foo\n', 'bar']

def test_len(note):
    # success
    assert len(note) == 7

def test_repr(note):
    # setup
    note.path = '/dir/foo.txt'

    # success
    assert repr(note) == "Note('/dir/foo.txt')"

def test_append(note):
    # success
    note.append('baz', sep='\n')
    assert open(note.path).read() == 'foo\nbar\nbaz'

def test_exists(note):
    # success
    assert     note.exists()
    assert not Note('/nope.txt').exists()

def test_match(note):
    # success
    assert     note.match('fo?')
    assert not note.match('n*pe')

def test_read(note):
    # success
    assert note.read() == 'foo\nbar'

def test_search(note):
    # success
    assert     note.search(r'(\w+)')
    assert not note.search(r'(nope)')

def test_write(note):
    # success
    note.write('test')
    assert open(note.path).read() == 'test'
