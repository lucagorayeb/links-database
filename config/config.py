#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : config.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 25/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
import shutil as shu
from pathlib import Path
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()


def return_enviroment_variables(variable: str) -> str:
    env_variables = {
        'db_schema': os.getenv('DB_SCHEMA'),
        'db_server': os.getenv('DB_SERVER'),
        'db_file': os.getenv('DB_FILE'),
        'bkp_file': os.getenv('BKP_FILE'),
    }
    return env_variables[f"{variable}"]


def verify_database():
    db_schema = return_enviroment_variables('db_schema')
    db_server = return_enviroment_variables('db_server')
    db_file = return_enviroment_variables('db_file')
    bkp_file = return_enviroment_variables('bkp_file')

    if db_schema == '' or db_server == '' or db_file == '' or bkp_file == '':
        raise ValueError('Enviroment variables are empty.')
    else:
        db_file_path = Path(db_file)
        bkp_file_path = Path(bkp_file)

    if not db_file_path.exists() and not bkp_file_path.exists():

        print('! NONE DATABASE FOUNDED !')
        print('! A NEW WILL BE CREATED !')
        create_new_database(db_server, db_file, db_schema)

    elif bkp_file_path.exists() and not db_file_path.exists():
        create_database_from_bkp(bkp_file_path, db_file_path)

    elif not bkp_file_path.exists() and db_file_path.exists():
        create_backup(db_file_path, bkp_file_path)


def create_new_database(db_server: str, db_file: str, db_schema: str) -> None:
    subprocess.run([db_server, db_file, '<', db_schema])


def create_database_from_bkp(bkp_file_path: str, db_file_path: str) -> None:
    shu.copy(bkp_file_path, db_file_path, follow_symlinks=False)


def create_backup(db_file_path: str, bkp_file_path: str) -> None:
    shu.copy(db_file_path, bkp_file_path, follow_symlinks=False)
