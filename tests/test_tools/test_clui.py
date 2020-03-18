'''
Tests for 'posce.tools.clui'.
'''

import click
import pytest

from posce.tools import clui

def test_error():
    # success
    with pytest.raises(click.ClickException) as exc:
        clui.error('test')
    assert exc.exconly() == 'click.exceptions.ClickException: test'
