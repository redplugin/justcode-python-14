from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

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


Session = sessionmaker(bind=engine)

session = Session()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)

    address = relationship('Address', back_populates='user')


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    email = Column(String(40))
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='address')


def get_users():
    users = session.query(User).all()
    return users


def get_addresses_of_under_30():
    # subq = session.query(User.id).filter(User.age > 30).subquery("subq")
    subq = session.query(User).filter(User.age > 30).subquery("subq")

    # addresses = (
    #     session.query(Address)
    #     .filter(
    #         Address.user_id.in_(subq)
    #     )
    # ).all()

    addresses = (
        session.query(Address, subq.c.name)
        .join(
            subq,
            Address.user_id == subq.c.id   # .c = columns
        )
    ).all()

    return addresses


if __name__ == '__main__':

    addresses = get_addresses_of_under_30()

    for address, user_name in addresses:
        print(f"{address.id}: {address.email}. User: {user_name}")


    session.close()
