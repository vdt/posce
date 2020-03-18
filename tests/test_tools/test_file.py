'''
Tests for 'posce.tools.file'.
'''

import pytest

from posce.tools import file

def test_append(tmpdir):
    # setup
    path = tmpdir.join('append.txt')
    path.write('foo\nbar')

    # success
    file.append(path, 'baz', sep='\n')
    assert path.read() == 'foo\nbar\nbaz'

def test_create(tmpdir):
    # setup
    path = tmpdir.join('create.txt')

    # success
    file.create(path, 'test')
    assert path.read() == 'test'

    # failure - file exists
    with pytest.raises(FileExistsError):
        file.create(path, 'test')

def test_exists(tmpdir):
    # setup
    path = tmpdir.join('exists.txt')
    path.write('test')

    # success
    assert     file.exists(path)
    assert not file.exists('/nope')

def test_find(tmpdir):
    # setup
    dire = tmpdir.join('find')
    dire.mkdir()
    for name in ['foo', 'bar', 'baz']:
        dire.join(f'{name}.txt').write('test')

    # success
    assert list(file.find(dire, 'ba?.txt')) == [
        str(dire.join('bar.txt')),
        str(dire.join('baz.txt')),
    ]

def test_read(tmpdir):
    # setup
    path = tmpdir.join('read.txt')
    path.write('test')

    # success
    assert file.read(path) == 'test'

def test_write(tmpdir):
    # setup
    path = tmpdir.join('write.txt')

    # success
    file.write(path, 'test')
    assert path.read() == 'test'
