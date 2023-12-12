#!/usr/bin/python

import psycopg2
from config import config


def insert_single_shoe(shoe_name, category, no_of_colors, price):
    sql = """INSERT INTO ml_playground.shoes(shoe_name, category, no_of_colors, price)
             VALUES(%s, %s, %s, %s) RETURNING shoe_id;"""
    conn = None
    shoe_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (shoe_name, category, no_of_colors, price))
        # get the generated id back
        shoe_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return shoe_id

def insert_shoe_list(shoe_list):
    sql = "INSERT INTO ml_playground.shoes(shoe_name, category, no_of_colors, price) VALUES(%s, %s, %s, %s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,shoe_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    # insert one vendor
    insert_single_shoe("test", "MEN", 5, 1500.50)
    # insert multiple vendors
    insert_shoe_list([
        ("test", "MEN", 5, 1500.50),
        ("test", "MEN", 5, 1500.50)
    ])