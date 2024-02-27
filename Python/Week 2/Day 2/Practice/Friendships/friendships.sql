SELECT * FROM users;

SELECT * FROM friendships;

INSERT INTO users (first_name,last_name) VALUES ("Mario","Bros"),("Monkydy","Luffy"),("Zorro","Roronowa"),("Naruto","Uzumaki"),("Luigi","Bros"),("Link","Zelda");

INSERT INTO friendships (user_id,friend_id) VALUES (1,2),(1,4),(1,6);

INSERT INTO friendships (user_id,friend_id) VALUES (2,1),(2,3),(2,5);

INSERT INTO friendships (user_id,friend_id) VALUES (3,2),(3,5);

INSERT INTO friendships (user_id,friend_id) VALUES (4,3);

INSERT INTO friendships (user_id,friend_id) VALUES (5,1),(5,6);

INSERT INTO friendships (user_id,friend_id) VALUES (6,2),(6,3);

DELETE FROM friendships 
WHERE id in (4,5,6);

SELECT users.first_name as first_name, users.last_name as last_name,user2.first_name as friend_first_name, user2.last_name as friend_last_name FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON user2.id = friendships.friend_id;

SELECT user2.first_name as friend_first_name, user2.last_name as friend_last_name FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON user2.id = friendships.friend_id
WHERE users.id = 1;

SELECT COUNT(*) FROM friendships;

SELECT user_id, COUNT(user_id) AS count
FROM friendships
GROUP BY user_id
ORDER BY count DESC
LIMIT 1;

SELECT user_id , user2.first_name as friend_first_name, user2.last_name as friend_last_name FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON user2.id = friendships.friend_id
WHERE users.id = 3
ORDER BY friend_first_name ASC ;






