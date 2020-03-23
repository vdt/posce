'''
Tests for 'posce.items.note'.
'''

import os.path

import pytest

from posce.items.note import Note

@pytest.fixture
def note(tmpdir):
    path = tmpdir.join('alpha.txt')
    path.write('alpha\nbravo')
    return Note(path)

def test_init(note):
    # success
    assert note.path.endswith('alpha.txt')
    assert note.base == 'alpha.txt'
    assert note.ext  == 'txt'
    assert note.name == 'alpha'

def test_contains(note):
    # success
    assert 'alpha'    in note
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
    assert list(note) == ['alpha\n', 'bravo']

def test_len(note):
    # success
    assert len(note) == 11

def test_repr(note):
    # setup
    note.path = '/dire/alpha.txt'

    # success
    assert repr(note) == "Note('/dire/alpha.txt')"

def test_append(note):
    # success
    note.append('charlie', sep='\n')
    assert open(note.path).read() == 'alpha\nbravo\ncharlie'

def test_copy(note):
    # setup
    dest = note.path.replace('alpha', 'test')

    # success
    note.copy('test')
    assert os.path.exists(dest)
    assert os.path.exists(note.path)

def test_exists(note):
    # success
    assert     note.exists()
    assert not Note('/nope.txt').exists()

def test_match(note):
    # success
    assert     note.match('a*')
    assert not note.match('n*pe')

def test_reext(note):
    # setup
    dest = note.path.replace('txt', 'test')

    # success
    note.reext('test')
    assert     os.path.exists(dest)
    assert not os.path.exists(note.path)

def test_rename(note):
    # setup
    dest = note.path.replace('alpha', 'test')

    # success
    note.rename('test')
    assert     os.path.exists(dest)
    assert not os.path.exists(note.path)

def test_read(note):
    # success
    assert note.read() == 'alpha\nbravo'

def test_search(note):
    # success
    assert     note.search(r'(alpha)')
    assert not note.search(r'(nope)')

def test_write(note):
    # success
    note.write('test')
    assert open(note.path).read() == 'test'
