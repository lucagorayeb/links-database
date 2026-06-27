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
from dto import CreateLinkDTO, IdDTO
from repository import (
    create_link_repository,
    get_link_by_id_repository,
    get_link_by_category_repository,
    get_all_links_repository,
    update_link_repository,
    delete_link_repository,
    get_data_to_update_bkp_file_repository
)

def create_link_service(data: CreateLinkDTO):
    create_link_repository(data)


def get_link_by_category_service(category: str):
    return get_link_by_category_repository(category)


def get_link_by_id_service(id: IdDTO):
    return get_link_by_id_repository(id)


def get_all_links_service():
    return get_all_links_repository()


def update_link_service(data: CreateLinkDTO, id: IdDTO):
    return update_link_repository(data, id)


def delete_link_service(id: IdDTO):
    return delete_link_repository(id)

def get_data_to_update_bkp_file_service(rows_bkp: int):
    return get_data_to_update_bkp_file_repository(rows_bkp)