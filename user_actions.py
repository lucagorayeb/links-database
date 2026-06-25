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
    print('[0] - Exit')

def user_interaction():
    option = input('Select an option: ')
    define_db_action(int(option))

def define_db_action(option: int):
    match option:
        case 1:
            data = data_to_insert()
            insert_link_in_db(data)
            restart_program()
        
        case 2:
            category = input('Category: ')
            result = get_links_by_category_from_db(category)
            show_data_from_bd(result)
            restart_program()

        case 3:
            id = input('Id: ')
            result = get_links_by_id_from_db(int(id))
            show_data_from_bd(result)
            restart_program()

        case 4:
            result = get_all_links_from_db()
            show_data_from_bd(result)
            restart_program()
            
        case 0:
            print('Software ended.')

        case _:
            print("Invalid option.")

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

def restart_program():
    user_menu()
    user_interaction()
