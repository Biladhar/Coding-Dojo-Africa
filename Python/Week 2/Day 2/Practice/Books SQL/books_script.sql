INSERT INTO users (first_name,last_name) VALUE ("Jane","Amsden"),("Emily","Dixon"),("Theodore","Dostoevsky"),("William","Shapiro"),("Lao","Xiu");

SELECT * FROM users;

INSERT INTO books (title) VALUE ("C Sharp"),("Java"),("Python"),("PHP"),("Ruby");

SELECT * FROM books;

SET SQL_SAFE_UPDATES = 0;

UPDATE books 
SET title = "C#"
WHERE title  = "C Sharp";

UPDATE users
SET first_name = "Bill"
WHERE id  = 4;

INSERT INTO favorites (user_id,book_id) VALUE (1,1),(1,2);

SELECT * FROM favorites;

INSERT INTO favorites (user_id,book_id) VALUE (2,1),(2,2),(2,3);

INSERT INTO favorites (user_id,book_id) VALUE (3,1),(3,2),(3,3),(3,4);

INSERT INTO favorites (user_id,book_id) VALUE (4,1),(4,2),(4,3),(4,4),(4,5);

SELECT * FROM users
JOIN favorites ON favorites.user_id = users.id
WHERE favorites.book_id = 3;

DELETE FROM favorites
WHERE favorites.book_id = 3
ORDER BY favorites.user_id ASC
LIMIT 1 ;

INSERT INTO favorites (user_id,book_id) VALUE (5,2);

SELECT *
FROM users
LEFT JOIN favorites
ON users.id = favorites.user_id
LEFT JOIN books
ON favorites.book_id = books.id
WHERE users.id= 3;

SELECT *
FROM books
LEFT JOIN favorites
ON books.id = favorites.book_id
LEFT JOIN users
ON favorites.user_id = users.id
WHERE books.id= 5;



