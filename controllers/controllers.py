#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : user_actions.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 25/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
"""
from .dto import CreateLinkDTO, IdDTO
from services import (
    create_link_service,
    update_link_service,
    get_link_by_category_service,
    delete_link_service,
    get_all_links_service,
    get_link_by_id_service
)


def create_link_controller(data: CreateLinkDTO):
    try:
        create_link_service(data)
    except Exception as error:
        print(f"Error {error=}, {type(error)=}")
        raise


def update_link_controller(data: CreateLinkDTO, id: IdDTO):
    try:
        update_link_service(data, id)
    except Exception as error:
        print(f"Error {error=}, {type(error)=}")
        raise


def get_link_by_category_controller(category: str):
    try:
        return get_link_by_category_service(category)
    except Exception as error:
        print(f"Error {error=}, {type(error)=}")
        raise


def get_link_by_id_controller(id: IdDTO):
    id = input('Id: ')
    try:
        return get_link_by_id_service(int(id))
    except Exception as error:
        print(f"Error {error=}, {type(error)=}")
        raise


def get_all_links_controller():
    try:
        return get_all_links_service()
    except Exception as error:
        print(f"Error {error=}, {type(error)=}")
        raise


def delete_link_controller(id: IdDTO):
    try:
        delete_link_service(id)
    except Exception as error:
        print(f"Error {error=}, {type(error)=}")
        raise


""" def get_data_to_update_bkp_file_controller(rows_bkp: int):
    try:
       return get_data_to_update_bkp_file_service(rows_bkp)
    except Exception as error:
        print(f"Error {error=}, {type(error)=}")
        raise """
