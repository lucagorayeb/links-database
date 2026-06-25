#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : config.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 25/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from pathlib import Path
import subprocess

def verify_database():
    db_path = Path('links.sqlite3');
    if not db_path.exists():
        subprocess.run(['sqlite3', 'links.sqlite3', '<', 'schema.sql'])

