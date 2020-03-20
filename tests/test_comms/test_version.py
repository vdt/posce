'''
Tests for 'posce.comms.version'.
'''

from posce               import VERSION_STRING
from posce.comms.version import version
from tests.tools         import out

def test_version():
    # success
    assert out(None, version) == [VERSION_STRING + '\n']
