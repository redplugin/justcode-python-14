from faker import Faker
import psycopg2
import random
from datetime import datetime, timedelta

fake = Faker()

with psycopg2.connect(
        host="localhost",  # 116.202.177.123 port: 5432
        user="postgres",
        password="postgres",
        database="python14"
    ) as conn:

    with conn.cursor() as cursor:

        cursor.execute("""
            SELECT * FROM users LIMIT 5;
        """)

        data = cursor.fetchall()
        for row in data:
            print(row)


