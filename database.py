#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : database.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 24/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from sqlalchemy import create_engine


engine = create_engine("sqlite+pysqlite:///links.sqlite3", echo=False)