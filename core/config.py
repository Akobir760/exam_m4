import os

import psycopg2
from dotenv import load_dotenv

load_dotenv(
    dotenv_path=".env"
)

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

DB_CONFIG = {
    "database": 'm4_exam',
    "user": 'm4_exam',
    "port": 5432,
    "host": 'localhost',
    "password": 'm4_exam'
}
def get_connection():
    return psycopg2.connect(**DB_CONFIG)