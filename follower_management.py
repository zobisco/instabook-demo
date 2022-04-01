from utils import get_db_connection


def add_follower_pair(followed_user_id, following_user_id):
    """
    Add a new follower for a specific user
    Required tables: followers f
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            pass


def remove_follower_pair(followed_user_id, following_user_id):
    """
    Delete a follower for a specific user
    Required tables: followers f
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            pass
