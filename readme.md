Posce
=====

[![](https://img.shields.io/pypi/pyversions/posce)][py]
[![](https://img.shields.io/pypi/v/posce)][pp]
[![](https://img.shields.io/github/issues/posce/posce)][is]
[![](https://img.shields.io/badge/license-bsd--3-brightgreen)][li]

**Posce** (pronounced *posh·eee*) is a note-taking toolkit for your command line. It takes a single directory of plaintext note files and lets you create, edit, manipulate, and organise them to your heart's content.

- See [changes.md][ch] for a complete changelog.
- See [license.md][li] for licensing information.

Installation
------------

Posce required [Python 3.8][py] or higher. To install, you can:

- Run `pip install posce`, or
- Download the [latest release][re].

Configuration
-------------

Posce only requires two environment variables to be set:

~~~bash
# The path to your notes directory.
POSCE_DIR = "~/notes"

# The extension your note files use (no dot).
POSCE_EXT = "txt"
~~~

On macOS and Linux, these variables can be set in your shell profile script, most likely `$HOME/.profile`. On Windows, you can set them in the "Environment Variables" subscreen in System Properties (search "environment" in your Start Menu).

Usage
-----

### Commands

Optional arguments are marked with `[brackets]`, choices are in `(parentheses)`.

#### `list [GLOB] [-rs]`

List all notes, or notes matching `GLOB` (default `*`).

| Argument                   | Description            |
| -------------------------- | ---------------------- |
| `-r` `--reverse`           | Reverse sort order.    |
| `-s` `--sort (name\|size)` | Sort notes by element. |

<details><summary>Example.</summary>

~~~bash
$ posce list
alpha
bravo
charlie

$ posce list *ha* -r -s name
charlie
alpha
~~~

</details>

Contribution
------------

Bugs, suggestions, and feature requests are welcome! Please add them to the [issue tracker][is] with an appropriate label.

[ch]: https://github.com/posce/posce/blob/master/changes.md
[is]: https://github.com/posce/posce/issues
[li]: https://github.com/posce/posce/blob/master/license.md
[re]: https://github.com/posce/posce/releases/latest
[pp]: https://pypi.org/project/posce/
[py]: https://python.org
