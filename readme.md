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

Required arguments are marked with `<angles>`, optional arguments with `[brackets]`, choices are in `(parentheses)`.

#### `list [GLOB] [-rs]`

List all notes, or notes matching `GLOB` (default `*`).

| Argument                   | Description            |
| -------------------------- | ---------------------- |
| `-r` `--reverse`           | Reverse sort order.    |
| `-s` `--sort (name\|size)` | Sort notes by element. |

<details><summary>Example.</summary>

~~~bash
$ posce list
charlie
claudia
josh
sam
toby

$ posce list c* -r -s name
claudia
charlie
~~~

</details>

#### `show NAME [-w]`

Print a note's contents to the screen.

| Argument            | Description         |
| ------------------- | ------------------- |
| `-w` `--wrap <int>` | Wrap text to width. |

<details><summary>Example.</summary>

~~~bash
$ posce show claudia
I had woot canal!

$ posce show sam -w 40
Over three and a half centuries ago,
linked by faith and bound by a common
desire for liberty, a small band of
pilgrims sought out a place in the New
World where they could worship according
to their own beliefs... and solve
crimes.
~~~


Contribution
------------

Bugs, suggestions, and feature requests are welcome! Please add them to the [issue tracker][is] with an appropriate label.

[ch]: https://github.com/posce/posce/blob/master/changes.md
[is]: https://github.com/posce/posce/issues
[li]: https://github.com/posce/posce/blob/master/license.md
[re]: https://github.com/posce/posce/releases/latest
[pp]: https://pypi.org/project/posce/
[py]: https://python.org
