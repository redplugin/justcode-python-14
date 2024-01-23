from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Post, User


def get_posts(session):
    # posts = session.execute(
    #     select(Post)
    # ).scalars().all()

    posts = (
        session.query(Post)
    ).all()

    return posts


def get_posts_by_author_id(
        session: Session,
        author_id: int
):
    # posts = session.execute(
    #     select(Post)
    # ).scalars().all()

    posts = (
        session.query(Post)
        .filter(
            Post.author_id == author_id
        )
    ).all()

    return posts


def get_posts_with_author(
        session: Session,
):
    # posts = session.execute(
    #     select(Post)
    # ).scalars().all()

    posts = (
        session.query(
            Post,
            User
        )
        .join(
            Post.author
        )
    ).all()

    return posts


def create_post(
        session: Session,
        content: str,
        author_id: int,
):
    new_post = Post(
        content=content,
        author_id=author_id,
    )

    session.add(new_post)

    return new_post

