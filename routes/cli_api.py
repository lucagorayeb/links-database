#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : user_interaction.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 26/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from typing import Any
from controllers import (
    create_link_controller,
    update_link_controller,
    get_link_by_category_controller,
    delete_link_controller,
    get_all_links_controller,
    get_link_by_id_controller
)


def user_menu():
    print('[1] - Insert link on db')
    print('[2] - Select by Category')
    print('[3] - Select by Id')
    print('[4] - List all links')
    print('[5] - Update link')
    print('[6] - Delete link')
    print('[0] - Exit')


def user_interaction():
    option = input('Select an option: ')
    define_db_action(int(option))


def define_db_action(option: int):
    db_action = {
        1: create_link_api,
        2: get_link_by_category_api,
        3: get_link_by_id_api,
        4: get_all_links_api,
        5: update_link_api,
        6: delete_link_api,
        0: finish_program
    }
    db_action[option]()
    if not option == 0:
        restart_program()


def create_link_api():
    data = data_to_insert()
    create_link_controller(data)


def update_link_api():
    update_id = id_to_insert()
    update_data = data_to_insert()
    data = update_id.append(update_data)
    update_link_controller(data)


def delete_link_api():
    id = id_to_insert()
    delete_link_controller(id.id)


def get_link_by_category_api():
    category = category_to_insert()
    data = get_link_by_category_controller(category)
    return show_data_from_bd(data)


def get_link_by_id_api():
    id = id_to_insert()
    data = get_link_by_id_controller(id.id)
    return show_data_from_bd(data)


def get_all_links_api():
    data = get_all_links_controller()
    return show_data_from_bd(data)


def data_to_insert():
    category = category_to_insert()
    description = input('Description: ')
    url = input('URL: ')
    return {
        'category': category,
        'description': description,
        'url': url
    }


def id_to_insert():
    id = input('Id: ')
    return {
        'id': id
    }


def category_to_insert():
    return input('Category: ')


def show_data_from_bd(data: list[Any]):
    for dt in data:
        print(f"Id: {dt.id}")
        print(f"Category: {dt.category}")
        print(f"Description: {dt.description}")
        print(f"URL: {dt.url}")
        print()


def finish_program():
    print("Software Ended.")


def restart_program():
    user_menu()
    user_interaction()
