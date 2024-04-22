#!/usr/bin/env python3
import os
import venv
import subprocess


os.makedirs('user', exist_ok=True)
os.makedirs('file', exist_ok=True)
venv.create('venv', with_pip=True)

subprocess.check_call(['venv/bin/python', '-m', 'pip', 'install', '-r', 'requirements.txt'])