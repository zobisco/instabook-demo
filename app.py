"""
INSTALLATION GUIDE
To install flask, run `pip install flask`
To install mysql.connector, run `pip install mysql-connector-python`
"""
from flask import Flask, request, flash, make_response, render_template, redirect
from werkzeug.exceptions import HTTPException

from book_management import search_books, get_book_details
from user_management import add_user, username_available, get_user_with_credentials, search_users, get_user_details
from follower_management import add_follower_pair, remove_follower_pair
from rating_management import get_recent_book_ratings, get_recent_user_ratings, get_recent_follower_ratings, \
                              get_book_rating_for_user, add_rating, remove_rating

from utils import should_be_signed_in, should_be_signed_out, get_query_values, get_form_values, get_account_params_error
from config import FLASK_SECRET, FLASK_DEBUG

app = Flask(__name__)
app.secret_key = FLASK_SECRET


@app.get('/')
@should_be_signed_in
def view_feed():
    current_user_id = int(request.cookies.get('user_id'))
    recent_follower_ratings = get_recent_follower_ratings(current_user_id)
    return render_template('feed.html', ratings=recent_follower_ratings)


@app.get('/signup')
@should_be_signed_out
def view_signup():
    return render_template('signup.html')


@app.post('/signup')
@should_be_signed_out
def submit_signup():
    username, display_name, pin = get_form_values('username', 'display_name', 'pin')
    if (error := get_account_params_error(username, display_name, pin)) is not None:
        flash(error)
        return redirect('/signup')
    if not username_available(username):
        flash(f'The username {username} is already taken')
        return redirect('/signup')
    add_user(username, display_name, pin)
    return redirect('/signin')


@app.get('/signin')
@should_be_signed_out
def view_signin():
    return render_template('signin.html')


@app.post('/signin')
@should_be_signed_out
def submit_signin():
    username, pin = get_form_values('username', 'pin')
    if (user_id := get_user_with_credentials(username, pin)) is None:
        flash('Invalid details, please try again')
        return redirect('/signin')
    response = make_response(redirect('/'))
    response.set_cookie('user_id', str(user_id), max_age=3600)
    return response


@app.post('/signout')
@should_be_signed_in
def submit_signout():
    response = make_response(redirect('/signin'))
    response.delete_cookie('user_id')
    return response


@app.get('/books/search')
@should_be_signed_in
def find_book():
    title = get_query_values('title') or ''
    matching_books = search_books(title) if title else None
    return render_template('search_books.html', title=title, books=matching_books)


@app.get('/books/<int:book_id>')
@should_be_signed_in
def view_book(book_id):
    current_user_id = int(request.cookies.get('user_id'))
    book_details = get_book_details(book_id)
    book_ratings = get_recent_book_ratings(book_id)
    current_user_rating = get_book_rating_for_user(book_id, current_user_id)
    current_user_score = current_user_rating[0][0] if len(current_user_rating) > 0 else None
    return render_template('view_book.html', current_user_id=current_user_id, current_user_score=current_user_score, book_details=book_details, book_ratings=book_ratings)


@app.get('/books/<int:book_id>/rate')
@should_be_signed_in
def view_rate_book(book_id):
    current_user_id = int(request.cookies.get('user_id'))
    book_details = get_book_details(book_id)
    current_rating = get_book_rating_for_user(book_id, current_user_id)
    current_score, current_review = current_rating[0] if len(current_rating) > 0 else ('', '')
    return render_template('rate_book.html', book_details=book_details, current_score=current_score, current_review=current_review)


@app.post('/books/<int:book_id>/rate')
@should_be_signed_in
def submit_rate_book(book_id):
    current_user_id = int(request.cookies.get('user_id'))
    score, review = get_form_values('score', 'review')
    remove_rating(current_user_id, book_id)  # Remove any existing rating for the current user
    add_rating(current_user_id, book_id, score, review)  # Add the new rating
    return redirect(f'/books/{book_id}')


@app.post('/books/<int:book_id>/unrate')
@should_be_signed_in
def submit_unrate_book(book_id):
    current_user_id = int(request.cookies.get('user_id'))
    remove_rating(current_user_id, book_id)
    return redirect(f'/books/{book_id}')


@app.get('/users/search')
@should_be_signed_in
def find_user():
    current_user_id = int(request.cookies.get('user_id'))
    name = get_query_values('name') or ''
    matching_users = search_users(name) if name else None
    return render_template('search_users.html', current_user_id=current_user_id, name=name, users=matching_users)


@app.get('/users/<int:user_id>')
@should_be_signed_in
def view_user(user_id):
    is_current_user = (user_id == int(request.cookies.get('user_id')))
    user_details = get_user_details(user_id)
    user_ratings = get_recent_user_ratings(user_id)
    return render_template('view_user.html', is_current_user=is_current_user, user_details=user_details, user_ratings=user_ratings)


@app.get('/users/me')
@should_be_signed_in
def view_self():
    current_user_id = int(request.cookies.get('user_id'))
    return redirect(f'/users/{current_user_id}')


@app.post('/users/<int:user_id>/follow')
@should_be_signed_in
def follow_user(user_id):
    current_user_id = int(request.cookies.get('user_id'))
    add_follower_pair(user_id, current_user_id)
    return redirect(f'/users/{user_id}')


@app.post('/users/<int:user_id>/unfollow')
@should_be_signed_in
def unfollow_user(user_id):
    current_user_id = int(request.cookies.get('user_id'))
    remove_follower_pair(user_id, current_user_id)
    return redirect(f'/users/{user_id}')


@app.errorhandler(HTTPException)
def show_http_error(error):
    if error.code == 404:
        message = 'We couldn\'t find what you were looking for.'
    else:
        message = 'Something went wrong'
    return render_template('error.html', error_code=error.code, error_message=message)


app.run(debug=FLASK_DEBUG)
