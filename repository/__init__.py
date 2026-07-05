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
from .repository import (
    create_link_repository,
    get_link_by_id_repository,
    get_link_by_category_repository,
    get_all_links_repository,
    update_link_repository,
    delete_link_repository
)
