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

    # address = relationship('Address', back_populates='user')
    # address = relationship('Address', lazy="immediate", back_populates='user')
    # address = relationship('Address', uselist=False, lazy="joined", back_populates='user')
    # address = relationship('Address', cascade="all,delete", uselist=False, lazy="joined", back_populates='user')
    address = relationship('Address', cascade="all,delete", uselist=True, order_by='Address.email', lazy="joined", back_populates='user')


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    email = Column(String(40))
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))

    user = relationship('User', cascade="all,delete", back_populates='address')


Base.metadata.create_all(engine)


def get_users():
    users = session.query(User).all()
    return users

def get_user_by_id(id):
    user = session.query(User).filter(User.id == id).one()
    return user

def get_addresses():
    addresses = (
        session.query(Address)
    ).all()

    return addresses


if __name__ == '__main__':

    users = get_users()

    # for user in users:
    #     print(f"{user.id}: {user.name}, {user.address.email}")
    #
    #     # for address in user.address:
    #     #     print(f"-- address {address.id}: {address.email}")

    user_to_delete = get_user_by_id(8)

    session.delete(user_to_delete)

    session.commit()
    session.close()
