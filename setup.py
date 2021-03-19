# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 15:43:13 2021

@author: Saignol
"""

from cx_Freeze import setup, Executable

base = None

executables = [Executable("pdf2jpeg.py", base=base)]

packages = ["idna", "os", "glob", "shutil", "pdf2image"]
excludes = ["selenium", "bs4", "lxml", "nltk", "pandas", "numpy", "numpydoc", "sqlite3", "sqlalchemy", "sklearn", "mysql", "matplotlib", "cryptography", "email"]

options = {
    'build_exe': {    
        'packages':packages,
        'excludes':excludes,
    },
}

setup(
    name = "pdf2jpeg",
    options = options,
    version = "1.0",
    description = 'Voici mon programme',
    executables = executables
)