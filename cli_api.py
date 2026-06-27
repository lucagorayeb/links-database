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
from controllers import (
    create_link_controller,
    update_link_controller,
    get_link_by_category_controller,
    delete_link_controller,
    get_all_links_controller,
    get_link_by_id_controller,
    get_data_to_update_bkp_file_controller
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
        1: create_link_controller,
        2: get_link_by_category_controller,
        3:  get_link_by_id_controller,
        4: get_all_links_controller,
        5: update_link_controller,
        6: delete_link_controller,
        0: finish_program
    }
    db_action[option]()
    if not option == 0:
        restart_program()

def finish_program():
    print("Software Ended.")


def restart_program():
    user_menu()
    user_interaction()

def data_to_insert():
    category = input('Category: ')
    description = input('Description: ')
    url = input('URL: ')
    return {
        'category': category,
        'description': description,
        'url': url
    }

def show_data_from_bd(result: list[Any]):
    for row in result:
        print(f"Id: {row.id}")
        print(f"Category: {row.category}")
        print(f"Description: {row.description}")
        print(f"URL: {row.url}")
        print()