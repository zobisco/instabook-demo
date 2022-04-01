from utils import get_db_connection


def add_user(username, display_name, pin):
    """
    Add a new user to the database
    Required tables: users
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            # Temporary code
            pass


def username_available(username):
    """
    Return True if a username is taken, or False otherwise
    Required tables: users u
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            # Temporary code
            return False if username in ['somebody', 'somebodyelse'] else True


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
            users = [(1, 'somebody', 'Some Body', '1234'),
                     (2, 'somebodyelse', 'Somebody Else', '2345')]
            return [user[:3] for user in users if name in user[1]]


def get_user_details(user_id):
    """
    Return details of a specific user
    Required columns: u.id, u.username, u.display_name
    Required tables: users u
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            # Temporary code
            if user_id == 1:
                return 1, 'somebody', 'Some Body'
            else:
                return user_id, 'somebodyelse', 'Somebody Else'
