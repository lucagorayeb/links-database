#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : __init__.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 04/07/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from .controllers import (
    create_link_controller,
    update_link_controller,
    get_link_by_category_controller,
    delete_link_controller,
    get_all_links_controller,
    get_link_by_id_controller
)
