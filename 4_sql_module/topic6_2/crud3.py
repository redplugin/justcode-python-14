from sqlalchemy import func

from database import get_session
from models import User, Address

session = get_session()


def get_grouped_users():
    users = (
        session.query(
            User.age,
            func.count(User.id),
            func.max(User.id)
        )
        .group_by(User.age)
    ).all()

    return users


if __name__ == "__main__":
    print("Start ...")

    users = get_grouped_users()

    for age, count, max_user_id in users:
        print(f"age: {age}, count: {count}, max_user_id: {max_user_id}")







