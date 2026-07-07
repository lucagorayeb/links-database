#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : content.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 24/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
class Link:
    def __init__(self, category: str,
                 description: str,
                 url: str):
        
        self._category = category
        self._description = description
        self._url = url
        
        if category is None or description is None or url is None:
            raise ValueError("The field can not be empty.")

    def __str__(self) -> str:
        return f"""Content(
                    category: {self.content},
                    description: {self.description},
                    url: {self.url}
                )"""
