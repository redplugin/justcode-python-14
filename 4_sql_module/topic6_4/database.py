from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

USERNAME = 'postgres'
PASSWORD = 'postgres'
HOST = 'localhost'
PORT = '5432'
DB_NAME = 'blog'

engine = create_engine(
    f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}",
    echo=True,
    client_encoding='utf8',
)

Base = declarative_base()

Session = sessionmaker(bind=engine)


def get_session():
    session = Session()
    return session

