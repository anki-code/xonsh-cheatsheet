<p align="center">
Cheat sheet for <a href="https://xon.sh">the xonsh shell</a> with copy-pastable examples. This is a good level of knowledge at start.
<br><br>
<img src="https://repository-images.githubusercontent.com/310804308/f11fa180-280d-11eb-8fa4-c389308692bd">
</p>

<p align="center">
If you like the cheatsheet click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=The%20xonsh%20shell%20cheat%20sheet.&url=https://github.com/anki-code/xonsh-cheatsheet" target="_blank">tweet</a>.
</p>

[Full screen reading](https://github.com/anki-code/xonsh-cheatsheet/blob/main/README.md)

# What does xonsh mean?

The "xonsh" word sounds like [conch [kɑːntʃ]](https://www.google.com/search?q=what+is+conch) - a common name of a number of different sea snail or shells (🐚). Thus xonsh is the reference to the shell word that commonly used to name [command shells](https://en.wikipedia.org/wiki/Shell_(computing)).

# Install xonsh

There are three ways to use xonsh:

1. **[Simple xonsh install](#simple-xonsh-install)**. You can install or using system installed Python to install xonsh and dependencies. We don't plan to understand Python version or virtual environments.

2. **[Install xonsh with package and environment management system](#install-xonsh-with-package-and-environment-management-system)**. In this way you can flexible manage Python version, dependencies and virtual environments but because of xonsh is a Python-based shell you have to understand what you're doing and the section below will uncover the cases. 

3. **[Try xonsh without installation](#try-xonsh-without-installation)**. Use Docker or Linux AppImage to run and try xonsh.

### Simple xonsh install

Most of the modern operating systems has [Python 3](https://www.python.org/) and [PyPi (pip)](https://packaging.python.org/tutorials/installing-packages/) that preinstalled or you can install it easily. By installing from PyPi you will get [the latest version of the xonsh shell](https://github.com/xonsh/xonsh/releases). We highly recommend to use `full` version of xonsh PyPi-package with [prompt-toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/) on board:
```xsh
python -m pip install 'xonsh[full]'
```

Another way is to install from package manager that supplied by operating system. This way is not recommended because in the operating systems without [rolling release concept](https://en.wikipedia.org/wiki/Rolling_release) the xonsh shell version may be very old ([check latest release](https://github.com/xonsh/xonsh/releases/)) because the average [release cycle for the xonsh shell](https://github.com/xonsh/xonsh/releases) is two months.

```xsh
# Not recommended but possible
apt install xonsh     # Debian/Ubuntu
pacman -S xonsh       # Arch Linux
dnf install xonsh     # Fedora
brew install xonsh    # OSX
```
Or on any system you can install `python` and then install xonsh from pip i.e. `any_pkg_manager install python && python -m pip install 'xonsh[full]'` - this is more preferable way.

### Install xonsh with package and environment management system

Because of xonsh is a Python-based shell you have to understand what you're doing and where. The common mistake is to expect that xonsh that was ran in one environment will work in another just after activation the new environment. But let's understand the case step by step.

#### How to understand the xonsh location

Before you will install and use xonsh with package manader and virtual environment you should remember how to detect python, xonsh and packages locations from current xonsh instance:

Where is Python:
```xsh
which python
# /opt/homebrew/bin/python

ls -la @$(which python)
# /opt/homebrew/bin/python -> ../Cellar/python@3.10/3.10.9/bin/python3
```

Where is xonsh and what version of Python used:
```xsh
which xonsh
# /opt/homebrew/bin/xonsh

head -n1 @$(which xonsh)
# #!/opt/homebrew/opt/python@3.10/bin/python3.10

python -V
# 3.10.9
```

Where is packages:
```xsh
import json
json
# <module 'json' from '/opt/homebrew/ ... /3.10/lib/python3.10/json/__init__.py'>
```

### Using xonsh with conda

** THIS SECTION UNDER CONSTRUCTION **

We will use [Conda](https://docs.conda.io/en/latest/) with [Conda-forge](https://conda-forge.org/) to demonstrate. You can carefully use [pipx](https://pypa.github.io/pipx/), [venv](https://docs.python.org/3/library/venv.html), [pyenv](https://github.com/pyenv/pyenv) as well. 


### Install xonsh on macOS or Linux

Following the article "[Installing Python on macOS without going insane](https://eddieantonio.ca/blog/2020/01/26/installing-python-on-macos/)":
```zsh
zsh  # Default macOS shell

# Install brew from https://brew.sh/
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install pyenv and then install Python
brew install pyenv
echo 'export PATH="$HOME/.pyenv/shims:$PATH"' >> ~/.zshrc
# restart zsh
pyenv install --list | grep ' 3.' | tail  # Choose the Python version
pyenv install 3.10.6
pyenv global 3.10.6

# The article recommend to use pipx to install global Python tools
brew install pipx  
pipx install 'xonsh[full]'

# Use xonsh `xpip` to install xontribs to appropriate packages location
xonsh
xpip install xontrib-prompt-bar xontrib-back2dir
```
On Mac we also recommend to install [GNU coreutils](https://www.gnu.org/software/coreutils/) to use the Linux default tools (i.e. `ls`, `grep`):
```xsh
brew install coreutils
$PATH.append('/opt/homebrew/opt/coreutils/libexec/gnubin')  # add to ~/.xonshrc
```

#### pipx and xonsh

The [pipx](https://pipxproject.github.io/pipx/) is also good to install xonsh in case you need certain Python version:
```xsh
# Install Python before continue
pip install pipx
pipx install --python python3.8 xonsh
pipx run xonsh 
# or add /home/$USER/.local/bin to PATH (/etc/shells) to running just `xonsh` command
```

### Try xonsh without installation

#### Docker

```python
# Docker with certain Python version and latest release of xonsh
docker run --rm -it python:3.9-slim /bin/bash \
 -c "pip install 'xonsh[full]' && xonsh"

# Docker with certain Python version and xonsh from the master branch
docker run --rm -it python:3.9-slim /bin/bash \
 -c "apt update && apt install -y git && pip install -U git+https://github.com/xonsh/xonsh && xonsh"

# Official xonsh docker image has old version
docker run --rm -it xonsh/xonsh:slim
```

#### Linux-portable AppImage contains both [Python 3 and xonsh in one file](https://xon.sh/appimage.html)

```python
wget https://github.com/xonsh/xonsh/releases/latest/download/xonsh-x86_64.AppImage -O xonsh
chmod +x xonsh
./xonsh

# Then if you don’t have Python on your host, you can acccess it from AppImage by running:
$PATH = [$APPDIR + '/usr/bin'] + $PATH
python -m pip install tqdm --user  # the `tqdm` package will be installed to ~/.local/
import tqdm
```

You can [build your own xonsh AppImage](https://xon.sh/appimage.html#building-your-own-xonsh-appimage) with packages you need in 15 minutes.

# Xonsh basics

The xonsh language is a superset of Python 3 with additional shell support. As result you can mix shell commands and Python code as easy as possible. Right off the bat examples:

```xsh
cd /tmp && ls                     # shell commands

21 + 21                           # python command

for i in range(0, 42):            # mix python 
    echo @(i+1)                   # and the shell

len($(curl https://xon.sh))       # mix python and the shell

$PATH.append('/tmp')              # using environment variables

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
# to convert your ~/.xonshrc into pip-installable package 
# with extesnsions you need on board.
```

## Three most frequent things that newcomers missed

### 1. [Shell commands also known as subprocess commands](https://xon.sh/tutorial.html#python-mode-vs-subprocess-mode)

The first thing you should remember that the shell commands are not the calls of another shell (i.e. bash). The xonsh has it's own parser implementation for subprocess commands and this is the cause why the command like `echo {1..5} \;` (brace expansion and escape character in bash) is not working. Most of sh-shell features [can be replaced](https://xon.sh/bash_to_xsh.html) by the sane Python alternatives and the example before will be solved by `echo @(range(1,6)) ';'`. 

If you think that only xonsh has the sh-uncompatible elements in the parser, you are tend to mistaken. If we compare Bash and Zsh we can found that `pip install package[subpackage]` command will work in Bash but in Zsh the error will be raised because Zsh has special mening for square braces. It's normal to have an evolution in the syntax and features. 

Be calm and ready to the sane and self-consistent Python-driven mindset.

*Note:* 
* *Most of novices try to copy and paste sh-lang commands that contains special characters and get the syntax error in xonsh. If you want to run environment agnostic sh-lang's command that you copy from the internet page just use macro call in xonsh `bash -c! echo {123}` or use [xontrib-sh](https://github.com/anki-code/xontrib-sh) to run context-free bash commands in xonsh by adding `! ` at the beginning of the command.*


### 2. [Strings and arguments in shell commands](https://xon.sh/tutorial_subproc_strings.html)

The second thing comes from the first. To escaping the special charecters, special meaning of braces or passing the string to the arguments use quotes. When in doubt, use quotes!

You should clearly understand the difference:

 <table style="width:100%">
  <tr>
    <th>sh-lang shells</th>
    <th>xonsh</th>
  </tr>
<tr>
<td>
1. Have escape character:
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
* *You can use `showcmd` command to show the arguments list:*    
    ```python
    showcmd echo The @('arguments') @(['list', 'is']) $(echo here) "and" --say="hello" to you
    # ['echo', 'The', 'arguments', 'list', 'is', 'here\n', 'and', '--say="hello"', 'to', 'you']]    
    ```


### 3. The process substitution operator `$()` returns output with [universal new lines](https://www.python.org/dev/peps/pep-0278/)

In sh-compatible shells the [process substitution operator](https://en.wikipedia.org/wiki/Process_substitution) `$()` executes the command and then split the output and use these parts as arguments. The command `echo $(echo -e "1 2\n3")` will have three distinct arguments `1`, `2` and `3` that will passed to the first `echo`.

In xonsh shell the `$()` operator returns the output of the command. The command `echo $(echo -e "1 2\n3")` will have one argument `1 2\n3\n` that will be passed to the first `echo`.

*Note:*
* *To make what sh-compatible shells are doing by `$()` operator the xonsh shell has `@$()` operator that will be described in the next chapter.*
    ```python
    showcmd echo @$(echo "1\n2 3\n4")
    # ['echo', '1', '2', '3', '4']
    ```
* *To transform output to the lines for the arguments list you can use [splitlines](https://docs.python.org/3/library/stdtypes.html#str.splitlines) function and the python substitution:*
    ```python
    showcmd echo @($(echo "1\n2 3\n4").splitlines())  # the first echo will get three arguments: "1", "2 3", "4"
    # ['echo', '1', '2 3', '4']
    ```
* *Not all xonsh users like this behavior of `$()` operator and in the future this may be changed. There are [the thread to discussing](https://github.com/xonsh/xonsh/issues/3924) this and the [Xonsh Enhancement Proposal #2](https://github.com/anki-code/xonsh-operators-proposal/blob/main/XEP-2.rst).*

# [Switching from `$` to `@`](https://github.com/xonsh/xonsh/issues/4152)

By default the xonsh shell has the bash-like appearance for the interactive prompt: `user@host ~ $`. After reading the previous section you can understand that we highly recommended to replace `$` to `@` by adding this line to your `~/.xonshrc` (or use [xontrib-prompt-bar](https://github.com/anki-code/xontrib-prompt-bar)):

```python
$PROMPT_FIELDS['prompt_end'] = '@'
```
Now the prompt appearance will be: `user@host ~ @`. This appearance will remind you of what you are in the xonsh shell. You can use [xontrib-sh](https://github.com/anki-code/xontrib-sh) to run sh-shell commands.

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

### `$[]` - not capturing (return `None`), print stdout and stderr

Passes stdout to the screen and returns `None`:

```python
ret = $[echo 123]
#123
repr(ret)
'None'
```

This is the same as `echo 123` but this syntax allows to explicitly run a subprocess command. 

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

This operator is used under the hood to running commands in the interactive xonsh prompt.

### `@()` - use Python code as an argument or a callable alias

Evaluates Python and pass the arguments:

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
This is mostly what bash's `$()` operator do.

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

Setup local paths for prepending to path by default via loop in `.xonshrc`:
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
aliases |= {'a': 'echo a', 'b':'echo b'}  # Add aliases from the list
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

Read stdin and write to stdout (real life example - [xontrib-pipeliner](https://github.com/anki-code/xontrib-pipeliner)):
```python
def _exc(args, stdin, stdout):
    for line in stdin.readlines():
        print(line.strip() + '!', file=stdout, flush=True)

aliases['exc'] = _exc

echo hello | exc
# hello!
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

Simple way to read and write the file content using Path string:

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

To install xontribs xonsh has [`xpip`](https://xon.sh/aliases.html?highlight=aliases#xpip) - a predefined alias pointing to the pip command associated with the Python executable running this xonsh. It's the right way to install xontrib via `xpip` to be confident that the xontrib will be installed in the right environment.

If you want to create your own xontrib [using xontrib-template](https://github.com/xonsh/xontrib-template) is the best way:
```python
pipx install copier
pipx inject copier jinja2-time
pipx inject copier cookiecutter

copier gh:xonsh/xontrib-template .
```

# Xonsh Script (xsh)

Real life example of xsh script that have: arguments, tab completion for arguments (using [xontrib-argcomplete](https://github.com/anki-code/xontrib-argcomplete)), subprocess calls with checking the result, colorizing the result and exit code:
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

There are two history backends: `json` and [`sqlite`](https://xon.sh/tutorial_hist.html#sqlite-history-backend) which xonsh has by default. The `json` backend creates json file with commands history on every xonsh session. The `sqlite` backend has one file with SQL-database.

We recommend to use `sqlite` backend because it saves the command on every execution and the querying of the history using SQL is very handy i.e. [history-search, history-pull](https://github.com/anki-code/xontrib-rc-awesome/blob/dfc9a8fc9a561b511262172c4ee58bd51dfc6b00/xontrib/rc_awesome.xsh#L158-L195).

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
sqlite_web $XONSH_HISTORY_FILE
# Open the database in the browser
```

There is third party history backends that's supplied as xontribs: [xontrib-history-encrypt](https://github.com/anki-code/xontrib-history-encrypt).

# [Interactive mode events](https://xon.sh/events.html)

When you're in xonsh interactive mode you can register an event i.e.:

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

# Known issues and workaround

### ModuleNotFoundError

Sometimes when you're using PyPi, Conda or virtual environments you can forget about current version and location of Python and try to import packages in xonsh with `ModuleNotFoundError` error. Ordinary you installed the package in other environment and didn't realise it. To solve this case there is [`xpip`](https://xon.sh/aliases.html#xpip) alias that you can use to install PyPi packages in the Python environment that was used to run current xonsh session.

The example of how to get the path to Python:
```python
# Getting current active Python version
python --version   # Python 3.8.5
which python       # /opt/miniconda3/bin/python
pip install tqdm   # Will be installed to /opt/miniconda3/lib

# Getting the Python version that used to run xonsh
import sys  
sys.executable                  # '/usr/bin/python'
@(sys.executable) --version     # Python 3.9.2
xpip install tqdm               # Will be installed to /usr/lib
```

### Freezed terminal in interactive tools

If you run the console tool and got the freezed terminal (Ctrl+c, Ctrl+d is not working) this looks like the tool was interpreted as threaded and capturable program but the tool has interactive elements that expect the input from the user. There are four workarounds now:

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

Finally check [`$XONSH_CAPTURE_ALWAYS`](https://xon.sh/envvars.html#xonsh-capture-always).

### Uncaptured output

If you want to capture the output of the tool but it's not captured there are three workarounds now:

1. Add the `head` tool at the end of pipe to force using the threadable mode:

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

3. Wrap the tool into bash subprocess:

    ```python
    !(bash -c "echo 123")
    #CommandPipeline(
    #  returncode=0,
    #  output='123\n',
    #  errors=None
    #)
    ```

### [Bad file descriptor](https://github.com/xonsh/xonsh/issues/4224)

In case of using callable aliases in the long loop the error `Bad file descriptor` will be raised. Workaround is to avoid using callable aliases in the loop and move the code from callable alias to the loop or [mark callable alias as unthreadable](https://xon.sh/tutorial.html#unthreadable-aliases):

```python
from xonsh.tools import unthreadable

@unthreadable
def _e():
    execx('echo -n 1')
aliases['e'] = _e

for i in range(100):
      e
```

### Unexpected issues around the [bashisms xontrib](https://xon.sh/xontribs.html#bashisms)

Sometimes [the bashisms xontrib](https://xon.sh/xontribs.html#bashisms) can be the cause of unexpected issues ([4250](https://github.com/xonsh/xonsh/issues/4250)). We recommend to avoid using this xontrib. Instead of trying to bring bash into xonsh we recommend to dive into xonsh. In case of you will need some bash syntax the best way is to implement this manually to have the clean understanding of what you do.

# Tips and tricks

### Make your own installable xonsh RC file

Start from fork [xontrib-rc-awesome](https://github.com/anki-code/xontrib-rc-awesome).

### Using text block in command line

Creating file:
```python
echo @("""
line 1
line 2
line 3
""".strip()) > file.txt

$(cat file.txt)
# 'line 1\nline 2\nline 3\n'
```

Run commands in docker:
```python
docker run -it --rm xonsh/xonsh:slim xonsh -c @("""
pip install --disable-pip-version-check -q lolcat
echo "We're in docker container now!" | lolcat
""")
```
Don't forget that `Alt+Enter` can run the command from any place where cursor is.

### Interactive debugging the script

If you want to have a breakpoint to debug the script use [pdb](https://docs.python.org/3/library/pdb.html):

```xsh

echo @("""
echo hello
$VAR = 1
var = 2

import pdb
pdb.set_trace()   # interactive debug

echo finish
""") > /tmp/run.xsh

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

You stuffed command shell with aliases, tools and colors but you lose it all when using ssh. The mission of [xxh project](https://github.com/xxh/xxh) is to bring your favorite shell wherever you go through the ssh without root access and system installations.

### How to modify command before execution?

To change the command between pressing enter and execution there is [on_transform_command](https://xon.sh/events.html#on-transform-command) event:

```python
xpip install lolcat

@events.on_transform_command
def _(cmd, **kw):
    if cmd.startswith('echo') and 'lolcat' not in cmd:  
        # Be careful with the condition! The modified command will be passed 
        # to `on_transform_command` event again and again until the event 
        # returns the same command. Newbies make a mistakes and facing with looping.
        return cmd.rstrip() + ' | lolcat'
    else:
        return cmd
        
echo 123456789 # <Enter>
# Execution: echo 123456789 | lolcat
```

### Comma separated thousands in output (custom formatter)

The snippet from [@maxwellfire](https://github.com/maxwellfire):

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
from contextlib import contextmanager

@contextmanager
def chdir(adir):
    old_dir = os.getcwd()
    os.chdir(adir)
    yield
    os.chdir(old_dir)
	
# --------------------------------------------

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

### How to paste and edit the multiple line of code being in interactive mode

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

### Copy current session commands to clipboard using [xclip](https://github.com/astrand/xclip)

```python
aliases['hist-to-clip'] = lambda: $[echo @('\n\n'.join([h.cmd for h in __xonsh__.history])) | xclip]
hist-to-clip
```

### How to trace the xonsh code?

Trace with [hunter](https://github.com/ionelmc/python-hunter):

```python
pip install hunter
$PYTHONHUNTER='depth_lt=10,stdlib=False' $XONSH_DEBUG=1 xonsh -c 'echo 1'
```
Or try [xunter](https://github.com/anki-code/xunter) for tracing and profiling.

### From Bash to Xonsh

Read [Bash to Xonsh Translation Guide](https://xon.sh/bash_to_xsh.html), run `bash -c! echo 123` or install [xontrib-sh](https://github.com/anki-code/xontrib-sh).

### Xonsh and Windows

We recommend to use [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/about) with [Manjaro](https://github.com/sileshn/ManjaroWSL2) (that supported [rolling release](https://en.wikipedia.org/wiki/Rolling_release)) on Windows. Don't forget to [fix PATH](https://github.com/xonsh/xonsh/issues/3895#issuecomment-713078931).

# Answers to the holy war questions

### Bash is everywhere! Why xonsh?

Python is everywhere as well ;)

### Xonsh is slower! Why xonsh?

Significant much more time you spending on Googling and debugging the sh-based solutions as well as significant much more time takes the payload work after running a command. Yeah, xonsh is a bit slower but you will not notice that in real life tasks :)

Also:
* [Making Python 5x FASTER with Guido van Rossum](https://www.youtube.com/watch?v=_r6bFhl6wR8).
* [Python 3.11 is up to 10-60% faster than Python 3.10](https://docs.python.org/3.11/whatsnew/3.11.html)

### My fancy prompt in other shell is super duper! Why xonsh?

The fancy prompt is the tip of the iceberg. We love the xonsh shell entirely: [sane language](https://github.com/anki-code/xonsh-cheatsheet#basics), [powerful aliases](https://github.com/anki-code/xonsh-cheatsheet#aliases), [agile extensions](https://github.com/anki-code/xonsh-cheatsheet#xontrib---extension-or-plugin-for-xonsh), [history backends](https://github.com/anki-code/xonsh-cheatsheet#history), [fully customisable tab completion](https://github.com/anki-code/xonsh-cheatsheet#tab-completion), [magic macro blocks](https://github.com/anki-code/xonsh-cheatsheet#macro-block), [behaviour customisation via environment variables](https://xon.sh/envvars.html) and [more](https://github.com/anki-code/xonsh-cheatsheet#bind-hotkeys-in-prompt-toolkit-shell), and [more](https://github.com/anki-code/xonsh-cheatsheet#make-your-own-installable-xonsh-rc-file), and [more](https://github.com/anki-code/xonsh-cheatsheet#using-xonsh-wherever-you-go-through-the-ssh) :)

### Xonsh has an issues! Why xonsh?

In comparing with the 15-20 years old shells yeah, xonsh is a 5 years old young man. But we use it for this 5 years day by day to solve our tasks with success and happiness :)

# Thank you!

Thank you for the reading! This cheatsheet is the tip of the iceberg of the xonsh shell and you can find more in the [official documentation](https://xon.sh/contents.html#guides).

Also you can install cheatsheet xontrib:
```python
xpip install -U git+https://github.com/anki-code/xonsh-cheatsheet
xontrib load cheatsheet
cheatsheet
# Opening: https://github.com/anki-code/xonsh-cheatsheet/blob/main/README.md
```

If you like the cheatsheet click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=The%20xonsh%20shell%20cheat%20sheet.&url=https://github.com/anki-code/xonsh-cheatsheet" target="_blank">tweet</a>.

# Credits
* [Xonsh Tutorial](https://xon.sh/tutorial.html)
* Most copy-pastable examples prepared by [xontrib-hist-format](https://github.com/anki-code/xontrib-hist-format)
* The cheat sheet xontrib was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).
