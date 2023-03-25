#!/usr/bin/env python
import setuptools

try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = ''

setuptools.setup(
    name='xontrib-cheatsheet',
    version='0.4.2',
    license='MIT',
    author='anki-code',
    author_email='no@no.no',
    description="Cheat sheet for xonsh shell with copy-pastable examples.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=['xonsh'],
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.py']},
    platforms='any',
    url='https://github.com/anki-code/xontrib-cheatsheet',
    project_urls={
        "Documentation": "https://github.com/anki-code/xontrib-cheatsheet/blob/master/README.md",
        "Code": "https://github.com/anki-code/xontrib-cheatsheet",
        "Issue tracker": "https://github.com/anki-code/xontrib-cheatsheet/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Shells",
        "Topic :: System :: System Shells",
        "Topic :: Terminals",
    ]
)
