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

    for n, name in enumerate(['alpha', 'bravo', 'charlie']):
        dire.join(f'{name}.txt').write(name * (n+1))
    return Book(dire, 'txt')

def test_init(book):
    # success
    assert book.dire.endswith('book')
    assert book.ext == 'txt'
    assert book.notes.keys() == {'alpha', 'bravo', 'charlie'}

def test_contains(book):
    # success
    assert 'alpha'    in book
    assert 'nope' not in book

def test_eq(book):
    # success
    assert book == book
    assert book != Book('/nope', 'txt')
    assert book != 'not a book'

def test_getitem(book):
    # success
    assert book['alpha'] == book.notes['alpha']

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
    book.dire = '/dire'

    # success
    assert repr(book) == "Book('/dire', 'txt')"

def test_create(book):
    # success
    note = book.create('test', 'test')
    assert book.notes['test'] == note
    assert note.name   == 'test'
    assert note.read() == 'test'
    assert os.path.dirname(note.path) == book.dire

def test_disambiguate(book):
    # success
    assert set(book.disambiguate('al')) == {book['alpha']}

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
    assert set(book.match('a*')) == {book['alpha']}

def test_search(book):
    # success
    assert set(book.search(r'(alpha)')) == {book['alpha']}
