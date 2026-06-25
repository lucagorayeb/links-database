#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : services.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 25/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from repository import insert_link, get_links_by_category, get_links_by_id, get_all_links
from dto import CreateLinkDTO, IdDTO

def insert_link_in_db(data: CreateLinkDTO):
    insert_link(data)

def get_links_by_category_from_db(category: str):
    return get_links_by_category(category)

def get_links_by_id_from_db(id: IdDTO):
    return get_links_by_id(id)

def get_all_links_from_db():
    return get_all_links()