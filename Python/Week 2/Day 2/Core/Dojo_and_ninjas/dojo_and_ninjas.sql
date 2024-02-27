INSERT INTO dojos_and_ninjas_shema.dojos (name) VALUES ("coding"),("art"),("music");

SELECT * FROM dojos_and_ninjas_shema.dojos ;

SET SQL_SAFE_UPDATES = 0;

DELETE FROM dojos_and_ninjas_shema.dojos ;

INSERT INTO dojos_and_ninjas_shema.dojos (name) VALUES ("coding2"),("art2"),("music2");

SELECT * FROM dojos_and_ninjas_shema.ninjas ;

INSERT INTO dojos_and_ninjas_shema.ninjas (first_name , last_name , age , dojo_id ) VALUES ("steve","jobs",80,4), ("elon","musk",46, 4) ,("bill","gates",53,4);

INSERT INTO dojos_and_ninjas_shema.ninjas (first_name , last_name , age , dojo_id ) VALUES ("micheal","jackson",102,5), ("janenet","jackson",58, 5) ,("raouf","maher",45,5);

INSERT INTO dojos_and_ninjas_shema.ninjas (first_name , last_name , age , dojo_id ) VALUES ("cristiano","ronaldo",36,6), ("leo","messi",38, 6) ,("youssef","msakni",30,6);

SELECT * FROM  dojos_and_ninjas_shema.ninjas WHERE dojo_id = 4 ;

SELECT * FROM  dojos_and_ninjas_shema.ninjas WHERE dojo_id = 6 ;

SELECT dojos.name FROM dojos
JOIN ninjas ON dojo_id = ninjas.dojo_id
ORDER BY ninjas.id DESC
LIMIT 1;

SELECT * FROM ninjas 
JOIN dojos ON dojos.id = ninjas.dojo_id 
WHERE ninjas.id = 6 ;

SELECT * FROM ninjas 
JOIN dojos ON dojos.id = ninjas.dojo_id ;