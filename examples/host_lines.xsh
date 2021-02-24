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
    printx(f'{{GREEN}}Count of lines on {{#00FF00}}{args.host}{{GREEN}}: {{YELLOW}}{lines_count}{{RESET}}')  # Colorizing messages
else:
    printx(f'{{RED}}Error while reading {{YELLOW}}{args.host}{{RED}}! {{RESET}}')
    exit(1)  # Exit with code number 1
