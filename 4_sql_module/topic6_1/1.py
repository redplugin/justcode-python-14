from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

USERNAME = 'postgres'
PASSWORD = 'postgres'
HOST = 'localhost'
PORT = '5432'
DB_NAME = 'sql_alchemy_test'

engine = create_engine(f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}')

metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('surname', String),
    Column('age', Integer),
)

metadata.create_all(engine)


















# with engine.connect() as conn:
#     conn.execute(text("""
#         SELECT * FROM test;
#     """))
