<p align="center">
Cheat sheet for the <a href="https://xon.sh">xonsh shell</a> with copy-pastable examples. This is a good level of knowledge to start being productive.
<br><br>
<img src="https://repository-images.githubusercontent.com/310804308/f11fa180-280d-11eb-8fa4-c389308692bd">
</p>

<p align="center">
If you like the cheatsheet click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=The%20xonsh%20shell%20cheat%20sheet.&url=https://github.com/anki-code/xonsh-cheatsheet" target="_blank">tweet</a> about it.
</p>

[Full screen reading](https://github.com/anki-code/xonsh-cheatsheet/blob/main/README.md)

# What is xonsh?

Xonsh is a Python-powered, cross-platform, Unix-gazing shell language and command prompt. The language is a superset of Python 3.6+ with additional shell primitives that you are used to from [Bash](https://www.gnu.org/software/bash/) and [IPython](https://ipython.org/). It works on all Python-compatible systems, including Linux, macOS, and Windows. Try [right off the bat examples](https://github.com/anki-code/xonsh-cheatsheet/blob/main/README.md#xonsh-basics).

# What does xonsh mean?

The "xonsh" word sounds like [conch [kɑːntʃ]](https://www.google.com/search?q=what+is+conch) - a common name of a number of different sea snails or shells (🐚). Thus xonsh is the reference to the shell word that is commonly used to name [command shells](https://en.wikipedia.org/wiki/Shell_(computing)).

You will also face with "xontrib" word. The xontrib is short version of ["(contrib)ution"](https://www.collinsdictionary.com/dictionary/english/contribution) word and points to extensions, community articles and other materials around xonsh.

# Install xonsh

There are three ways to use xonsh:

1. **[Simple xonsh install](#simple-xonsh-install)**. You can use the system installed Python to install xonsh and dependencies. This is a good option if you don't plan to manage Python versions or virtual environments.

2. **[Install xonsh with package and environment management system](#install-xonsh-with-package-and-environment-management-system)**. In this way you can flexibly manage the Python version, dependencies, and virtual environments, but because xonsh is a Python-based shell you have to understand what you're doing and the section below will provide some guidance.

3. **[Try xonsh without installation](#try-xonsh-without-installation)**. Use Docker or the Linux AppImage to run and try xonsh.

### Simple xonsh install

Most modern operating systems have [Python](https://www.python.org/) and [PyPi (pip)](https://packaging.python.org/tutorials/installing-packages/) that are preinstalled or that can be installed easily. By installing from PyPi you will get [the latest version of the xonsh shell](https://github.com/xonsh/xonsh/releases). We highly recommend using the `full` version of the xonsh PyPi-package with [prompt-toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/) on board:
```xsh
python -m pip install 'xonsh[full]'
```

Another way is to install xonsh from the package manager that is supplied by the operating system. This way is _not_ recommended because in operating systems without the [rolling release concept](https://en.wikipedia.org/wiki/Rolling_release) the xonsh shell version may be very old ([check latest xonsh release](https://github.com/xonsh/xonsh/releases/) or [versions of xonsh across platforms](https://repology.org/project/xonsh/versions)) because the average [release cycle for the xonsh shell](https://github.com/xonsh/xonsh/releases) is quarter.

```xsh
# Not recommended but possible
apt install xonsh     # Debian/Ubuntu
pacman -S xonsh       # Arch Linux
dnf install xonsh     # Fedora
brew install xonsh    # OSX
```

On any system you can install `python` and then install xonsh from pip i.e., `any_pkg_manager install python && python -m pip install 'xonsh[full]'` This is the preferable way.

### Install xonsh with package and environment management system

Xonsh is a Python-based shell, and to run xonsh you must have Python installed. The Python version and its packages can be installed and located anywhere: in the operating system directories, as part of a virtual environment, as part of the user directory, or as a virtual drive created temporarily behind the scenes by the Linux AppImage.

The first thing you have to remember is that when you execute `import` or any other Python code during a xonsh session it will be executed in the Python environment that was used to run current instance of xonsh.

In other words, you can activate a virtual environment during a xonsh session (using conda, pyenv, pipx) but the current session will continue to use packages from the environment that was used to run xonsh. And if you want to run xonsh with the packages from the currently activated virtual environment you have to install xonsh in that environment and run it directly.

Thus the second thing you should remember is that when you run xonsh in virtual environment it will try to load [xonsh RC files](https://xon.sh/xonshrc.html#run-control-file) (i.e. `~/.xonshrc`) and because the virtual environment is different from the environement you ordinarily use, the loading of the RC file will tend to fail because of the lack of the appropriate set of packages. When you write your `~/.xonshrc` it's good practice to check the existing external dependencies before loading them. See also [xontrib-rc-awesome](https://github.com/anki-code/xontrib-rc-awesome).

#### Install xonsh on macOS or Linux using conda

You can use [Conda](https://docs.conda.io/en/latest/) with [Conda-forge](https://conda-forge.org/) to install and use xonsh. 

```xsh
#
# Install python using brew
#
zsh  # Default macOS shell
# Install brew from https://brew.sh/
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python  # or `python@3.11`

#
# Install Miniconda from https://docs.conda.io/en/latest/miniconda.html 
# (example for Mac, use the link for your platform)
#
cd /tmp
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh
chmod +x Miniconda3-latest-MacOSX-arm64.sh
./Miniconda3-latest-MacOSX-arm64.sh
# Add conda init code that was printed to `~/.zshrc` and restart zsh.
# Or run `/Users/username/miniconda3/bin/conda init zsh` to add init to ~/.zshrc and restart zsh.

# After restarting zsh you will see `(base)` in prompt.
# This means that you're in the conda `base` environment.

# Switch to Conda-forge channel
conda config --add channels conda-forge
conda config --set channel_priority strict 
conda update --all --yes

# Install xonsh to the `base` environment
conda install xonsh
conda init xonsh  # Add init to ~/.xonshrc. You can also add `$CONDA_AUTO_ACTIVATE_BASE='false'` to avoid conda loading at start

which xonsh
# /Users/username/miniconda3/bin/xonsh

# Run xonsh from the `base` environment
xonsh
```
How to work and understand the environments in conda:
```xsh
# `xpip` is used to install packages to the current xonsh session location (now it's `base` environment)
xpip install ujson  

# Example of creating the environment with a certain version of Python
conda search python | grep 3.10
conda create -n "py310" python=3.10 xonsh

conda activate py310
# Now the environment is `py310` but current xonsh session is still in `base` environment

which xonsh
# /Users/username/miniconda3/envs/py310/bin/xonsh

which pip
# /Users/username/miniconda3/envs/py310/bin/pip  # pip from `py310`

which xpip
# /Users/username/miniconda3/bin/pip  # pip from `base` environment from where xonsh ran

# Run xonsh that installed in `py310` environment from xonsh runned in `base` environment
xonsh
conda activate py310
# Now xonsh session is in `py310` environment and the current environment is also `py310`

import ujson
# No module named 'ujson'   # YES because ujson was installed in `base` environment
```

On Mac we also recommend to install [GNU coreutils](https://www.gnu.org/software/coreutils/) to use the Linux default tools (i.e. `ls`, `grep`):
```xsh
brew install coreutils
$PATH.append('/opt/homebrew/opt/coreutils/libexec/gnubin')  # add to ~/.xonshrc
```

#### How to understand the xonsh location

Which xonsh and which Python used to run the **current** xonsh session:

```xsh
import sys
[sys.argv[0], sys.executable]
# ['/opt/homebrew/bin/xonsh', '/opt/homebrew/opt/python@3.11/bin/python3.11']


@(sys.executable) -m site
# Full info about paths
```

Which `xonsh` and which `python` that will be executed to run **new instances** depends on the list of directories in `$PATH` or virtual environment:

```xsh
$PATH
# ['/home/user/miniconda3/bin', '/opt/homebrew/bin]

[$(ls -la @$(which xonsh)), $(ls -la @$(which python)), $(python -V)]
# ['/home/user/miniconda3/bin/xonsh', '/home/user/miniconda3/bin/python -> python3.11', 'Python 3.11.1']

python -m site
# Full info about paths
```

#### pipx and xonsh

The [pipx](https://pipxproject.github.io/pipx/) tool is also good to install xonsh in case you need certain Python version:
```xsh
# Install Python before continuing
pip install pipx
pipx install --python python3.8 xonsh
pipx run xonsh 
# or add /home/$USER/.local/bin to PATH (/etc/shells) to allow running just the `xonsh` command
```

### Try xonsh without installation

#### Docker

```python
# Docker with specific Python version and latest release of xonsh
docker run --rm -it python:3.11-slim /bin/bash \
 -c "pip install 'xonsh[full]' && xonsh"

# Docker with specific Python version and xonsh from the master branch
docker run --rm -it python:3.11-slim /bin/bash \
 -c "apt update && apt install -y git && pip install -U git+https://github.com/xonsh/xonsh && xonsh"

# Official xonsh docker image has an old version
docker run --rm -it xonsh/xonsh:slim
```

#### Linux-portable AppImage contains both [Python 3 and xonsh in one file](https://xon.sh/appimage.html)

```python
wget https://github.com/xonsh/xonsh/releases/latest/download/xonsh-x86_64.AppImage -O xonsh
chmod +x xonsh
./xonsh

# Then if you don’t have Python on your host, you can acccess it from the AppImage by running:
$PATH = [$APPDIR + '/usr/bin'] + $PATH
python -m pip install tqdm --user  # the `tqdm` package will be installed to ~/.local/
import tqdm
```

You can [build your own xonsh AppImage](https://xon.sh/appimage.html#building-your-own-xonsh-appimage) with the packages you need in 15 minutes.

# Xonsh basics

The xonsh language is a superset of Python 3 with additional shell support. As result you can mix shell commands and Python code as easily as possible. Right off the bat examples:

```xsh
cd /tmp && ls                     # shell commands

21 + 21                           # python command

for i in range(0, 42):            # mix python 
    echo @(i+1)                   # and the shell

len($(curl https://xon.sh))       # mix python and the shell

$PATH.append('/tmp')              # using environment variables

p'/etc/passwd'.read_text().find('root')  # path-string returns Path 
                                         # (https://docs.python.org/3/library/pathlib.html)

for line in $(cat /etc/passwd).splitlines():  # read the lines from the output
    echo @(line.split(':')[0])                # prepare line on Python and echo

for file in gp`*.*`:              # reading the list of files as Path-objects
    if file.exists():             # using rich functionality of Path-objects
        du -sh @(file)            # and pass it to the shell command

import json                       # python libraries are always at hand
if docker_info := $(docker info --format '{{json .}}'):
    print('ContainersRunning:', json.loads(docker_info)['ContainersRunning'])

xpip install xontrib-prompt-bar   # xonsh has huge amount of powerful extensions
xontrib load prompt_bar           # follow the white rabbit - https://github.com/topics/xontrib

# Finally fork https://github.com/anki-code/xontrib-rc-awesome
# to convert your ~/.xonshrc into a pip-installable package 
# with the extensions you need on board.
```

Looks nice? [Install xonsh](#install-xonsh)!

## Three most frequent things that newcomers overlook

### 1. [Shell commands, also known as subprocess commands](https://xon.sh/tutorial.html#python-mode-vs-subprocess-mode)

The first thing you should remember is that the shell commands are not the calls of another shell (i.e. bash). Xonsh has its own parser implementation for subprocess commands, and this is why a command like `echo {1..5} \;` (brace expansion and escape characters in bash) won't work. Most sh-shell features [can be replaced](https://xon.sh/bash_to_xsh.html) by sane Python alternatives. For example, the earlier command could be expressed as `echo @(range(1,6)) ';'`.

If you think that only xonsh has the sh-uncompatible elements in its parser, you are mistaken. If we compare Bash and Zsh we will find that `pip install package[subpackage]` command will work in Bash but in Zsh the error will be raised because Zsh has a special meaning for square braces. It's normal to have an evolution in the syntax and features. 

Be calm and accept the sane and self-consistent Python-driven mindset.

*Note:*

* *Most of novice try to copy and paste sh-lang commands that contain special characters and get syntax errors in xonsh. If you want to run environment agnostic sh-lang's commands that you copy from the internet just use the macro call in xonsh `bash -c! echo {123}` or use [xontrib-sh](https://github.com/anki-code/xontrib-sh) to run context-free bash commands in xonsh by adding `! ` at the beginning of the command.*
* *We highly recommend to taking a look at the section [Install xonsh with package and environment management system](#install-xonsh-with-package-and-environment-management-system).*


### 2. [Strings and arguments in shell commands](https://xon.sh/tutorial_subproc_strings.html)

The second potential misunderstanding comes from the first. To escape special charecters, the special meaning of braces, or pass a string as an argument, use quotes. When in doubt, use quotes!

You should clearly understand the difference:

 <table style="width:100%">
  <tr>
    <th>sh-lang shells</th>
    <th>xonsh</th>
  </tr>
<tr>
<td>
1. Has an escape character:
<pre>
<b>echo 123\ 456</b>
# 123 456
</pre>
</td>
    <td>
1. Use quotes:
<pre>
<b>echo "123 456"</b>
# 123 456
</pre>
<a href="https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals">Escape character</a> to wrap and so on:
<pre>
<b>echo "123\
456"</b>
# 123456
</pre>

</td>
  </tr>

<tr>
<td>
2. Open the quotes:
<pre>
<b>echo --arg="val"</b>
# --arg=val<br>
# and:<br>
<b>echo --arg "val"</b>
# --arg val

</pre>
</td>
    <td>
2. Save quotes:
<pre>
<b>echo --arg="val"</b>
# --arg="val"<br>
# But if argument quoted entirely:<br>
<b>echo --arg "val"</b>
# --arg val
</pre>
</td>
  </tr>

<tr>
<td>
3. Brackets have no meaning:
<pre>
<b>echo {123} [456]</b>
# {123} [456]<br><br><br>
</pre>
</td>
    <td>
3. Brackets have meaning:
<pre>
<b>echo {123} [456]</b>
# SyntaxError<br>
<b>echo "{123}" '[456]'</b>
# {123} [456]
</pre>
</td>
  </tr>
</table> 

*Note:*

* *You can wrap any argument into Python string substitution:*
    ```python
    name = 'snail'
    echo @('--name=' + name.upper())
    # --name=SNAIL
    ```
* *You can use the `showcmd` command to show the arguments list:*    
    ```python
    showcmd echo The @('arguments') @(['list', 'is']) $(echo here) "and" --say="hello" to you
    # ['echo', 'The', 'arguments', 'list', 'is', 'here\n', 'and', '--say="hello"', 'to', 'you']]    
    ```


### 3. The process substitution operator `$()` returns output with [universal new lines](https://www.python.org/dev/peps/pep-0278/)

In sh-compatible shells, the [process substitution operator](https://en.wikipedia.org/wiki/Process_substitution) `$()` executes the command and then splits the output and uses those parts as arguments. The command `echo $(echo -e "1 2\n3")` will have three distinct arguments, `1`, `2` and `3` that will passed to the first `echo`.

In xonsh shell the `$()` operator returns the output of the command. The command `echo $(echo -e "1 2\n3")` will have one argument, `1 2\n3\n` that will be passed to the first `echo`.

*Note:*

* *To do what sh-compatible shells are doing with the `$()` operator, the xonsh shell has the `@$()` operator that will be described in the next chapter.*
    ```python
    showcmd echo @$(echo "1\n2 3\n4")
    # ['echo', '1', '2', '3', '4']
    ```
* *To transform output to the lines for the arguments list you can use [splitlines](https://docs.python.org/3/library/stdtypes.html#str.splitlines) function and the python substitution:*
    ```python
    showcmd echo @($(echo "1\n2 3\n4").splitlines())  # the first echo will get three arguments: "1", "2 3", "4"
    # ['echo', '1', '2 3', '4']
    ```
* *Not all xonsh users like this behavior of `$()` operator, and in the future, this may be changed. There is [a thread to discussing](https://github.com/xonsh/xonsh/issues/3924) this and the [Xonsh Enhancement Proposal #2](https://github.com/anki-code/xonsh-operators-proposal/blob/main/XEP-2.rst).*

# [Switching from `$` to `@`](https://github.com/xonsh/xonsh/issues/4152)

By default, the xonsh shell has a bash-like appearance for its interactive prompt: `user@host ~ $`. After reading the previous section you can understand that we highly recommended replacing `$` with `@` by adding this line to your `~/.xonshrc`:

```python
$PROMPT_FIELDS['prompt_end'] = '@'  # or '\n@' to have fixed position of the command typing
```

Or by using [xontrib-prompt-bar](https://github.com/anki-code/xontrib-prompt-bar). Now the prompt will appear as: `user@host ~ @`. This will remind you that you are in the xonsh shell. You can use [xontrib-sh](https://github.com/anki-code/xontrib-sh) to run sh-shell commands.

# [Operators](https://xon.sh/tutorial.html#captured-subprocess-with-and)

### `$()` - capture and return output without printing stdout and stderr

Captures stdout and returns output with [universal new lines](https://www.python.org/dev/peps/pep-0278/):
```python
showcmd $(echo -e '1\n2\r3 4\r\n5')    # Subproc mode
# ['1\n2\n3 4\n5\n']

output = $(echo -e '1\n2\r3 4\r\n5')   # Python mode 
output
# '1\n2\n3 4\n5\n'
```

### `!()` - capture all and return object without printing stdout and stderr

Captures stdout and returns [CommandPipeline](https://xon.sh/api/procs/pipelines.html#xonsh.procs.pipelines.CommandPipeline). Truthy if successful (returncode == 0), compares to, iterates over lines of stdout:
  
```python
ret = !(echo 123)
ret
#CommandPipeline(
#  pid=404136,
#  returncode=0,
#  args=['echo', '123'],
#  alias=None,
#  timestamps=[1604742882.1826484, 1604742885.1393967],
#  executed_cmd=['echo', '123'],
#  input='',
#  output='123\n',
#  errors=None
#)   

if ret:
      print('Success')     
#Success

for l in ret:
      print(l)     
#123
#

```

Note! In some cases, to get the output you need to convert an object to a string or invoke `.end()` manually or use the `.out`:

```xsh
r = !(ls /)
r.output
# ''

r.end()
r.output
# 'bin\netc\n...'

r = !(ls /)
r.out                # out is forcing ending
# 'bin\netc\n...'

r = !(ls /)
print(r)             # r will be converted to str and the ending will be forced
# bin
# etc
# ...
```

### `$[]` - not capturing (return `None`), print stdout and stderr

Passes stdout to the screen and returns `None`:

```python
ret = $[echo 123]
#123
repr(ret)
'None'
```

This is the same as `echo 123`, but this syntax allows explicitly running a subprocess command.

### `![]` - capture all and return hidden object, print stdout and stderr

Passes stdout to the screen and returns [HiddenCommandPipeline](https://xon.sh/api/procs/pipelines.html#xonsh.procs.pipelines.HiddenCommandPipeline):

```python
ret = ![echo -e '1\n2\r3 4\r\n5']
#1
#3 4
#5
ret               # No return value because it's hidden CommandPipeline object
ret.out           # But it has the properties from CommandPipeline
'1\n2\r3 4\n5\n'
```

This operator is used under the hood for running commands at the interactive xonsh prompt.

### `@()` - use Python code as an argument or a callable alias

Evaluates Python and passes the arguments:

```python
showcmd 'Supported:' @('string') @(['list','of','strings']) 
#['Supported:', 'string', 'list', 'of', 'strings']

echo -n '!' | @(lambda args, stdin: 'Callable' + stdin.read())
#Callable!
```

### `@$()` - split output of the command by white spaces for arguments list

```python
showcmd @$(echo -e '1\n2\r3 4\r\n5')
#['1', '2\r3', '4', '5']
```
This is mostly [what bash's `$()` operator does](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html).

# [Environment Variables](https://xon.sh/tutorial.html#environment-variables)

```python
${...}            # Get the list of environment variables
__xonsh__.env     # Get the list of environment variables using Python syntax

$VAR = 'value'    # Set environment variable

ENV = ${...}                # short typing
ENV.get('VAR', 'novalue')   # the good practice to have a fallback for missing value
# 'value'
ENV.get('VAR2', 'novalue')  # the good practice to have a fallback for missing value
# 'novalue'

'VAR' in ${...}   # Check environment variable exists
#True

${'V' + 'AR'}     # Get environment variable value by name from expression
#'value'

print($VAR)
with ${...}.swap(VAR='another value', NEW_VAR='new value'):  # Change VAR for commands block
    print($VAR)
print($VAR)
#value
#another value
#value

$VAR='new value' xonsh -c r'echo $VAR'   # Change variable for subprocess command
#new value

__xonsh__.env.get('VAR', 'novalue')  # the way to call environment using the __xonsh__ builtin
# 'value'
```

Python and subprocess mode:
```python
print("my home is $HOME")                        # Python mode
# my home is $HOME

print("my home is " + $HOME)                     # Python mode
# my home is /home/snail

echo "my home is $HOME" as well as '$HOME'       # Subprocess mode
# my home is /home/snail as well as /home/snail
```

Work with [`$PATH`](https://xon.sh/envvars.html#path):
```python
$PATH
# EnvPath(
# ['/usr/bin',
#  '/sbin',
#  '/bin']
# )

$PATH.add(p"~/bin", front=True, replace=True))   # Insert path '~/bin' at front of $PATH list and replace existing entries
$PATH.add(p"~/bin", front=True)                  # Insert path '~/bin' at front of $PATH list
$PATH.add(p"~/bin", front=False, replace=True))  # Insert path '~/bin' at end of $PATH list and replace existing entries
$PATH.insert(0, '/tmp')                          # Insert path '/tmp' at front of $PATH list
$PATH.append('/tmp')                             # Append path '/tmp' at end of $PATH list
$PATH.remove('/tmp')                             # Remove path '/tmp' (first match)
```

Setup local paths by prepending to path via a loop in `.xonshrc`:
```python
import os.path
from os import path
$user_bins = [
    f'{$HOME}/.cargo/bin',
    f'{$HOME}/.pyenv/bin',
    f'{$HOME}/.poetry/bin',
    f'{$HOME}/bin',
    f'{$HOME}/local/bin',
    f'{$HOME}/.local/bin', 
]

for dir in $user_bins:
    if path.isdir(dir) and path.exists(dir):
        $PATH.add(dir,front=True, replace=True)
```

See also the list of [xonsh default environment variables](http://xon.sh/envvars.html).

# [Aliases](https://xon.sh/tutorial.html#aliases)

## Simple aliases

```python
aliases['g'] = 'git status -sb'           # Add alias as string
aliases['e'] = 'echo @(2+2)'              # Add xonsh executable alias (ExecAlias)
aliases['gp'] = ['git', 'pull']           # Add alias as list of arguments
aliases['b'] = lambda: "Banana!\n"        # Add alias as simple callable lambda
aliases |= {'a': 'echo a', 'b':'echo b'}  # Add aliases from the dict
del aliases['b']                          # Delete alias
```

Easy wrapping a command by using [ExecAlias](https://xon.sh/tutorial.html#aliases) with built-in [`$args`](https://xon.sh/tutorial.html#aliases) (or `$arg0`, `$arg1`, etc) variable:

```python
aliases['echo-new'] = "echo @($args) new"
$(echo-new hello)
# 'hello new\n'
$(echo-new -n hello)
# 'hello new'
```

Also with handy `"""`-string to use `"` and `'` without escaping:

```python
aliases['scmd'] = """showcmd @([a for a in $args if a != "cutme"])"""

scmd
# usage: showcmd [-h|--help|cmd args]
# Displays the command and arguments as a list ...

scmd 1 2 cutme 3
#['1', '2', '3']
```

## [Callable aliases](https://xon.sh/tutorial.html#callable-aliases)

```python
def _myargs1(args):
#def _myargs2(args, stdin=None):
#def _myargs3(args, stdin=None, stdout=None):
#def _myargs4(args, stdin=None, stdout=None, stderr=None):
#def _myargs5(args, stdin=None, stdout=None, stderr=None, spec=None):
#def _myargs6(args, stdin=None, stdout=None, stderr=None, spec=None, stack=None):
    print(args)
    
aliases['args'] = _myargs1
del _myargs1

args 1 2 3
#['1', '2', '3']
```

Simple definition with [decorator](https://wiki.python.org/moin/PythonDecorators#What_is_a_Python_Decorator):
```xsh
@aliases.register("hello")
def __hello():
    echo world
    
hello
# world
```

Read stdin and write to stdout (real-life example - [xontrib-pipeliner](https://github.com/anki-code/xontrib-pipeliner)):
```python
def _exc(args, stdin, stdout):
    for line in stdin.readlines():
        print(line.strip() + '!', file=stdout, flush=True)

aliases['exc'] = _exc

echo hello | exc
# hello!
```
## Abbrevs

There is [xontrib-abbrevs](https://github.com/xonsh/xontrib-abbrevs) as alternative to aliases. You can create abbrev and set the position of editing:
```xsh
xpip install xontrib-abbrevs
xontrib load abbrevs

abbrevs['gst'] = 'git status'
gst  # Once you hit <space> or <return> 'gst' gets expanded to 'git status'.

abbrevs['gp'] = "git push <edit> --force"  # Set the edit position.
abbrevs['@'] = "@(<edit>)"  # Make shortcut.
abbrevs['...'] = "cd ../.."  # Workaround for syntax intersections with Python i.e. `elepsis` object from Python here.

# You can set a callback that receives current command buffer and word that triggered abbrev
abbrevs['*'] = lambda buffer, word: "asterisk" if buffer.text.startswith('echo') else word
ls *  # will stay
echo *  # will be transformed to `echo asterisk`
```

# [Path strings](https://xon.sh/tutorial.html#advanced-string-literals)

The p-string returns [Path object](https://docs.python.org/3/library/pathlib.html):

```python
path = p'~/.xonshrc'
path
# Path('/home/snail/.xonshrc')

[path.name, path.exists(), path.parent]
# ['.xonshrc', True, Path('/home/snail')]

[f for f in path.parent.glob('*') if 'xonsh' in f.name]
# [Path('/home/snail/.xonshrc')]

dir1 = 'hello'
dir2 = 'world'
path = p'/tmp' / dir1 / dir2 / 'from/dir' / f'{dir1}'
path
# Path('/tmp/hello/world/from/dir/hello')
```

A simple way to read and write the file content using Path string:

```python
text_len = p'/tmp/hello'.write_text('Hello world')
content = p'/tmp/hello'.read_text()
content
# 'Hello world'
```


# [Globbing](https://xon.sh/tutorial.html#normal-globbing) - get the list of files from path by mask or regexp
To [Normal globbing](https://xon.sh/tutorial.html#normal-globbing) add `g` before back quotes:
```python
ls *.*
ls g`*.*`

for f in gp`/tmp/*.*`:  # `p` is to return path objects
    print(f.name)
      
for f in gp`/tmp/*/**`:  # `**` is to glob subdirectories
    print(f)

```
To [Regular Expression Globbing](https://xon.sh/tutorial.html#regular-expression-globbing) add `r` before back quotes:
```python
ls `.*`
ls r`.*`

for f in rp`.*`:          # `p` is to return path instances
      print(f.exists())
```
To [Custom function globbing](https://xon.sh/tutorial.html#custom-path-searches) add `@` and the function name before back quotes:
```python
def foo(s):
    return [i for i in os.listdir('.') if i.startswith(s)]
cd /
@foo`bi`
#['bin']
```

# Macros

## [Simple macros](https://xon.sh/tutorial_macros.html#function-macros)

```python
def m(x : str):
    return x

# No macro calls:
[m('me'), m(42), m(m)]
# ['me', 42, <function __main__.m>]

# Macro calls:
[m!('me'), m!(42), m!(identity), m!(42), m!(  42 ), m!(import os)]
# ["'me'", '42', 'identity', '42', '42', 'import os']

m!(if True:
    pass)
# 'if True:\n    pass'
```

## [Subprocess Macros](https://xon.sh/tutorial_macros.html#subprocess-macros)

```python
echo! "Hello!"
# "Hello!"

bash -c! echo "Hello!"
# Hello!

docker run -it --rm xonsh/xonsh:slim xonsh -c! 2+2
# 4
```

Inside of a macro, all [additional munging](https://xon.sh/tutorial.html#string-literals-in-subprocess-mode) is turned off:

```python

echo $USER
# lou

echo! $USER
# $USER
```

## [Macro block](https://xon.sh/tutorial_macros.html#context-manager-macros)

### Builtin macro Block
```python
from xonsh.contexts import Block
with! Block() as b:
    qwe
    asd
    zxc

b.macro_block
# 'qwe\nasd\nzxc\n\n'
b.lines
# ['qwe', 'asd', 'zxc', '']
```

### Custom JSON block
```python
import json

class JsonBlock:
    __xonsh_block__ = str

    def __enter__(self):
        return json.loads(self.macro_block)

    def __exit__(self, *exc):
        del self.macro_block, self.macro_globals, self.macro_locals


with! JsonBlock() as j:
    {
        "Hello": "world!"
    }
    
j['Hello']
# world!
```

### Custom Docker block

The example is from [xontrib-macro-lib](https://github.com/anki-code/xontrib-macro-lib):

```python
from xonsh.contexts import Block

class Doxer(Block):
    """Run xonsh codeblock in docker container."""

    def __init__(self):
       self.docker_image = 'xonsh/xonsh:slim'

    def __exit__(self, *a, **kw):
        $[docker run -it --rm @(self.docker_image) /usr/local/bin/xonsh -c @(self.macro_block)]


with! Doxer() as d:
   pip install lolcat
   echo "We're in docker container now!" | lolcat
```

### Macro blocks library

See also [xontrib-macro-lib](https://github.com/anki-code/xontrib-macro-lib).

# [Tab-Completion](https://xon.sh/tutorial_completers.html)

```python
completer list  # List the active completers

# Create your own completer:
def dummy_completer(prefix, line, begidx, endidx, ctx):
    '''
    Completes everything with options "lou" and "carcolh",
    regardless of the value of prefix.
    '''
    return {"lou", "carcolh"}
    
completer add dummy dummy_completer  # Add completer: `completer add <NAME> <FUNC>`
# Now press Tab key and you'll get {"lou", "carcolh"} in completions
completer remove dummy
```

# Bind hotkeys in prompt toolkit shell

Uncover the power of [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit#python-prompt-toolkit) by [binding](https://xon.sh/tutorial_ptk.html) the [hotkeys](https://github.com/prompt-toolkit/python-prompt-toolkit/blob/master/src/prompt_toolkit/keys.py). Run this snippet or add it to `~/.xonshrc`:

```python
from prompt_toolkit.keys import Keys

@events.on_ptk_create
def custom_keybindings(bindings, **kw):

    # Press F1 and get the list of files
    @bindings.add(Keys.F1)
    def run_ls(event):
        ls -l
        event.cli.renderer.erase()
    
    # Press F3 to insert the grep command
    @bindings.add(Keys.F3)
    def say_hi(event):
        event.current_buffer.insert_text('| grep -i ')
        
```

# [Xontrib](https://xon.sh/tutorial_xontrib.html) - extension or plugin for xonsh

Xontrib lists: 
* [Github topic](https://github.com/topics/xontrib)
* [Github repositories](https://github.com/search?q=xontrib-&type=repositories)
* [awesome-xontribs](https://github.com/xonsh/awesome-xontribs)

To install xontribs xonsh has [`xpip`](https://xon.sh/aliases.html?highlight=aliases#xpip) - a predefined alias pointing to the pip command associated with the Python executable running this xonsh. Using `xpip` is the right way to install xontrib to be confident that the xontrib will be installed in the right environment.

If you want to create your own xontrib [using xontrib-template](https://github.com/xonsh/xontrib-template) is the best way:
```python
xpip install copier jinja2-time cookiecutter
copier gh:xonsh/xontrib-template .
```

# Xonsh Script (xsh)

Real-life example of xsh script that has: arguments, tab completion for arguments (using [xontrib-argcomplete](https://github.com/anki-code/xontrib-argcomplete)), subprocess calls with checking the result, colorizing the result and exit code:
```python
#!/usr/bin/env xonsh
# PYTHON_ARGCOMPLETE_OK                                  
import argparse
import argcomplete  # Tab completion support with xontrib-argcomplete
from argcomplete.completers import ChoicesCompleter

argp = argparse.ArgumentParser(description=f"Get count of lines in HTML by site address.")
argp.add_argument('--host', required=True, help="Host").completer=ChoicesCompleter(('xon.sh', 'github.com'))
argcomplete.autocomplete(argp)
args = argp.parse_args()

if result := !(curl -s -L @(args.host)):  # Python + Subprocess = ♥
    lines_count = len(result.out.splitlines())
    printx(f'{{GREEN}}Count of lines on {{#00FF00}}{args.host}{{GREEN}}: {{YELLOW}}{lines_count}{{RESET}}')
else:
    printx(f'{{RED}}Error while reading {{YELLOW}}{args.host}{{RED}}! {{RESET}}') # Colorizing messages
    exit(1)  # Exit with code number 1
```
Try it in action:
```python
xonsh
pip install argcomplete xontrib-argcomplete
xontrib load argcomplete
cd /tmp
wget https://raw.githubusercontent.com/anki-code/xonsh-cheatsheet/main/examples/host_lines.xsh
xonsh host_lines.xsh --ho<Tab>
xonsh host_lines.xsh --host <Tab>
xonsh host_lines.xsh --host xon.sh  # OR: chmod +x host_lines.xsh && ./host_lines.xsh --host xon.sh
# Count of lines on xon.sh: 568
```

# [History](https://xon.sh/tutorial_hist.html)

There are two history backends: `json` and [`sqlite`](https://xon.sh/tutorial_hist.html#sqlite-history-backend) which xonsh has by default. The `json` backend creates a json file with commands history on every xonsh session. The `sqlite` backend has one file with SQL-database.

We recommend using the `sqlite` backend because it saves the command on every execution, and querying of the history using SQL is very handy i.e. [history-search, history-pull](https://github.com/anki-code/xontrib-rc-awesome/blob/dfc9a8fc9a561b511262172c4ee58bd51dfc6b00/xontrib/rc_awesome.xsh#L158-L195).

```python
echo 123
# 123

__xonsh__.history[-1]
# HistoryEntry(cmd='echo 123', out='123\n', rtn=0, ts=[1614527550.2158427, 1614527550.2382812])

history info
# backend: sqlite
# sessionid: 637e577c-e5c3-4115-a3fd-99026f113464
# filename: /home/user/.local/share/xonsh/xonsh-history.sqlite
# session items: 2
# all items: 8533
# gc options: (100000, 'commands')

sqlite3 $XONSH_HISTORY_FILE  "SELECT inp FROM xonsh_history ORDER BY tsb LIMIT 1;"
# echo 123

aliases['history-search'] = """sqlite3 $XONSH_HISTORY_FILE @("SELECT inp FROM xonsh_history WHERE inp LIKE '%" + $arg0 + "%' AND inp NOT LIKE 'history-%' ORDER BY tsb DESC LIMIT 10");"""
cd /tmp
history-search "cd /"
# cd /tmp
history-search! cd /  # macro call
# cd /tmp

pip install sqlite_web
sqlite_web $XONSH_HISTORY_FILE  # Open the database in the browser

history pull  # Pull the history from parallel sessions and add to the current session. [xonsh -V > 0.13.4]
```

There is a third party history backend that's supplied in xontribs: [xontrib-history-encrypt](https://github.com/anki-code/xontrib-history-encrypt).

# [Interactive mode events](https://xon.sh/events.html)

When you're in xonsh interactive mode you can register an event, i.e.:

```python
@events.on_chdir
def mychdir(olddir, newdir, **kw):
    echo Jump from @(olddir) to @(newdir)
    
cd /tmp
# Jump from /home/snail to /tmp
```

# [Help](https://xon.sh/tutorial.html#help-superhelp-with)

Add `?` (regular help) or `??` (super help) to the command:

```python
ls?
# man page for ls

import json
json?
# json module help
json??
# json module super help
```

# Known issues and workarounds

### ModuleNotFoundError

Sometimes when you're using PyPi, Conda, or virtual environments you can forget about the current version and location of Python and try to import packages in xonsh resulting in a `ModuleNotFoundError` error. Often this means you installed the package in another environment and didn't realise it. To avoid this read the section about xonsh installation above.

### Intersection of console tools or shell syntax with Python builtins

In case of names or syntax intersection try to use aliases or [abbrevs](https://github.com/xonsh/xontrib-abbrevs) to resolve the conflict.

The case with `elepsis`:

```xsh
aliases['...'] = 'cd ../..'  # looks nice, but
...
# Elepsis

del aliases['...']
abbrevs['...'] = 'cd ../..'
...  # becomes `cd ../..`
```

The case with `import`:

```xsh
cd /tmp
$PATH.append('/tmp')
echo 'echo I am import' > import && chmod +x import

import  # Run subprocess `./import`
# I am import

import args  # Run Python import of `args` module
# ModuleNotFoundError: No module named 'args'

aliases['imp'] = "import"
imp
# I am import
```


### Frozen terminal in interactive tools

If you run a console tool and get a frozen terminal (Ctrl+c, Ctrl+d is not working) this can be that the tool was interpreted as threaded and capturable program but the tool actually has interactive elements that expect the input from the user. There are four workarounds now:

1. Disable [THREAD_SUBPROCS](https://xon.sh/envvars.html#thread-subprocs):

    ```python
    with ${...}.swap(THREAD_SUBPROCS=False):
          ./tool.sh
    ```

2. Run the tool in uncaptured mode:

    ```python
    $[./tool.sh]
    ```

3. Set the unthreadable predictor:

    ```python
    __xonsh__.commands_cache.threadable_predictors['tool.sh'] = lambda *a, **kw: False  # use the pure name of the tool
    ./tool.sh
    ```

4. Finally, check [`$XONSH_CAPTURE_ALWAYS`](https://xon.sh/envvars.html#xonsh-capture-always) value.

### Uncaptured output

If you want to capture the output of a tool but it's not captured, there are three workarounds:

1. Add the `head` tool at the end of the pipeline to force using the threadable mode:

    ```python
    !(echo 123 | head -n 1000)
    #CommandPipeline(
    #  returncode=0,
    #  output='123\n',
    #  errors=None
    #)
    ```

2. Change threading prediction for this tool:

    ```python
    __xonsh__.commands_cache.threadable_predictors['ssh'] = lambda *a, **kw: True

    !(ssh host -T "echo 1")
    #CommandPipeline(
    #  returncode=0,
    #  output='1\n',
    #  errors=None
    #)
    ```

3. Wrap the tool into a bash subprocess:

    ```python
    !(bash -c "echo 123")
    #CommandPipeline(
    #  returncode=0,
    #  output='123\n',
    #  errors=None
    #)
    ```

### [Bad file descriptor](https://github.com/xonsh/xonsh/issues/4224)

Using callable aliases in a long loop can cause the `Bad file descriptor` error to be raised. The workaround is to avoid using callable aliases in the loop and moving the code from callable alias directly into the loop or [marking the callable alias as unthreadable](https://xon.sh/tutorial.html#unthreadable-aliases):

```python
from xonsh.tools import unthreadable

@unthreadable
def _e():
    execx('echo -n 1')
aliases['e'] = _e

for i in range(100):
      e
```

# Tips and tricks

### Make your own installable xonsh RC file

Start by forking [xontrib-rc-awesome](https://github.com/anki-code/xontrib-rc-awesome).

### Using a text block in the command line

The first way is to use multiline strings:
```xsh
echo @("""
line 1
line 2
line 3
""".strip()) > file.txt

$(cat file.txt)
# 'line 1\nline 2\nline 3\n'
```
The second way is to use xonsh macro block via [xontrib-macro](https://github.com/anki-code/xontrib-macro):
```xsh
xpip install xontrib-macro

from xontrib.macro.data import Write

with! Write('/tmp/t/hello.xsh', chmod=0o700, replace=True, makedir=True, verbose=True):
    echo world
    
/tmp/t/hello.xsh
# world
```

Run commands in docker:
```python
docker run -it --rm xonsh/xonsh:slim xonsh -c @("""
pip install --disable-pip-version-check -q lolcat
echo "We're in docker container now!" | lolcat
""")
```
Don't forget that `Alt+Enter` can run the command from any place where cursor is.

### Ask to input argument and with autocomplete

```xsh
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

def ask(arg : str, completions : list = []):
    completer = WordCompleter(completions)
    session = PromptSession(completer=completer)
    user_input = session.prompt(f'{arg}: ')
    return user_input


echo I am saying @(ask('What to say'))
# What to say: hello
# I am saying hello

echo Give @(ask('Fruit', ['apple', 'banana', 'orange'])) to @(ask('To', [$(whoami).strip()]))
# Fruit: <Tab>
# Fruit: apple
# To: <Tab>
# To: user
# Give apple to user
```

### From the shell to REST API for one step

If you want to run shell commands from REST API you can create a [flask](https://flask.palletsprojects.com/) wrapper using [xontrib-macro](https://github.com/anki-code/xontrib-macro):
```xsh
xpip install flask xontrib-macro

cd /tmp

from xontrib.macro.data import Write
with! Write('myapi.xsh', chmod=0o700):
    import json
    from flask import Flask
    app = Flask(__name__)
    @app.route('/echo')
    def index():
        result = $(echo -n hello from echo)  # run subprocess command
        return json.dumps({'result': result})
    app.run()

./myapi.xsh
# Running on http://127.0.0.1:5000

curl http://127.0.0.1:5000/echo
# {"result": "hello from echo"}
```
Don't forget [about API security](https://flask-httpauth.readthedocs.io/en/latest/#basic-authentication-examples).

### Interactively debugging a script

If you want to have a breakpoint to debug a script, use the standard Python [pdb](https://docs.python.org/3/library/pdb.html):

```xsh
xpip install xontrib-macro
from xontrib.macro.data import Write
with! Write('/tmp/run.xsh', chmod=0o700, replace=True, makedir=True):
    echo hello
    $VAR = 1
    var = 2

    import pdb
    pdb.set_trace()   # interactive debug

    echo finish


xonsh /tmp/run.xsh
# hello
# > /tmp/run.xsh(9)<module>()
# -> echo finish
# (Pdb)

var
# 2

__xonsh__.env['VAR']
# 1

exit
# bdb.BdbQuit
```

### Using xonsh wherever you go through the SSH

You've stuffed your command shell with aliases, tools, and colors but you lose it all when using ssh. The mission of the [xxh project](https://github.com/xxh/xxh) is to bring your favorite shell wherever you go through ssh without root access or system installations.

### How to modify a command before execution?

To change the command between pressing enter and execution there is the [on_transform_command](https://xon.sh/events.html#on-transform-command) event:

```python
xpip install lolcat

@events.on_transform_command
def _(cmd, **kw):
    if cmd.startswith('echo') and 'lolcat' not in cmd:  
        # Be careful with the condition! The modified command will be passed 
        # to `on_transform_command` event again and again until the event 
        # returns the same command. Newbies can make a mistake here and
        # end up with unintended looping.
        return cmd.rstrip() + ' | lolcat'
    else:
        return cmd
        
echo 123456789 # <Enter>
# Execution: echo 123456789 | lolcat
```

### Comma separated thousands in output (custom formatter)

Here is a snippet from [@maxwellfire](https://github.com/maxwellfire):

```xsh
50000+50000
# 100000

500+500.123
# 1000.123

import xonsh.pretty
xonsh.pretty.for_type(type(1), lambda int, printer, cycle: printer.text(f'{int:,}'))
xonsh.pretty.for_type(type(1.0), lambda float, printer, cycle: printer.text(f'{float:,}'))

50000+50000
# 100,000

500+500.123
# 1,000.123
```

### `chdir` [context manager](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager) for scripting

```xsh
from xonsh.tools import chdir

cd /tmp
mkdir -p dir1

pwd
with chdir("./dir1"):
    pwd
pwd

# /tmp
# /tmp/dir1
# /tmp
```

### Juggling of exit code using python substitution

cd-ing into directory and if count of files less then 100 run `ls`:

```xsh
aliases['cdls'] = "cd @($arg0) && @(lambda: 1 if len(g`./*`) > 100 else 0) && ls"
cdls / && pwd
# bin dev etc ...
# /
cdls /usr/sbin && pwd
# /usr/sbin
```

### How to paste and edit multiple lines of code while in interactive mode

In some terminals (Konsole in Linux or Windows Terminal for WSL) you can press `ctrl-x ctrl-e` to open up an editor (`nano` in Linux) in the terminal session, paste the code there, edit and then quit out. Your multiple line code will be pasted and executed.

### Waiting for the job done
```python
sleep 100 &  # job 1
sleep 100 &  # job 2
sleep 100 &  # job 3

while $(jobs):
    time.sleep(1)

print('Job done!')
```

### How to trace xonsh code?

Trace with [hunter](https://github.com/ionelmc/python-hunter):

```python
pip install hunter
$PYTHONHUNTER='depth_lt=10,stdlib=False' $XONSH_DEBUG=1 xonsh -c 'echo 1'
```

Or try [xunter](https://github.com/anki-code/xunter) for tracing and profiling.

### From Bash to Xonsh

Read [Bash to Xonsh Translation Guide](https://xon.sh/bash_to_xsh.html), run `bash -c! echo 123` or install [xontrib-sh](https://github.com/anki-code/xontrib-sh).

### Xonsh and Windows

We recommend using [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/about) with [Manjaro](https://github.com/sileshn/ManjaroWSL2) (that maintains a [rolling release](https://en.wikipedia.org/wiki/Rolling_release)) on Windows. Don't forget to [fix PATH](https://github.com/xonsh/xonsh/issues/3895#issuecomment-713078931).

# Answers to the holy war questions

### Bash is everywhere! Why xonsh?

Python is everywhere as well ;)

### Xonsh is slower! Why xonsh?

You can spend significantly more time Googling and debugging sh-based solutions as well as significantly more time to make the payload work after running a command. Yeah, xonsh is a bit slower but you will not notice that in real life tasks :)

Also take a look:

* [Python 3.12: A Game-Changer in Performance and Efficiency](https://python.plainenglish.io/python-3-12-a-game-changer-in-performance-and-efficiency-8dfaaa1e744c)
* [Python 3.11 is up to 10-60% faster than Python 3.10](https://docs.python.org/3.11/whatsnew/3.11.html)
* [Making Python 5x FASTER with Guido van Rossum](https://www.youtube.com/watch?v=_r6bFhl6wR8).

### My fancy prompt in another shell is super duper! Why xonsh?

The fancy prompt is the tip of the iceberg. Xonsh shell brings other important features to love: [sane language](https://github.com/anki-code/xonsh-cheatsheet#basics), [powerful aliases](https://github.com/anki-code/xonsh-cheatsheet#aliases), [agile extensions](https://github.com/anki-code/xonsh-cheatsheet#xontrib---extension-or-plugin-for-xonsh), [history backends](https://github.com/anki-code/xonsh-cheatsheet#history), [fully customisable tab completion](https://github.com/anki-code/xonsh-cheatsheet#tab-completion), [magic macro blocks](https://github.com/anki-code/xonsh-cheatsheet#macro-block), [behaviour customisation via environment variables](https://xon.sh/envvars.html), and [more](https://github.com/anki-code/xonsh-cheatsheet#bind-hotkeys-in-prompt-toolkit-shell), and [more](https://github.com/anki-code/xonsh-cheatsheet#make-your-own-installable-xonsh-rc-file), and [more](https://github.com/anki-code/xonsh-cheatsheet#using-xonsh-wherever-you-go-through-the-ssh) :)

### Xonsh has issues! Why xonsh?

Compared to 15-20 year old shells, yeah, xonsh is a 5 year old youngster. But we've used it over these 5 years day by day to solve our tasks with success and happiness :)

# Thank you!

Thank you for reading! This cheatsheet is the tip of the iceberg of the xonsh shell and you can find more in the [official documentation](https://xon.sh/contents.html#guides).

Also you can install the cheatsheet xontrib:
```python
xpip install xontrib-cheatsheet
xontrib load cheatsheet
cheatsheet
# Opening: https://github.com/anki-code/xonsh-cheatsheet/blob/main/README.md
```

If you like the cheatsheet, click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=The%20xonsh%20shell%20cheat%20sheet.&url=https://github.com/anki-code/xonsh-cheatsheet" target="_blank">tweet</a>.

# Credits
* [Xonsh Tutorial](https://xon.sh/tutorial.html)
* Most copy-pastable examples prepared by [xontrib-hist-format](https://github.com/anki-code/xontrib-hist-format)
* The cheat sheet xontrib was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).
