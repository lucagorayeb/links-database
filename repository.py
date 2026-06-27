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


def get_all_links_repository():
    with engine.connect() as conn:
        stmt = text("SELECT id, category, description, url FROM links")
        return conn.execute(stmt)


def get_link_by_id_repository(id: int):
    with engine.connect() as conn:
        stmt = text("""SELECT id,
                            category,
                            description,
                            url
                    FROM links WHERE id = :id""")
        return conn.execute(stmt, {'id': id})


def get_link_by_category_repository(category: str):
    with engine.connect() as conn:
        stmt = text("""SELECT id,
                            category,
                            description,
                            url
                    FROM links WHERE category = :category""")
        return conn.execute(stmt, {'category': category})


def create_link_repository(data: list[Any]):
    with engine.connect() as conn:
        stmt = text("""INSERT INTO links
                    (
                        category,
                        description,
                        url
                    )
                    VALUES
                    (
                        :category,
                        :description,
                        :url
                    );""")
        conn.execute(stmt, data)
        conn.commit()


def update_link_repository(data: list[Any], id: int):
    with engine.connect() as conn:
        stmt = text("""UPDATE links
                    (
                        category,
                        description,
                        url
                    )
                    VALUES
                    (
                        :category,
                        :description,
                        :url
                    )
                    WHERE id = :id;""")
        data.append({'id': id})
        conn.execute(stmt, data)
        conn.commit()


def delete_link_repository(id: int):
    with engine.connect() as conn:
        stmt = text("DELETE FROM links WHERE id = :id")
        conn.execute(stmt, {'id': id})
        conn.commit()


def get_data_to_update_bkp_file_repository(rows_bkp: int):
    with engine.connect() as conn:
        stmt = text("""SELECT id,
                            category,
                            description,
                            url
                    FROM links WHERE id > :id""")
        conn.execute(stmt, {'id': rows_bkp})
        conn.commit()

