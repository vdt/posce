Posce
=====

[![](https://img.shields.io/pypi/pyversions/posce)][py]
[![](https://img.shields.io/pypi/v/posce)][pp]
[![](https://img.shields.io/github/issues/posce/posce)][is]
[![](https://img.shields.io/badge/license-bsd--3-brightgreen)][li]

**Posce** (pronounced *posh·ee*) is a note-taking toolkit for your command line. It takes a single directory of plaintext note files and lets you create, edit, manipulate, and organise them to your heart's content; all in a single unified interface.

- See [changes.md][ch] for a complete changelog.
- See [license.md][li] for licensing information.

Table of Contents
-----------------

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Commands](#commands)
    - [`clip NAME`](#-clip-name-)
    - [`copy NAME DEST`](#-copy-name-dest-)
    - [`drop NAME`](#-drop-name-)
    - [`dump FILE [-l]`](#-dump-file---l--)
    - [`edit NAME [-e]`](#-edit-name---e--)
    - [`find TERM [-r]`](#-find-term---r--)
    - [`list [GLOB] [-rs]`](#-list--glob----rs--)
    - [`make NAME [-f]`](#-make-name---f--)
    - [`move NAME DEST`](#-move-name-dest-)
    - [`show NAME [-w]`](#-show-name---w--)
    - [`wget NAME URL`](#-wget-name-url-)
- [Contribution](#contribution)

Installation
------------

Posce required [Python 3.8][py] or higher. To install, you can:

- Run `pip install posce`, or
- Download and install the [latest release][re].

Configuration
-------------

Posce only requires you to set two environment variables:

~~~bash
# The path to your notes directory.
POSCE_DIR = "~/notes"

# The extension your note files use (no dot).
POSCE_EXT = "txt"
~~~

On macOS and Linux, these variables can be set in your shell profile script, most likely `$HOME/.profile`. On Windows, you can set them in the "Environment Variables" subscreen in System Properties (search "environment" in your Start Menu).

Usage
-----

Notes are always referred to by their pure name, no extension or filepath. In addition, notes and commands are disambiguated, which means you can write abbreviated versions and — if it's unambiguous — Posce will automatically expand them for you.

For example, if you have a directory that looks like this:

~~~text
- ~/notes
    - alpha.txt
    - bravo.txt
    - charlie.txt
~~~

Then your notes will look like this:

~~~bash
$ posce list
alpha
bravo
charlie

$ posce show c
Charliiiiiiieeeeeee!
~~~

And you can abbreviate commands like this:

~~~bash
$ posce l
alpha
bravo
charlie

$ posce s c
Charliiiiiiieeeeeee!
~~~

### Commands

#### `clip NAME`

Copy the existing note `NAME` to the clipboard.

~~~bash
$ posce clip alpha
# Copy "alpha.txt" to clipboard.
~~~

#### `copy NAME DEST`

Copy the existing note `NAME` to the new note `DEST`.

~~~bash
$ posce copy alpha delta
# Copy "alpha.txt" to new file "delta.txt".
~~~

#### `drop NAME`

Move the existing note `NAME` to the system trash/recycle bin.

~~~bash
$ posce drop alpha
# Move "alpha.txt" to trash/recycle bin.
~~~

#### `dump FILE [-l]`

Create a zip archive of the notes directory at `FILE`.

- `-l` `--level INT`: Compression level from `0` to `9` (default `5`).

~~~bash
$ posce dump notes.zip
# Create zip archive "notes.zip".

$ posce dump notes.zip --level 9
# Create "notes.zip" with maximum compression.
~~~

#### `edit NAME [-e]`

Edit the existing note `NAME` in your default editor.

- `e` `--editor PROG`: Open the note in the program `PROG` instead.

~~~bash
$ posce edit alpha
# Open "alpha.txt" in default "txt" editor.

$ posce edit alpha --editor notepad
# Open "alpha.txt" in "notepad".
~~~

#### `find TERM [-r]`

List all notes containing the substring or regular expression `TERM`.

- `r` `--regex`: Use search term as regex.

~~~bash
$ posce find "Charliiiiiiieeeeeee!"
charlie

$ posce find "Charli{7}e{7}!" --regex
charlie
~~~

#### `list [GLOB] [-rs]`

List all notes with names matching `GLOB` (default `*`).

- `-r` `--reverse`: Reverse sorting order.
- `-s` `--sort (name|size)`: Sort notes by name or size.

~~~bash
$ posce list
alpha
bravo
charlie

$ posce list al*
alpha

$ posce list --reverse --sort name
charlie
bravo
alpha
~~~

#### `make NAME [-f]`

Create the new empty note `NAME`.

- `-f` `--file FILE`: Copy the note's contents from a file.

~~~bash
$ posce make delta
# Create empty file "delta.txt" in notes directory.

$ posce make delta --file ~/temp.txt
# Create "delta.txt" with contents from "~/temp.txt".
~~~

#### `move NAME DEST`

Move the existing note `NAME` to the new note `DEST`.

~~~bash
$ posce move alpha delta
# Move "alpha.txt" to "delta.txt".
~~~

#### `show NAME [-w]`

Print the contents of the existing note `NAME`.

- `-w` `--wrap COLS`: Wrap text to this width.

~~~bash
$ posce show alpha
This is the note Alpha!

$ posce show bravo --wrap 40
This is the much longer note Bravo, and
will be wrapped across two lines.
~~~

#### `wget NAME URL`

Download a URL into the existing note `NAME`.

~~~bash
$ posce wget alpha example.com
# Download "https://example.com" and write contents to "alpha.txt".
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
