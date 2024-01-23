from crud.posts import create_post, get_posts, get_posts_by_author_id, get_posts_with_author
from crud.users import get_users, create_user, get_user_with_posts_by_username
from database import get_session

if __name__ == '__main__':

    session = get_session()

    # new_user = create_user(
    #     session=session,
    #     username="redfix",
    #     name="max",
    #     surname="red"
    # )
    #
    # print("Created:", new_user.username)

    # users = get_users(session)
    #
    # for user in users:
    #     print(f"{user.id}. Username: {user.username}")

    # new_post = create_post(
    #     session=session,
    #     content="Я Макс, приятно познакомиться!",
    #     author_id=2
    # )

    # posts = get_posts(session)
    # posts = get_posts_by_author_id(session, 2)

    # posts = get_posts_with_author(session)
    # print(f"posts: {posts}")
    # for post, user in posts:
    #     print(f"{post.id}. Author: {user.username}. Content: {post.content}")

    user, posts = get_user_with_posts_by_username(session, 'qospanulan')
    print(f"username: {user.username}\n"
          f"name: {user.name}\n"
          f"surname: {user.surname}\n"
          f"posts:")

    for post in posts:
        print(f"-- Content: {post}")

    session.commit()
    session.close()






