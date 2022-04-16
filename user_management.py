from utils import get_db_connection


def add_user(username, display_name, pin):
    """
    Add a new user to the database
    Required tables: users
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                            INSERT INTO users
                            (username, display_name, pin)
                            VALUES(%s, %s, %s);""", (username, display_name, pin))
            connection.commit()


# print(add_user('zoescott', 'Zoe', 1234))


def username_available(username):
    """
    Return True if a username is taken, or False otherwise
    Required tables: users u
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            # Temporary code # return False if username in ['somebody', 'somebodyelse'] else True
            cursor.execute("""
                            SELECT * FROM users u
                            WHERE u.username = %s;""", (username,))
            results = cursor.fetchall()
            if len(results) > 0:  # this means there is already a user with the same username in our DB
                return False
            return True


# print(username_available('emily'))  # returns False


def get_user_with_credentials(username, pin):
    """
    Return a user id (if it exists) given a username and pin
    Required columns: u.id
    Required tables: users u
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            # Example - this one is filled in for you
            cursor.execute("""SELECT u.id
                              FROM users u
                              WHERE u.username = %s
                              AND u.pin = %s""", (username, pin))
            user_ids = cursor.fetchall()
            if len(user_ids) > 0:
                return user_ids[0][0]  # Return the id from the first (and hopefully only) row


def search_users(name):
    """
    Get all users whose username or display name is like a particular name
    Required columns: u.id, u.username, u.display_name
    Required tables: users u
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            # Temporary code
            # users = [(1, 'somebody', 'Some Body', '1234'),
            #          (2, 'somebodyelse', 'Somebody Else', '2345')]
            # return [user[:3] for user in users if name in user[1]]
            cursor.execute("""
                            SELECT u.id, u.username, u.display_name
                            FROM users u
                            WHERE u.username LIKE CONCAT('%', %s, '%')
                            OR u.display_name LIKE CONCAT('%', %s, '%');""", (name, name))
            results = cursor.fetchall()
            return results



def get_user_details(user_id):
    """
    Return details of a specific user
    Required columns: u.id, u.username, u.display_name
    Required tables: users u
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            # Temporary code
            # if user_id == 1:
            #     return 1, 'somebody', 'Some Body'
            # else:
            #     return user_id, 'somebodyelse', 'Somebody Else'
            cursor.execute("""
                            SELECT u.id, u.username, u.display_name
                            FROM users u
                            WHERE u.id = %s;""", (user_id,))
            results = cursor.fetchall()
            if len(results) > 0:
                return results[0]


def search_books(title):
    """
    Return a list of books whose titles are like a particular title
    Required columns: b.id, b.title, b.author, AVG(r.score)
    Required tables: books b, book_ratings r
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""SELECT b.id, b.title, b.author, ROUND(AVG(r.score), 1)
                              FROM books b
                              JOIN book_ratings r
                              ON b.id = r.book_id
                              WHERE b.title LIKE CONCAT('%', %s, '%')
                              GROUP BY b.id;""", (title,))
            results = cursor.fetchall()
            return results


def get_book_details(book_id):
    """
    Return details of a specific book
    Required columns: b.id, b.title, b.author, AVG(r.score)
    Required tables: books b, book_ratings r
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""SELECT b.id, b.title, b.author, ROUND(AVG(r.score), 1)
                              FROM books b
                              JOIN book_ratings r
                              ON b.id = r.book_id
                              WHERE b.id = %s
                              GROUP BY b.id;""", (book_id,))
            results = cursor.fetchall()
            if len(results) > 0:
                return results[0]


def get_book_rating_for_user(book_id, user_id):
    """
    Get a specific user's rating for a book
    Required columns: r.score, r.review
    Required tables: book_ratings r
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""SELECT *
                              FROM book_ratings r
                              WHERE r.book_id = %s
                              AND r.user_id = %s;""", (book_id, user_id))
            results = cursor.fetchall()
            return


def get_recent_book_ratings(book_id):
    """
    Get 10 most recent ratings for a book
    Required columns: u.id, u.username, u.display_name, r.score, r.review
    Required tables: users u, book_ratings r
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""SELECT u.id, u.username, u.display_name, r.score, r.review
                              FROM book_ratings r
                              JOIN users u
                              ON r.user_id = u.id
                              WHERE r.book_id = %s;""", (book_id,))
            results = cursor.fetchall()
            return results


def get_recent_user_ratings(user_id):
    """
    Get 10 most recent ratings for a user
    Required columns: b.id, b.title, b.author, r.score, r.review
    Required tables: books b, book_ratings r
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""SELECT b.id, b.title, b.author, r.score, r.review
                              FROM book_ratings r
                              JOIN books b
                              ON r.book_id = b.id
                              WHERE r.user_id = %s;""", (user_id,))
            results = cursor.fetchall()
            return results


def get_recent_follower_ratings(user_id):
    """
    Get 10 most recent ratings from followed users
    Required columns: u.id, u.username, u.display_name, b.id, b.title, b.author, r.score, r.review
    Required tables: users u, followers f, books b, book_ratings r
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""SELECT u.id, u.username, u.display_name, b.id, b.title, b.author, r.score, r.review
                              FROM book_ratings r
                              JOIN books b
                              ON r.book_id = b.id
                              JOIN users u
                              ON r.user_id = u.id
                              JOIN followers f
                              ON u.id = f.followed_user_id
                              WHERE f.following_user_id = %s;""", (user_id,))
            results = cursor.fetchall()
            return results


def add_rating(user_id, book_id, score, review):
    """
    Add a user rating for a specific book into the database
    Required tables: book_ratings r
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO book_ratings
                              (user_id, book_id, score, review)
                              VALUES
                              (%s, %s, %s, %s);""", (user_id, book_id, score, review))
            connection.commit()


def remove_rating(user_id, book_id):
    """
    Remove a user rating for a specific book
    Required tables: book_ratings r
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""DELETE FROM book_ratings
                              WHERE user_id = %s
                              AND book_id = %s;""", (user_id, book_id))
            connection.commit()