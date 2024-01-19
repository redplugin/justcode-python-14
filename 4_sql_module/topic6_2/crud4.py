from sqlalchemy import func, and_, or_

from database import get_session
from models import User, Address

session = get_session()


def get_users_with_email():
    users = (
        session.query(
            User,
            Address
        )
        .join(
            Address,
            User.age == Address.user_id
        )
    ).all()

    return users


if __name__ == "__main__":
    print("Start ...")

    users = get_users_with_email()
    # print(users)
    for user, address in users:
        print(f"user_name: {user.name}, email: {address.email}")







