<p align="center">
Cheat sheet for <a href="https://xon.sh">the xonsh shell</a> with copy-pastable examples. This is a good level of knowledge at start.
</p>

<p align="center">
If you like the cheatsheet click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=The%20xonsh%20shell%20cheat%20sheet.&url=https://github.com/anki-code/xonsh-cheatsheet" target="_blank">tweet</a>.
</p>

[Full screen reading](https://github.com/anki-code/xonsh-cheatsheet/blob/main/README.md)

# Install xonsh or try without installation

### Recommended way to install xonsh

Most of the modern operating systems has [Python 3](https://www.python.org/) and [PyPi (pip)](https://packaging.python.org/tutorials/installing-packages/) that preinstalled or you can install it easily. This way is recommended, because you will get [the latest version of the xonsh shell](https://github.com/xonsh/xonsh/releases) from PyPi:
```python
python -m pip install 'xonsh[full]'
```

If you're using [Conda](https://docs.conda.io/en/latest/) the package from [Conda-forge](https://conda-forge.org/) is also fresh:
```python
conda config --add channels conda-forge && conda install xonsh
```

### Install from package managers

```python
apt install xonsh    # Debian/Ubuntu
dnf install xonsh    # Fedora
pacman -S xonsh      # Arch Linux
brew install xonsh   # OSX
```
*Note! In the operating systems without [rolling release concept](https://en.wikipedia.org/wiki/Rolling_release) the xonsh shell version may be very old because the average release cycle for the xonsh shell is one-two month.*

### Try without installation

Docker:

```python
docker run --rm -it xonsh/xonsh:slim

# Docker with certain Python version and latest release of xonsh
docker run --rm -it python:3.9-slim /bin/bash \
-c "pip install 'xonsh[full]' && xonsh"

# Docker with certain Python version and xonsh from the master branch
docker run --rm -it python:3.9-slim /bin/bash \
-c "apt update && apt install -y git && pip install -U git+https://github.com/xonsh/xonsh && xonsh"
```

Linux-portable AppImage contains both Python 3 and xonsh:

```python
wget https://github.com/xonsh/xonsh/releases/latest/download/xonsh-x86_64.AppImage -O xonsh
chmod +x xonsh
./xonsh

# Then if you don’t have Python on your host, you may want to get it from AppImage by running:
$PATH = [$APPDIR + '/usr/bin'] + $PATH
python -m pip install tqdm --user  # the `tqdm` package will be installed to ~/.local/
import tqdm
```

# Basics

The xonsh language is a superset of Python 3 with additional shell support. As result you can mix shell commands and Python code as easy as possible. Right off the bat examples:

```python
cd /tmp && ls                     # shell commands

21 + 21                           # python command

for i in range(0, 42):            # mix python 
    echo @(i+1)                   # and the shell

len($(curl https://xon.sh))       # mix python and the shell

$PATH.append('/tmp')              # using environment variables

for file in gp`*.*`:              # reading the list of files as Path-objects
    if file.exists():             # using rich functionality of Path-objects
        du -sh @(file)            # and pass it to the shell command
        
import json                       # python libraries are always at hand
if docker_info := $(docker info --format '{{json .}}'):
    print('ContainersRunning:', json.loads(docker_info)['ContainersRunning'])
        
```

## Three most frequent things that newcomers missed

### 1. [Shell commands as known as subprocess commands](https://xon.sh/tutorial.html#python-mode-vs-subprocess-mode)

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
1. No escape character - use quotes:
<pre>
<b>echo "123 456"</b>
# 123 456
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
    echo @$(echo "1\n2 3\n4")  # the first echo will get four arguments: "1", "2", "3", "4"
    ```
* *To transform output to the lines for the arguments list you can use [splitlines](https://docs.python.org/3/library/stdtypes.html#str.splitlines) function and the python substitution:*
    ```python
    echo @($(echo "1\n2 3\n4").splitlines())  # the first echo will get three arguments: "1", "2 3", "4"
    ```
* *Not all xonsh users like this behavior of `$()` operator and in the future this may be changed. There are [the thread to discussing](https://github.com/xonsh/xonsh/issues/3924) this and the [Xonsh Enhancement Proposal #2](https://github.com/anki-code/xonsh-operators-proposal/blob/main/XEP-2.rst).*

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

# Environment Variables

```python
$VAR = 'value'    # Set environment variable

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
```

Python and subprocess mode:
```python
print("my home is $HOME")   # Python mode
# my home is $HOME

print("my home is " + $HOME)   # Python mode
# my home is /home/snail

echo "my home is $HOME" as well as '$HOME'     # Subprocess mode
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

$PATH.insert(0, '/tmp')  # Add first path to $PATH list
$PATH.append('/tmp')  # Add last path to $PATH list
$PATH.remove('/tmp')  # Remove path (first match)
```

See also the list of [xonsh default environment variables](http://xon.sh/envvars.html).

# [Aliases](https://xon.sh/tutorial.html#aliases)

## Simple alias

```python
aliases['g'] = 'git status -sb'           # Add alias as string
aliases['e'] = 'echo @(2+2)'              # Add xonsh executable alias (ExecAlias)
aliases['gp'] = ['git', 'pull']           # Add alias as list of arguments
aliases['b'] = lambda: "Banana!\n"        # Add alias as simple callable lambda
aliases |= {'a': 'echo a', 'b':'echo b'}  # Add aliases from the list
del aliases['b']                          # Delete alias
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
The same but as lambda:
```python
showcmd 1 2 3
#['1', '2', '3']
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
Inside of a macro, all additional munging is turned off:
```

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

You can wrap existing completers. For example if you want to remove `../` and `./` from the completion list for the `cd` command add this to `~/.xonshrc`:

```python
from xonsh.completers.dirs import complete_cd
def _complete_smart_cd(prefix, line, start, end, ctx):
    """Completion for "cd" without `../` and `./`."""
    if comp := complete_cd(prefix, line, start, end, ctx):
        paths, lprefix = comp
    else:
        return
    new_paths = {p for p in paths if p not in ['../', './']}
    return (new_paths, lprefix)

completer add smart_cd _complete_smart_cd ">cd"  # ">cd" means add the completer after the existing `cd` completer
completer remove cd
```

# [Xontrib](https://xon.sh/tutorial_xontrib.html) - extension or plugin for xonsh

Xontrib lists: [github topic](https://github.com/topics/xontrib), [github repos](https://github.com/search?q=xontrib-&type=repositories), [official list](https://xon.sh/xontribs.html).

Create xontrib [using cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter):
```python
pip install cookiecutter
cookiecutter gh:xonsh/xontrib-cookiecutter
```

# Xonsh Script (xsh)

Real life example of xsh script that have: arguments, tab completion for arguments, subprocess calls with checking the result, colorizing the result and exit code:
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

There are two history backends: `json` and `sqlite` which xonsh has by default. The `json` backend creates json file with commands history on every xonsh session. The `sqlite` backend has one file with SQL-database.

There is third party history backends that's supplied as xontribs: [xontrib-history-encrypt](https://github.com/anki-code/xontrib-history-encrypt).

```python
echo 123
# 123

__xonsh__.history[-1]
# HistoryEntry(cmd='echo 123', out='123\n', rtn=0, ts=[1614527550.2158427, 1614527550.2382812])

history info
# backend: sqlite
# sessionid: 637e577c-e5c3-4115-a3fd-99026f113464
# filename: /home/user/.local/share/xonsh/xonsh-history.sqlite
# session items: 39
# all items: 8533
# gc options: (100000, 'commands')
```

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

### Freezed terminal in some apps

If you run the console tool and got the freezed terminal (Ctrl+c, Ctrl+d is not working) try to disable [THREAD_SUBPROCS](https://xon.sh/envvars.html#thread-subprocs) for this tool:
```python
with ${...}.swap(THREAD_SUBPROCS=False):
      ./tool.sh
```

### Uncaptured pipe

If you're trying to run the pipe `cat file | some_tool` and the captured output is empty or freez try to add `cat` or `head` to the end of pipe i.e. `cat file | some_tool | head`.

# Tips and tricks

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

### Using xonsh wherever you go through the SSH

You stuffed command shell with aliases, tools and colors but you lose it all when using ssh. The mission of [xxh project](https://github.com/xxh/xxh) is to bring your favorite shell wherever you go through the ssh without root access and system installations.

### How to modify command before execution?

To change the command between pressing enter and execution there is [on_transform_command](https://xon.sh/events.html#on-transform-command) event:

```python
pip install lolcat

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

### How to paste and edit the multiple line of code being in interactive mode

In some terminals (i.e. Konsole) you can press `ctrl-x ctrl-e` to open up an editor in the terminal session, paste the code there, edit and then quit out. Your multiple line code will be pasted.

### How to get stack trace without `__amalgam__`?

Run xonsh in debug mode:
```python 
bash
XONSH_DEBUG=1 XONSH_SHOW_TRACEBACK=1 xonsh
```

### Waiting for the job done
```python
sleep 100 &  # job 1
sleep 100 &  # job 2
sleep 100 &  # job 3

while $(jobs):
    time.sleep(1)

print('Job done!')
```

### Copy current session commands to clipboard using xclip

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

# Answers to the holy war questions

### Bash is everywhere! Why xonsh?

Python is everywhere as well ;)

### Xonsh is slower! Why xonsh?

Significant much more time you spending on Googling and debugging the sh-based solutions as well as significant much more time takes the payload work after running a command. Yeah, xonsh is a bit slower but you will not notice that in real life tasks :)

### My fancy prompt in other shell is super duper! Why xonsh?

The fancy prompt is the tip of the iceberg. You are still living in the 90th with the sh-syntax language. We love the xonsh shell entirely: sane language, powerful aliases, agile extensions, history backends, fully customisable tab completion, magic macro blocks, behaviour customisation via environment variables and more, and more, and more :)

### Xonsh has an issues! Why xonsh?

In comparing with the 15-20 years old shells yeah, xonsh is a 5 years old young man. But we use it for this 5 years day by day to solve our tasks with success and happiness :)

# Thank you!

Thank you for the reading! This cheatsheet is the tip of the iceberg of the xonsh shell and you can find more in the [official documentation](https://xon.sh/contents.html#guides).

If you like the cheatsheet click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=The%20xonsh%20shell%20cheat%20sheet.&url=https://github.com/anki-code/xonsh-cheatsheet" target="_blank">tweet</a>.

# Credits
* [Xonsh Tutorial](https://xon.sh/tutorial.html)
* Most copy-pastable examples prepared by [xontrib-hist-format](https://github.com/anki-code/xontrib-hist-format)
