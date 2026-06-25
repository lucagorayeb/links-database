#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : repository.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 24/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from database import engine
from sqlalchemy import text
from typing import Any

def get_all_links():
    with engine.connect() as conn:
        stmt = text("SELECT id, category, description, url FROM links")
        return conn.execute(stmt)

def get_links_by_id(id: int):
    with engine.connect() as conn:
        stmt = text("SELECT id, category, description, url FROM links WHERE id = :id")
        return conn.execute(stmt, {'id': id})

def get_links_by_category(category: str):
    with engine.connect() as conn:
        stmt = text("SELECT id, category, description, url FROM links WHERE category = :category")
        return conn.execute(stmt, {'category': category})
         

def insert_link(data: list[Any]):
    with engine.connect() as conn:
        stmt = text("INSERT INTO links (category, description, url) VALUES (:category, :description, :url);")
        conn.execute(stmt, data)
        conn.commit()

