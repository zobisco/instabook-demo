CREATE DATABASE IF NOT EXISTS instabook;
USE instabook;

CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL AUTO_INCREMENT,
    username VARCHAR(20) NOT NULL UNIQUE,
    display_name VARCHAR(50) NOT NULL,
    pin CHAR(4) NOT NULL,
    is_admin BOOLEAN NOT NULL DEFAULT FALSE,

    PRIMARY KEY (id),
    CHECK (LENGTH(username) > 0),
    CHECK (LENGTH(display_name) > 0)
);

CREATE TABLE IF NOT EXISTS followers (
    follower_user_id INTEGER NOT NULL,
    followed_user_id INTEGER NOT NULL,

    PRIMARY KEY (follower_user_id, followed_user_id),
    FOREIGN KEY (follower_user_id) REFERENCES users(id),
    FOREIGN KEY (followed_user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS books (
    id INTEGER NOT NULL AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255),
    isbn VARCHAR(13),

    PRIMARY KEY (id),
    CHECK (LENGTH(title) > 0),
    CHECK (LENGTH(isbn) IN (10, 13))
);

CREATE TABLE IF NOT EXISTS book_ratings (
    user_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    score INTEGER NOT NULL,
    review VARCHAR(255),

    PRIMARY KEY (user_id, book_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    CHECK (score BETWEEN 1 AND 5)
);
