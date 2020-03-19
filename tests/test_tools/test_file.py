'''
Tests for 'posce.tools.file'.
'''

import pytest

from posce.tools import file

def test_append(tmpdir):
    # setup
    path = tmpdir.join('append.txt')
    path.write('alpha\nbravo')

    # success
    file.append(path, 'charlie', sep='\n')
    assert path.read() == 'alpha\nbravo\ncharlie'

def test_copy(tmpdir):
    # setup
    path = tmpdir.join('copy.txt')
    path.write('')

    # success
    file.copy(path, 'dest')
    assert path.exists()
    assert tmpdir.join('dest.txt').exists()

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
    path.write('')

    # success
    assert     file.exists(path)
    assert not file.exists('/nope')

def test_find(tmpdir):
    # setup
    dire = tmpdir.join('find')
    dire.mkdir()

    for name in ['alpha', 'bravo', 'charlie']:
        dire.join(f'{name}.txt').write('test')

    # success
    assert list(file.find(dire, '*h*.txt')) == [
        str(dire.join('alpha.txt')),
        str(dire.join('charlie.txt')),
    ]

def test_read(tmpdir):
    # setup
    path = tmpdir.join('read.txt')
    path.write('test')

    # success
    assert file.read(path) == 'test'

def test_reext(tmpdir):
    # setup
    path = tmpdir.join('reext.txt')
    path.write('')

    # success
    file.reext(path, 'new')
    assert not path.exists()
    assert     tmpdir.join('reext.new').exists()

def test_rename(tmpdir):
    # setup
    path = tmpdir.join('rename.txt')
    path.write('')

    # success
    file.rename(path, 'dest')
    assert not path.exists()
    assert     tmpdir.join('dest.txt').exists()

def test_write(tmpdir):
    # setup
    path = tmpdir.join('write.txt')

    # success
    file.write(path, 'test')
    assert path.read() == 'test'
