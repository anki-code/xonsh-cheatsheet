<p align="center">
Cheatsheet for xonsh shell.
</p>

<p align="center">
If you like the cheatsheet click ⭐ on the repo and stay tuned.
</p>

<p align="center">
Work in progress. PRs are welcome.
</p>

# Environment Variables
* **`$VAR`**: Get the env var `VAR`
* **`${...}`**: Get the entire environment (as a dict like object)
* **`${'V'+'AR'}`**: Get the env var from an expression (eg, `VAR`)
* [Xonsh Environment Variables](http://xon.sh/envvars.html) list

# Xonsh Scripts (xsh)
* **`$ARGS`**: List of all command line parameter arguments.
* **`$ARG0`, `$ARG1`, ... `$ARG9`**: Script command line argument at index n.

# Subprocess

* **`$()`**: Captures output, returns stdout
* **`!()`**: Captures output, returns [CommandPipeline](http://xon.sh/api/proc.html#xonsh.proc.CommandPipeline)
  (Truthy if successful, compares to integers, iterates over lines of stdout)
* **`$[]`**: Output passed, returns `None`
* **`![]`**: Output passed, returns [CommandPipeline](http://xon.sh/api/proc.html#xonsh.proc.CommandPipeline)
* **`@()`**: Evaluate Python. `str` (not split), sequence, or callable (in the same form as callable aliases)
* **`@$()`**: Execute and split

* **`|`**: Shell-style pipe
* **`and`**, **`or`**: Logically joined commands, lazy
* **`&&`**, **`||`**: Same

* **`COMMAND &`**: Background into job (May use `jobs`, `fg`, `bg`)

## Redirection
* **`>`**: Write (stdout) to
* **`>>`**: Append (stdout) to
* **`</spam/eggs`**: Use file for stdin
* **`out`**, **`o`**
* **`err`**, **`e`**
* **`all`**, **`a`** (left-hand side only)

```
>>> COMMAND1 e>o < input.txt | COMMAND2 > output.txt e>> errors.txt
```

# Strings

* **`"foo"`**: Regular string: backslash escapes
* **`f"foo"`**: Formatted string: brace substitutions, backslash escapes
* **`r"foo"`**: Raw string: unmodified
* **`p"foo"`**: Path string: backslash escapes, envvar substitutions, returns `Path`
* **`pr"foo"`**: Raw Path string: envvar substitutions, returns `Path`
* **`pf"foo"`**: Formatted Path string: backslash escapes, brace substitutions, envvar substitutions, returns `Path`
* **`fr"foo"`**: Raw Formatted string: brace substitutions

# Globbing
* Shell-like globs: Default in subprocess
* **`` `re` ``**, **`` r`re` ``**: Glob by regular expression (Python and Subprocess)
* **``g`glob` ``**: Glob by wildcard (Python and Subprocess)
* **``@spam`egg` ``**: Glob by custom function `spam(s)` (Python and Subprocess)
* **`` pr`re` ``**: Glob by regular expression, returning `Path` instances
* **``pg`glob` ``**: Glob by wildcard, returning `Path` instances

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

# [Help](https://xon.sh/tutorial.html#help-superhelp-with)
* **`?`**: regular help, inline
* **`??`**: superhelp, inline

# Links
* [Tutorial](https://xon.sh/tutorial.html)
