

from database import get_session
from models import User, Address

session = get_session()


def create_user(new_user):
    session.add(new_user)


def create_address(new_address):
    session.add(new_address)


def get_users():
    users = session.query(User).all()
    return users


def get_addresses():
    addresses = session.query(Address).all()
    return addresses


if __name__ == "__main__":
    print("Start ...")

    address = Address(
        email='user5@example.com',
        user_id='4'
    )
    # create_address(address)

    addresses = get_addresses()

    for address in addresses:
        print(f"{address.id}. user_id:{address.user_id}, email: {address.email}")

    try:
        session.commit()
    except Exception as e:
        print(f"Error is: {e}")
        session.rollback()
    finally:
        session.close()






