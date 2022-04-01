USE instabook;

INSERT INTO users (username, display_name, pin, is_admin) VALUES
('emily', 'Emily F', '1234', TRUE),
('emma', 'Emma M', '5678', FALSE),
('kim', 'Kim G', '9876', FALSE),
('youri', 'Youri M', '5432', FALSE),
('omotola', 'Omotola S', '1234', FALSE),
('patricia', 'Patricia P', '9876', FALSE),
('raneen', 'Raneen I', '5432', FALSE),
('anu', 'Anu P', '1234', FALSE);

INSERT INTO followers (follower_user_id, followed_user_id) VALUES
(1, 2),
(1, 3),
(2, 3),
(2, 4),
(3, 4),
(3, 5),
(4, 5),
(4, 6),
(5, 6),
(5, 7),
(6, 7),
(6, 8),
(7, 8),
(7, 1),
(8, 1),
(8, 2);

INSERT INTO books (title, author) VALUES
('Ron Weasley and the Pile of Rocks', 'J. K. Rowling'),
('The Desecration of the Rings', 'J. R. R. Tolkein'),
('The Tiger, the Wizard and the Dishwasher', 'C. S. Lewis'),
('Peter Ferret', 'Beatrix Potter'),
('Pride and Pedicures', 'Jane Austen'),
('Game of Chairs', 'George R. R. Martin');

INSERT INTO book_ratings (user_id, book_id, score, review) VALUES
(1, 1, 2, 'Not really a fan of rocks'),
(2, 2, 3, 'A bit long'),
(2, 3, 5, 'Riveting'),
(3, 4, 5, 'Truly radical'),
(4, 5, 4, 'Gives you an insight into an era'),
(4, 6, 4, 'Very strong writing'),
(5, 1, 3, 'Quite nostalgic'),
(6, 2, 4, 'The ending was surprising'),
(6, 3, 4, 'I do like a good dishwasher'),
(7, 4, 4, 'A fun woodland story'),
(8, 5, 3, 'I prefer manicures'),
(8, 6, 3, 'A bit violent');
