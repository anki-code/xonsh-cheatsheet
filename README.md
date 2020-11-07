<p align="center">
Cheat sheet for xonsh shell with copy-pastable examples.
</p>

<p align="center">
If you like the cheatsheet click ⭐ on the repo and stay tuned.
</p>

<p align="center">
Work in progress. PRs are welcome.
</p>

# Basics
Xonsh supports Python and shell commands:
```python
2 + 2
# 4

ls / | head -n 5
# boot cdrom dev etc home
```

# Operators

**`$()`** - captures stdout and returns output with [universal new lines](https://www.python.org/dev/peps/pep-0278/):
```python
aliases['args'] = lambda args: print(args)

args $(echo -e '1\n2\r3 4\r\n5')       # Subproc mode
#['1\n2\n3 4\n5\n']

output = $(echo -e '1\n2\r3 4\r\n5')   # Python mode 
output
#'1\n2\n3 4\n5\n'
```

**`!()`** - captures stdout and returns [CommandPipeline](http://xon.sh/api/proc.html#xonsh.proc.CommandPipeline)
  (Truthy if successful, compares to integers, iterates over lines of stdout):
  
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

**`$[]`** - passes stdout to the screen and returns `None`.

```python
ret = $[echo 123]
#123
repr(ret)
'None'
```

**`![]`**:  - passes stdout to the screen and returns [HiddenCommandPipeline](https://xon.sh/api/proc.html#xonsh.proc.HiddenCommandPipeline)

```python
ret = ![echo -e '1\n2\r3 4\r\n5']
#1
#3 4
#5
ret               # No representation, no return value because it's hidden CommandPipeline object
ret.out           # But it has the properties from CommandPipeline
'1\n2\r3 4\n5\n'
```

**`@()`** - evaluates Python and pass the arguments. 

```python
aliases['args'] = lambda args: print(args)

args 'Supported:' @('string') @(['list','of','strings']) 
#['Supported:', 'string', 'list', 'of', 'strings']

echo -n '!' | @(lambda args, stdin: 'Callable in the same form as callable aliases'+ stdin.read())
#Callable in the same form as callable aliases!!!
```

**`@$()`** - split output of the command by whitespaces:
```python
aliases['args'] = lambda args: print(args)

args @$(echo -e '1\n2\r3 4\r\n5')
#['1', '2\r3', '4', '5']
```

# Environment Variables
* **`$VAR`**: Get the env var `VAR`
* **`${...}`**: Get the entire environment (as a dict like object)
* **`${'V'+'AR'}`**: Get the env var from an expression (eg, `VAR`)
* [Xonsh Environment Variables](http://xon.sh/envvars.html) list

## Shell syntax
* **`|`**: Shell-style pipe
* **`and`**, **`or`**: Logically joined commands, lazy
* **`&&`**, **`||`**: Same
* **`COMMAND &`**: Background into job (May use `jobs`, `fg`, `bg`)
* **`>`**: Write (stdout) to
* **`>>`**: Append (stdout) to
* **`</spam/eggs`**: Use file for stdin
* **`out`**, **`o`**
* **`err`**, **`e`**
* **`all`**, **`a`** (left-hand side only)

```
>>> COMMAND1 e>o < input.txt | COMMAND2 > output.txt e>> errors.txt
```

# [Advanced String Literals](https://xon.sh/tutorial.html#advanced-string-literals)

* **`"foo"`**: Regular string: backslash escapes
* **`f"foo"`**: Formatted string: brace substitutions, backslash escapes
* **`r"foo"`**: Raw string: unmodified
* **`p"foo"`**: Path string: backslash escapes, envvar substitutions, returns `Path`
* **`pr"foo"`**: Raw Path string: envvar substitutions, returns `Path`
* **`pf"foo"`**: Formatted Path string: backslash escapes, brace substitutions, envvar substitutions, returns `Path`
* **`fr"foo"`**: Raw Formatted string: brace substitutions

# [Globbing](https://xon.sh/tutorial.html#normal-globbing)
[Normal globbing](https://xon.sh/tutorial.html#normal-globbing):
```python
ls *.*
# or
ls g`*.*`
# or return path instances:
for f in gp`.*`:
      print(f.exists())
```
[Regular Expression Globbing](https://xon.sh/tutorial.html#regular-expression-globbing):
```python
ls `.*`
# or
ls r`.*`
# or return path instances:
for f in rp`.*`:
      print(f.exists())
```
[Custom function globbing](https://xon.sh/tutorial.html#custom-path-searches):
```python
def foo(s):
    return [i for i in os.listdir('.') if i.startswith(s)]
cd /
@foo`bi`
#['bin']
```

# [Aliases](https://xon.sh/tutorial.html#aliases)
* `aliases['g'] = 'git status -sb'`
* `aliases['gp'] = ['git', 'pull']`

# [Callable aliases](https://xon.sh/tutorial.html#callable-aliases)

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
or:
```python
aliases['args'] = lambda args: print(args)

args 1 2 3
#['1', '2', '3']
```

# Xonsh Scripts (xsh)
* **`$ARGS`**: List of all command line parameter arguments.
* **`$ARG0`, `$ARG1`, ... `$ARG9`**: Script command line argument at index n.

# Xontribs
Xontrib list: [github topic](https://github.com/topics/xontrib), [github repos](https://github.com/search?q=xontrib-&type=repositories), [official list](https://xon.sh/xontribs.html).

Create xontrib [using cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter):
```
pip install cookiecutter
cookiecutter gh:xonsh/xontrib-cookiecutter
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

# Credits
* [Xonsh Tutorial](https://xon.sh/tutorial.html)
* Most copy-pastable examples prepared by [xontrib-hist-format](https://github.com/anki-code/xontrib-hist-format)
* The first short version of the cheat sheet was made by @AstraLuma. Thanks!
