# |-topic6_4
#   |-database.py
#   |-models
#     |-users.py
#     |-posts.py
#     |-comments.py
#   |-crud
#     |-users.py
#     |-posts.py
#     |-comments.py
#


from sqlalchemy import select, func
from sqlalchemy.orm import Session

from models import User, Post


def get_users(session):
    # users = session.execute(
    #     select(User)
    # ).scalars().all()

    users = (
        session.query(User)
    ).all()

    return users


def get_user_with_posts_by_username(
        session: Session,
        username: str
):

    user = (
        session.query(
            User,
            func.array_agg(Post.content)
        )
        .filter(
            User.username == username
        )
        .join(User.posts)
        .group_by(User)
    ).one()

    return user


def create_user(
        session: Session,
        username: str,
        name: str,
        surname: str
):
    new_user = User(
        username=username,
        name=name,
        surname=surname
    )

    session.add(new_user)

    return new_user

















