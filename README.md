<p align="center">
Cheat sheet for xonsh shell with copy-pastable examples. This is a good level of knowledge for any xonsh users.
</p>

<p align="center">
If you like the cheatsheet click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=The%20xonsh%20shell%20cheat%20sheet.&url=https://github.com/anki-code/xonsh-cheatsheet" target="_blank">tweet now</a>.
</p>

# Install xonsh or try without installation
Installation methods:
```python
pip install xonsh  # PyPi

conda config --add channels conda-forge && conda install xonsh  # Conda

apt install xonsh    # Debian/Ubuntu
dnf install xonsh    # Fedora
pacman -S xonsh      # Arch Linux
brew install xonsh   # OSX
```
Try without installation:
```python
docker run -it --rm xonsh/xonsh:slim  # Docker
```
```python
# Linux portable xonsh AppImage
wget https://github.com/xonsh/xonsh/releases/latest/download/xonsh-x86_64.AppImage -O xonsh
chmod +x xonsh
./xonsh
```

# Basics

The xonsh language is a superset of Python 3 with additional shell primitives. As result you can mix shell commands and Python code as easy as possible.

Right off the bat examples:

```python
cd /tmp && ls

for i in range(0, 42):
    echo @(i+1)

len($(curl https://xon.sh))

import json
docker_network_id = '1c04fa7dbb06'
network_config = json.loads( $(docker network inspect @(docker_network_id)) )[0]

21 + 21

$PATH.append('/tmp')

for file in gp`*.*`:
    if file.exists():
        du -sh @(file)
```

## Three most frequent things that newcomers missed

### 1. [Python and Subprocess](https://xon.sh/tutorial.html#python-mode-vs-subprocess-mode)

The first thing you should remember that there is Python and subprocess commands:

```python
echo -n Hello   # Subprocess command: running `echo` tool with two arguments: `-n` and `Hello`
2 + 2           # Python command
import json     # Python command

for i in range(0, 42):  # Python
    echo @(i)           # Subprocess: run `echo` with the Python variable `i` as an argument
    i += 1              # Python
    ![echo @(i)]        # Explicit way to run subprocess command
    
html = $(curl https://xon.sh)  # Python command where called captured subprocess command
```

The subprocess commands are not the calls of another shell (i.e. bash). The xonsh has it's own parser implementation for subprocess commands and this is the cause why the commands like `echo {1..5}` (brace expansion in bash) is not working and should be implemented using xonsh parser. Most of [bash features could be replaced by the Python alternatives](https://xon.sh/bash_to_xsh.html) and the example before will be solved by `echo @(range(1,6))`. Be calm and ready to the new Python-driven mindset.

### 2. [Strings and arguments in subprocess commands](https://xon.sh/tutorial_subproc_strings.html)

