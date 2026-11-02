import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv


PHASE02_DIR = Path(__file__).resolve().parent
load_dotenv(PHASE02_DIR / ".env")


def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )


def check_connection():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT current_database(), current_schema()")
            return cursor.fetchone()


def find_member_by_email(cursor, email: str):
    cursor.execute(
        "SELECT id FROM members WHERE email = %s",
        (email,),
    )
    return cursor.fetchone()


def insert_member(cursor, name: str, email: str, age: int):
    cursor.execute(
        """
        INSERT INTO members (name, email, age)
        VALUES (%s, %s, %s)
        RETURNING id, name, email, age
        """,
        (name, email, age),
    )
