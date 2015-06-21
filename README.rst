.. image:: https://travis-ci.org/DevinCarr/artemis-core.svg?branch=master
    :target: https://travis-ci.org/DevinCarr/artemis-core

Artemis-Core (Arty)
=======================
This is the core module and shell runtime for Arty.

Artemis (Arty) is a Python-based shell that encapsulates
the standard Bash prompt to give it more extensibility through
Python modules. Artemis-Core also acts as the entry point and core
for a learning build tool and 'helpful AI'. Most of the other
parts are still in progress.

Install
=======================
Requirements:
- Python 3.4+

Installing: (Notice, not pushed to PyPi yet, so see Contributing for installation)

``$ pip3 install artemis-core``

Run with:

``$ arty``

Example commands
=======================
``help``: Display the help

``lc``:   List Python-based commands

``quit``: Quit out of Arty

\*Note: Any normal command within Bash can be executed. If Arty doesn't understand
 the command, the command will be passed to Bash to be executed.

Plugin Commands
=======================
Run ``add <github link>`` within Arty to download and load a plugin.
The plugin module will be stored within the ``~/.artemis/`` folder.

Folder Structure of plugin:

\\folder

  \\module_name

    __init__.py

    file.py

  \\tests

    test1.py

    test2.py

Arty will then load the command as "module_name".
The ``__init__.py`` for the plugin module will have to have two functions:
``def execute(args):`` which will take a list of arguments, if any are passed.
And: ``def help_message():`` which takes no parameters and should return a string
that is a short help for the module's execute function.

Contributing
=======================
Install:

``$ git clone git@github.com:DevinCarr/artemis-core.git``

``$ cd artemis-core``

``$ pip3 install -e .``


License
============
The MIT License (MIT)

Copyright (c) 2015 Devin Carr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
