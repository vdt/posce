'''
Tests for 'posce.tools.clui'.
'''

import click
import pytest

from posce.tools import clui

def test_error():
    # success
    with pytest.raises(click.ClickException) as exc:
        clui.error('foo')
    assert exc.exconly() == 'click.exceptions.ClickException: foo'
