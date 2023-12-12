#!/usr/bin/python

import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE ml_playground.shoes (
            shoe_id SERIAL PRIMARY KEY,
            shoe_name TEXT,
            category VARCHAR(5),
            no_of_colors INTEGER,
            price REAL
        )
        """,
        """ CREATE TABLE ml_playground.shoes_details (
                shoe_id SERIAL PRIMARY KEY,
                product_code VARCHAR(20) NOT NULL,
                count_of_sizes INTEGER,
                color1 VARCHAR(5),
                color2 VARCHAR(5),
                color3 VARCHAR(5),
                color4 VARCHAR(5),
                color5 VARCHAR(5)
                )
        """,
        """
        CREATE TABLE ml_playground.shoes_feedback (
                shoe_id SERIAL PRIMARY KEY,
                reviews INTEGER,
                size INTEGER,
                comfort VARCHAR(5),
                performance VARCHAR(20),
                rating REAL
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()