SELECT * FROM users_schema.users;

insert INTO users (first_name , last_name , email) VALUES ("Walid" , "Guetat" , "Walidguetat@dojo.com") , ( "Bilel" , "Laadhar" , "Bilellaadhar@dojo.com") , ("Slimane" , "Labyath" , "Drslimaelabyath@psy.com");

SELECT * FROM users_schema.users;

SELECT * FROM users WHERE users.email = "Walidguetat@dojo.com" ;

SELECT * FROM users WHERE users.id = 3 ;

UPDATE users_schema.users SET last_name = "Pancakes" WHERE id = 3 ;

-- SELECT * FROM users_schema.users;

DELETE FROM users_schema.users WHERE id = 2 ;

-- SELECT * FROM users_schema.users;

SELECT * FROM users_schema.users ORDER BY first_name ASC;

SELECT * FROM users_schema.users ORDER BY first_name DESC;