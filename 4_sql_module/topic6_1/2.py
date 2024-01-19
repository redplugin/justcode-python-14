from sqlalchemy import create_engine, Column, Integer, String, desc
from sqlalchemy.orm import declarative_base, sessionmaker

USERNAME = 'postgres'
PASSWORD = 'postgres'
HOST = 'localhost'
PORT = '5432'
DB_NAME = 'sql_alchemy_test'

engine = create_engine(
    f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}',
    echo=True,
    client_encoding='utf8',
)

Base = declarative_base()


# Модели, схемы
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)


# Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

# Create
# new_user = User(
#     name='User4',
#     surname='xxxxx',
#     age=99
# )
#
# session.add(new_user)
# session.commit()

# SELECT * FROM users
# users = session.query(User).all()
# print("All users..:")
# for user in users:
#     # print(user.name)
#     print(user.__dict__)

# user = session.query(User).first()
# print(user.__dict__)


# users = session.query(User).filter(User.name == 'Ulan').all()
# users = session.query(User).filter_by(name='Ulan').all()
# print("All users..:")
# for user in users:
#     print(user.__dict__)


# users = (
#     session
#     .query(User)
#     .order_by(desc(User.age))
#     .limit(1)
#     .offset(2)
# ).all()
#
# print("All users..:")
# for user in users:
#     print(user.__dict__)


users = (
    session
    .query(User.age)
    .group_by(User.age)
).all()

print("All users..:")
print(users)
# for user in users:
#     print(user.__dict__)




session.close()
