#!/usr/bin/env python

import sys
from cx_Freeze import setup, Executable


build_exe_options = {'packages': ['os']}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'


setup(
    name = 'appveyor-test',
    version = "0.1",
    description = "A small app to test appveyor.",
    options = {'build_exe': build_exe_options},
    executables = [Executable('app/app.py', base=base)]
)
