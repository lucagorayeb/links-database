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
from services import *
    
def user_menu():
    print('[1] - Insert link on db')
    print('[2] - Select by Category')
    print('[3] - Select by Id')
    print('[4] - List all links')

def user_interaction():
    option = input('Select an option: ')
    result = define_db_action(int(option))
    for row in result:
        print(f"Id: {row.id}")
        print(f"Category: {row.category}")
        print(f"Description: {row.description}") 
        print(f"URL: {row.url}")
        print()

def define_db_action(option: int):
    match option:
        case 1:
            data = data_to_insert()
            insert_link_in_db(data)
        
        case 2:
            category = input('Category: ')
            return get_links_by_category_from_db(category)

        case 3:
            id = input('Id: ')
            return get_links_by_id_from_db(int(id))

        case 4:
            return get_all_links_from_db()
        
        case _:
            print("Invalid option.")

def data_to_insert():
    category = input('Category: ')
    description = input('Description: ')
    url = input('URL: ')
    data =  {
        'category': category,
        'description': description,
        'url': url
    }
    print(data)
    return data