from faker import Faker
import psycopg2
import random
from datetime import datetime, timedelta

fake = Faker()

conn = psycopg2.connect(
    host="localhost",  # 116.202.177.123 port: 5432
    user="postgres",
    password="postgres",
    database="python14"
)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50),
        email VARCHAR(100),
        created_at TIMESTAMP,
        role_name VARCHAR(30)
    );
""")

roles = ['admin', 'moderator', 'web_app_user', 'guest']
genders = ['male', 'female']
for _ in range(100):
    username = fake.user_name()
    email = fake.email()
    created_at = fake.date_time_this_decade(before_now=True, after_now=False)
    # fake.
    role_name = random.choice(roles)

    cursor.execute(f"""
        INSERT INTO users (username, email, created_at, role_name)
        VALUES ('{username}', '{email}', '{created_at}', '{role_name}');
    """)

conn.commit()
cursor.close()
conn.close()

