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
from .services import (
    create_link_service,
    update_link_service,
    get_link_by_category_service,
    delete_link_service,
    get_all_links_service,
    get_link_by_id_service
)
