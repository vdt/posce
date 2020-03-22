Posce
=====

[![](https://img.shields.io/pypi/pyversions/posce)][py]
[![](https://img.shields.io/pypi/v/posce)][pp]
[![](https://img.shields.io/github/issues/posce/posce)][is]
[![](https://img.shields.io/badge/license-bsd--3-brightgreen)][li]

**Posce** (pronounced *posh·ee*) is a note-taking toolkit for your command line. It takes a single directory of plaintext note files and lets you create, edit, manipulate, and organise them to your heart's content.

- See [changes.md][ch] for a complete changelog.
- See [license.md][li] for licensing information.

Installation
------------

Posce required [Python 3.8][py] or higher. To install, you can:

- Run `pip install posce`, or
- Download the [latest release][re].

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

<details><summary>Example.</summary>

If you have a directory that looks like this:

~~~text
- ~/notes
    - josh.txt
    - sam.txt
    - toby.txt
~~~

Then your notes will look like this:

~~~bash
$ posce list
josh
sam
toby

$ posce show j
"Toby, come quick, Sam's getting his ass kicked by a girl!"
~~~

And you can abbreviate commands like this:

~~~bash
$ posce l
josh
sam
toby

$ posce s j
"Toby, come quick, Sam's getting his ass kicked by a girl!"
~~~

I recommend aliasing `posce` to `p` for maximum brevity.

</details>

### Commands

Required arguments are marked with `<angles>`, optional arguments with `[brackets]`, choices are in `(parentheses)`.

#### `copy <NAME> <DEST>`

Copy a note to another file in the same directory.

<details><summary>Example.</summary>

~~~bash
$ posce copy ed larry
# Copy "ed.txt" to "larry.txt".
~~~

</details>

#### `edit <NAME> [-en]`

Open a new or existing note in an editor.

| Argument        | Description                | Default         |
| --------------- | -------------------------- | --------------- |
| `-e` `--editor` | Open note in this program. | System default. |

<details><summary>Example.</summary>

~~~bash
$ posce edit toby
# Open "toby.txt" in your default editor.

$ posce edit toby -e notepad
# Open "toby.txt" in Notepad.
~~~

</details>

#### `find <TERM> [-r]`

List all notes containing a substring or matching a regular expression.

| Argument       | Description                            | Default   |
| -------------- | -------------------------------------- | --------- |
| `-r` `--regex` | Use search term as regular expression. | Disabled. |

<details><summary>Example.</summary>

~~~bash
$ posce find "jackass"
josh
toby

$ posce find "It's on page \d{1,3}!" -r
claudia
~~~

</details>

#### `list [GLOB] [-rs]`

List all notes, or notes matching `GLOB` (default `*`).

| Argument                   | Description               | Default   |
| -------------------------- | ------------------------- | --------- |
| `-r` `--reverse`           | Reverse sort order.       | Disabled. |
| `-s` `--sort (name\|size)` | Sort notes by this field. | `name`    |

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

#### `move <NAME> <DEST>`

Move a note to another file in the same directory.

<details><summary>Example.</summary>

~~~bash
$ posce move claudia cj
# Move "claudia.txt" to "cj.txt".
~~~

</details>

#### `show <NAME> [-w]`

Print a note's raw contents to the screen.

| Argument            | Description                 | Default   |
| ------------------- | --------------------------- | --------- |
| `-w` `--wrap <int>` | Wrap text to width `<int>`. | Disabled. |

<details><summary>Example.</summary>

~~~bash
$ posce show claudia
"I had woot canal!"

$ posce show sam -w 40
"Over three and a half centuries ago,
linked by faith and bound by a common
desire for liberty, a small band of
pilgrims sought out a place in the New
World where they could worship according
to their own beliefs... and solve
crimes."
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
