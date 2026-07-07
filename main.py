#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : main.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 24/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from routes.cli_api import user_menu, user_interaction
from config.config import (
    verify_database
)

verify_database()
user_menu()
user_interaction()
