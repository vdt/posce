'''
Testing tools and helpers.
'''

from click.testing import CliRunner

def out(book, cmd, *args):
    '''
    Return the output of a Click command.
    '''

    runner = CliRunner()
    result = runner.invoke(cmd, args, obj=book)
    return result.output.splitlines(keepends=True)
