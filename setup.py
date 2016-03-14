#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from cx_Freeze import setup, Executable
 
setup(
 name="main",
 version="0.1",
 description="Sincronario maya",
 author="JDesing",
 executables = [Executable("main.py", base="Win32GUI", icon="src/icono.ico")],
 )
