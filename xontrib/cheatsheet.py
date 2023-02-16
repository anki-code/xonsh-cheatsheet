"""Cheat sheet for xonsh shell with copy-pastable examples. The best doc for the new users. """

def _cheatsheet():
    import webbrowser
    url = "https://github.com/anki-code/xonsh-cheatsheet/blob/main/README.md"
    printx(f'{{YELLOW}}Opening: {url}')
    webbrowser.open("https://github.com/anki-code/xonsh-cheatsheet/blob/main/README.md")

aliases['cheatsheet'] = _cheatsheet
del _cheatsheet
