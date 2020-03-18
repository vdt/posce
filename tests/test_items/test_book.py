'''
Tests for 'posce.items.book'.
'''

import os.path

import pytest

from posce.items.book import Book

@pytest.fixture
def book(tmpdir):
    dire = tmpdir.join('book')
    dire.mkdir()
    for name in ['foo', 'bar', 'baz']:
        dire.join(f'{name}.txt').write(name)
    return Book(dire, 'txt')

def test_init(book):
    # success
    assert book.dire.endswith('book')
    assert book.ext == 'txt'
    assert book.notes.keys() == {'foo', 'bar', 'baz'}

def test_contains(book):
    # success
    assert 'foo'      in book
    assert 'nope' not in book

def test_eq(book):
    # success
    assert book == book
    assert book != Book('/nope', 'txt')
    assert book != 'not a book'

def test_getitem(book):
    # success
    assert book['foo'] == book.notes['foo']

def test_hash(book):
    # success
    assert {book, book} == {book}

def test_iter(book):
    # success
    assert set(book) == set(book.notes.values())

def test_len(book):
    # success
    assert len(book) == 3

def test_repr(book):
    # setup
    book.dire = '/dir'

    # success
    assert repr(book) == "Book('/dir', 'txt')"

def test_create(book):
    # success
    note = book.create('test', 'test')
    assert book.notes['test'] == note
    assert note.name   == 'test'
    assert note.read() == 'test'
    assert os.path.dirname(note.path) == book.dire

def test_exists(book):
    # success
    assert     book.exists()
    assert not Book('/nope', 'txt').exists()

def test_filter(book):
    # success
    gen = book.filter(lambda note: True)
    assert set(gen) == set(book.notes.values())

def test_match(book):
    # success
    assert set(book.match('ba?')) == {book['bar'], book['baz']}

def test_search(book):
    # success
    assert set(book.search(r'(foo)')) == {book['foo']}