The second thing you should remember that xonsh syntax for subprocess commands is very [self-consistent](https://xon.sh/tutorial_subproc_strings.html) but it's differ than sh-lang. If you use arguments with quotes or brackets you should clearly understand the difference:

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

The golden rule for xonsh: When in doubt in subprocess mode, use quotes!

Most of novices try to copy and paste sh-lang commands that contains special characters and get the syntax error in xonsh. If you want to run environment agnostic sh-lang's command that you copy from the internet page just use macro call in xonsh:
```python
bash -c! echo {123}
```

### 3. The process substitution operator `$()` returns string

In sh-compatible shells the [process substitution operator](https://en.wikipedia.org/wiki/Process_substitution) `$()` executes the command and then split the output and use these parts as arguments. The command `echo $(echo -e "1 2\n3")` will have three distinct arguments `1`, `2` and `3` that will passed to the first `echo`.

In xonsh shell the `$()` operator returns the output of the command. The command `echo $(echo -e "1 2\n3")` will have one argument `1 2\n3\n` that will be passed to the first `echo`.

*Notes:*
* *To make what sh-compatible shells are doing by `$()` operator the xonsh shell has `@$()` operator that will be described in the next chapter.*
* *Not all xonsh users like this behavior of `$()` operator and in the future this may be changed. There are [the thread to discussing](https://github.com/xonsh/xonsh/issues/3924) this and the [Xonsh Enhancement Proposal #2](https://github.com/anki-code/xonsh-operators-proposal/blob/main/XEP-2.rst).*

# [Operators](https://xon.sh/tutorial.html#captured-subprocess-with-and)

### `$()` - capture and return output without printing stdout and stderr

Captures stdout and returns output with [universal new lines](https://www.python.org/dev/peps/pep-0278/):
```python
aliases['args'] = lambda args: print(args)

args $(echo -e '1\n2\r3 4\r\n5')       # Subproc mode
# ['1\n2\n3 4\n5\n']

output = $(echo -e '1\n2\r3 4\r\n5')   # Python mode 
output
# '1\n2\n3 4\n5\n'
```

### `!()` - capture all and return object without printing stdout and stderr

Captures stdout and returns [CommandPipeline](http://xon.sh/api/proc.html#xonsh.proc.CommandPipeline). Truthy if successful (returncode == 0), compares to, iterates over lines of stdout:
  
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

Passes stdout to the screen and returns [HiddenCommandPipeline](https://xon.sh/api/proc.html#xonsh.proc.HiddenCommandPipeline):

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
aliases['args'] = lambda args: print(args)

args 'Supported:' @('string') @(['list','of','strings']) 
#['Supported:', 'string', 'list', 'of', 'strings']

echo -n '!' | @(lambda args, stdin: 'Callable' + stdin.read())
#Callable!
```

### `@$()` - split output of the command by white spaces for arguments list

```python
aliases['args'] = lambda args: print(args)

args @$(echo -e '1\n2\r3 4\r\n5')
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
# Add alias as string
aliases['g'] = 'git status -sb'

# Add alias as list
aliases['gp'] = ['git', 'pull']

# Add alias as simple callable lambda
aliases['banana'] = lambda: "Banana for scale.\n"

# Delete alias
del aliases['banana']

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
aliases['args'] = lambda args: print(args)

args 1 2 3
#['1', '2', '3']
```


# [Globbing](https://xon.sh/tutorial.html#normal-globbing) - get the list of files from path by mask or regexp
To [Normal globbing](https://xon.sh/tutorial.html#normal-globbing) add `g` before back quotes:
```python
ls *.*
ls g`*.*`

for f in gp`.*`:          # `p` is to return path instances
      print(f.exists())
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

# Shell syntax

## [Input/Output Redirection](https://xon.sh/tutorial.html#input-output-redirection)

```python
# Redirect stdout
COMMAND > output.txt
COMMAND out> output.txt
COMMAND o> output.txt
COMMAND 1> output.txt # included for Bash compatibility

# Redirecting stderr
COMMAND err> errors.txt
COMMAND e> errors.txt
COMMAND 2> errors.txt # included for Bash compatibility

# Redirecting all stdout and stderr
COMMAND all> combined.txt
COMMAND a> combined.txt
COMMAND &> combined.txt # included for Bash compatibility

# Merge stderr into stdout - error messages are reported to the same location as regular output
COMMAND err>out
COMMAND err>o
COMMAND e>out
COMMAND e>o
COMMAND 2>&1  # included for Bash compatibility

# Merge can be combined with other redirections
COMMAND err>out | COMMAND2
COMMAND e>o > combined.txt

# Redirecting stdin
COMMAND < input.txt
< input.txt COMMAND

# Combining I/O Redirects
# This line will run COMMAND1 with the contents of input.txt fed in on stdin, 
# and will pipe all output (stdout and stderr) to COMMAND2; 
# the regular output of this command will be redirected to output.txt, 
# and the error output will be appended to errors.txt.
COMMAND1 e>o < input.txt | COMMAND2 > output.txt e>> errors.txt
```

## [Background Jobs](https://xon.sh/tutorial.html#background-jobs)
```python
# Run command in background 
sleep 30 &
sleep 31 &
sleep 32 &

# List of jobs
jobs
# [4]+ running: sleep 32 & & (15644)
# [3]- running: sleep 31 & & (15640)
# [2]  running: sleep 30 & & (15636)
```

# [String Literals in Subprocess-mode](https://xon.sh/tutorial.html#string-literals-in-subprocess-mode)

Simple example:

```python
print("my home is $HOME")   # Python mode
# my home is $HOME

echo "my home is $HOME"     # Subprocess mode
# my home is /home/snail
```

For the fine control of environment variables (envvar) substitutions, brace substitutions and backslash escapes there are extended list of literals:

* **`"foo"`**: Regular string: backslash escapes
* **`f"foo"`**: Formatted string: brace substitutions, backslash escapes
* **`r"foo"`**: Raw string: unmodified
* **`p"foo"`**: Path string: backslash escapes, envvar substitutions, returns `Path`
* **`pr"foo"`**: Raw Path string: envvar substitutions, returns `Path`
* **`pf"foo"`**: Formatted Path string: backslash escapes, brace substitutions, envvar substitutions, returns `Path`
* **`fr"foo"`**: Raw Formatted string: brace substitutions

To complete understanding let’s set environment variable `$EVAR` to `1` and local variable `var` to `2` and make a table that shows how literal changes the string in Python- and subprocess-mode:

|         String literal      |      As python object       | print([String literal]) |  echo [String literal] |
|    ------------------------ |  -------------------------- | ----------------------- | ---------------------  |
|    `"/$EVAR/\'{var}\'"`   | `"/$EVAR/'{var}'"`        | `/$EVAR/'{var}'`      | `/1/'{var}'`         |
|    `r"/$EVAR/\'{var}\'"`  | `"/$EVAR/\\'{var}\\'"`    | `/$EVAR/\'{var}\'`    | `/$EVAR/\'{var}\'`   |
|    `f"/$EVAR/\'{var}\'"`  | `"/$EVAR/'2'"`            | `/$EVAR/'2'`          | `/1/'2'`             |
|    `fr"/$EVAR/\'{var}\'"` | `"/$EVAR/\\'2\\'"`        | `/$EVAR/\'2\'`        | `/$EVAR/\'2\'`       |
|    `p"/$EVAR/\'{var}\'"`  | `Path("/1/'{var}'")`      | `/1/'{var}'`          | `/1/'{var}'`         |
|    `pr"/$EVAR/\'{var}\'"` | `Path("/1/\\'{var}\\'")`  | `/1/\'{var}\'`        | `/1/\'{var}\'`       |
|    `pf"/$EVAR/\'{var}\'"` | `Path("/1/'2'")`          | `/1/'2'`              | `/1/'2'`             |


# Macros

## [Simple macros](https://xon.sh/tutorial_macros.html#function-macros)

```python
def identity(x : str):
    return x

# No macro calls:

identity('me')
# 'me'
identity(42)
# 42
identity(identity)
# <function __main__.identity>

# Macro calls:

identity!('me')
# "'me'"
identity!(42)
# '42'
identity!(identity)
# 'identity'
identity!(42)
# '42'
identity!(  42 )
# '42'
identity!(import os)
# 'import os'

identity!(if True:
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

### Custom JsonBlock
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

# Tips and tricks

### Create file with content from command line
```python
echo @("""
line 1
line 2
line 3
""".strip()) > file.txt

$(cat file.txt)
# 'line 1\nline 2\nline 3\n'
```

### From Bash to Xonsh

* [Bash to Xonsh Translation Guide](https://xon.sh/bash_to_xsh.html) - This is the must read.
* [xontrib-sh](https://github.com/anki-code/xontrib-sh) - Paste and run commands from bash, fish, zsh, tcsh in xonsh shell. 
* `bash -c! echo 123` - The way to run bash command line using macro syntax.

### Using xonsh wherever you go through the SSH

You stuffed command shell with aliases, tools and colors but you lose it all when using ssh. The mission of [xxh project](https://github.com/xxh/xxh) is to bring your favorite shell wherever you go through the ssh without root access and system installations.

## How to paste and edit the multiple line of code being in interactive mode

In some terminals (i.e. Konsole) you can press `ctrl-x ctrl-e` to open up an editor in the terminal session, paste the code there, edit and then quit out. Your multiple line code will be pasted.

### How to get stack trace without `__amalgam__`?

Run xonsh in debug mode:
```python 
XONSH_DEBUG=1 XONSH_SHOW_TRACEBACK=1 xonsh
```

# Credits
* [Xonsh Tutorial](https://xon.sh/tutorial.html)
* Most copy-pastable examples prepared by [xontrib-hist-format](https://github.com/anki-code/xontrib-hist-format)
