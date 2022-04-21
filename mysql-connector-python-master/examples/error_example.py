from datetime import datetime

import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared

def main(config):
    output = []
    db = mysql.connector.Connect(**config)
    #cursor = db.cursor(cursor_class=MySQLCursorPrepared)
    
    
    def q(query):
        c = db.cursor(cursor_class=MySQLCursorPrepared)
        c.execute(query)
        for r in c:
            print (r)
        
    db = mysql.connector.Connect(**config)
    q("create database db23")
    q("create table db23.t(a time)")
    q("insert into db23.t values(0)")
    q("select * from db23.t")
    db.close()
    return output

if __name__ == '__main__':

    config = {
        'host': 'localhost',
        'port': 3306,
        'database': '',
        'user': 'root',
        'password': 'K@Nu&yPw3kaM',
        'use_pure': True
    }

    out = main(config)
    print('\n'.join(out))
