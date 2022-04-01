from utils import get_db_connection


def search_books(title):
    """
    Return a list of books whose titles are like a particular title
    Required columns: b.id, b.title, b.author, AVG(r.score)
    Required tables: books b, book_ratings r
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            # Temporary code
            books_with_average_scores = [(1, 'Some Book', 'Some Author', 5),
                                         (2, 'Some Other Book', 'Some Other Author', 4)]
            return [book for book in books_with_average_scores if title in book[1]]


def get_book_details(book_id):
    """
    Return details of a specific book
    Required columns: b.id, b.title, b.author, AVG(r.score)
    Required tables: books b, book_ratings r
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            # Temporary code
            if book_id == 1:
                return 1, 'Some Book', 'Some Author', 5
            else:
                return book_id, 'Some Other Book', 'Some Other Author', 4
