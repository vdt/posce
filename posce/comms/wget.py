'''
Click command function 'wget'.
'''

import urllib.parse
import urllib.request

import click

from posce            import tools
from posce.comms.base import group

@group.command()
@click.argument('name')
@click.argument('url')
@click.pass_obj
def wget(book, name, url):
    '''
    Download a note from a URL.
    '''

    note = tools.clui.disambiguate(book, name)
    url  = url if url.startswith('http') else f'http://{url}'

    try:
        resp = urllib.request.urlopen(url)
        if data := resp.read():
            note.write(data.decode('utf-8'))

    except urllib.error.URLError:
        tools.clui.error(f'Could not find {url!r}.')
