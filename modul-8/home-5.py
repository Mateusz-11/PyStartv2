import sqlite3
import subprocess
from sys import argv

def get_ips(db_connection):
    cursor = db_connection.cursor()
    res = cursor.execute('SELECT ip FROM ip_to_check')

    return res

def save_status(db_connection, ip:str, is_up:bool):
    cursor = db_connection.cursor()
    cursor.execute('INSERT INTO log VALUES(?, ?)', (
        ip,
        int(is_up)
    ))

def check_if_is_up(ip:str) -> bool:
    output = subprocess.run(['ping', ip], capture_output=True, shell=True)
    if 'could not' in output.stdout.decode('utf8').lower():
        return False

def initialize(db_connection):
    sqls = ['''CREATE TABLE ip_to_check(
    ip TEXT)
    ''',
        '''CREATE TABLE log(
        id INTEGER PRIMARY KEY AUTOINCREAMENT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        is_up INTEGER)
        ''']
    cursor = db_connection.cursor()

    for sql in sqls:
        cursor.execute(sql)

    db_connection.commit()

with sqlite3.connect('ip_to_check.db') as connection:
    if len(argv) == 2 and argv[1] == 'setup':
        initialize(connection)

    for ip, in get_ips(connection):
        save_status(connection, ip, check_if_is_up(ip))