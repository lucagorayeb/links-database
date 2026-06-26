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
Use:
-----------------------------------------------------
"""
from typing import Any
from services import *
    
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
        1: insert_data,
        2: get_data_by_category,
        3: get_data_by_id,
        4: get_all_data,
        5: update_data,
        6: delete_data,
        0: finish_program
    }
    db_action[option]()
    if not option == 0:
        restart_program()

def insert_data():
    data = data_to_insert()
    try:
        insert_link_in_db(data)
    except Exception as error:
        print(f"Error {error=}, {type(error)=}")
        raise

def update_data():
    data = data_to_insert()
    id = input('Id: ')
    try:
        update_links(data, id)
    except Exception as error:
        print(f"Error {error=}, {type(error)=}")
        raise

def data_to_insert():
    category = input('Category: ')
    description = input('Description: ')
    url = input('URL: ')
    return {
        'category': category,
        'description': description,
        'url': url
    }

def get_data_by_category():
    category = input('Category: ')
    try:
        result = get_links_by_category_from_db(category)
        show_data_from_bd(result)
    except Exception as error:
        print(f"Error {error=}, {type(error)=}")
        raise

def get_data_by_id():
    id = input('Id: ')
    try:
        result = get_links_by_id_from_db(int(id))
        show_data_from_bd(result)
    except Exception as error:
        print(f"Error {error=}, {type(error)=}")
        raise

def get_all_data():
    try:
        result = get_all_links_from_db()
        show_data_from_bd(result)
    except Exception as error:
        print(f"Error {error=}, {type(error)=}")
        raise

def show_data_from_bd(result: list[Any]):
    for row in result:
        print(f"Id: {row.id}")
        print(f"Category: {row.category}")
        print(f"Description: {row.description}") 
        print(f"URL: {row.url}")
        print()

def delete_data():
    id = input('Id: ')
    try:
        delete_links(id)
    except Exception as error:
        print(f"Error {error=}, {type(error)=}")
        raise

def finish_program():
    print("Software Ended.")

def restart_program():
    user_menu()
    user_interaction()
