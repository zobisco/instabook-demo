from utils import get_db_connection


def get_book_rating_for_user(book_id, user_id):
    """
    Get a specific user's rating for a book
    Required columns: r.score, r.review
    Required tables: book_ratings r
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            # Temporary code
            if book_id == 1:
                return [(5, 'Banging')]
            else:
                return []


def get_recent_book_ratings(book_id):
    """
    Get 10 most recent ratings for a book
    Required columns: u.id, u.username, u.display_name, r.score, r.review
    Required tables: users u, book_ratings r
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            # Temporary code
            return [(1, 'somebody', 'Some Body', 5, 'Banging'),
                    (2, 'somebodyelse', 'Somebody Else', 4, 'It was good I guess')]


def get_recent_user_ratings(user_id):
    """
    Get 10 most recent ratings for a user
    Required columns: b.id, b.title, b.author, r.score, r.review
    Required tables: books b, book_ratings r
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            # Temporary code
            return [(1, 'Some Book', 'Some Author', 5, 'Banging'),
                    (2, 'Some Other Book', 'Some Other Author', 4, 'It was good I guess')]


def get_recent_follower_ratings(user_id):
    """
    Get 10 most recent ratings from followed users
    Required columns: u.id, u.username, u.display_name, b.id, b.title, b.author, r.score, r.review
    Required tables: users u, followers f, books b, book_ratings r
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            # Temporary code
            return [(1, 'somebody', 'Some Body', 1, 'Some Book', 'Some Author', 5, 'Banging'),
                    (2, 'somebodyelse', 'Somebody Else', 2, 'Some Other Book', 'Some Other Author', 4, 'It was good I guess')]


def add_rating(user_id, book_id, score, review):
    """
    Add a user rating for a specific book into the database
    Required tables: book_ratings r
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            # Temporary code
            pass


def remove_rating(user_id, book_id):
    """
    Remove a user rating for a specific book
    Required tables: book_ratings r
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            # Temporary code
            pass
