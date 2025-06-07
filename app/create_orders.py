

from core.db_settings import execute_query

def authors_table():
    query = """
CREATE TABLE IF NOT EXISTS authors(
id SERIAL PRIMARY KEY,
full_name VARCHAR(90) UNIQUE);"""

    execute_query(query=query)

def books_table():
    books_query = """
CREATE TABLE IF NOT EXISTS books(
id SERIAL PRIMARY KEY,
title TEXT NOT NULL,
author_id INTEGER NOT NULL,
published_at DATE NOT NULL,
total_count INTEGER NOT NULL CHECK (total_count >= 0),
available_count INTEGER  NOT NULL CHECK (available_count >= 0),
CONSTRAINT unique_title_author UNIQUE (title, author_id));"""

    execute_query(query=books_query)



def users_table():
    user_query = """
CREATE TABLE IF NOT EXISTS users(
id SERIAL PRIMARY KEY,
full_name TEXT,
email VARCHAR(90) UNIQUE,
is_login BOOLEAN DEFAULT FALSE);"""

    execute_query(query=user_query)



def borrows_table():
    borrow_query = """
CREATE TABLE IF NOT EXISTS borrows(
id SERIAL PRIMARY KEY,
user_id INTEGER NOT NULL,
book_id INTEGER NOT NULL,
borrowed_at DATE NOT NULL,
returned_at DATE DEFAULT NULL);"""

    execute_query(query=borrow_query)

