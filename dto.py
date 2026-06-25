#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : dto.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 24/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from pydantic import BaseModel, HttpUrl

class CreateLinkDTO(BaseModel):
    category: str
    description: str
    url: HttpUrl

class IdDTO(BaseModel):
    id: int