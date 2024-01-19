
from database import get_session
from models import User

session = get_session()


# Create
def create_user(new_user):
    session.add(new_user)
    session.commit()
    return new_user


def get_users():
    users = session.query(User).all()

    for user in users:
        print(f"{user.id}: {user.name} {user.surname}, {user.age}")

    return users


def get_user(user_id):
    user = (
        session.query(User)
        .filter(User.id == user_id)
    ).one()

    return user


def update_user():
    user = session.query(User).filter(User.name == 'Ulan').one()  # all(), first(), one()
    print(f"{user.id}: {user.name} {user.surname}, {user.age}")
    user.age = 10
    session.commit()


def delete_user():
    user = session.query(User).filter(User.id == 2).one()  # all(), first(), one()
    print(f"{user.id}: {user.name} {user.surname}, {user.age}")

    session.delete(user)
    session.commit()


if __name__ == "__main__":
    print("Start ...")

    user = get_user(user_id=3)

    user.age = 99
    session.commit()


    session.close()





