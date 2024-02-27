SELECT * FROM names.names;

INSERT INTO names (name) value ("Bilel");
INSERT INTO names (name) value ("Walid");
INSERT INTO names (name) value ("Yassin"),("Zied"),("Nessrine");

UPDATE names SET name = ("Karim") WHERE id = 3;
UPDATE names SET name = ("Mohsen") WHERE names.id = 4;

SET SQL_SAFE_UPDATES = 0;

DELETE FROM names WHERE names.name = "Karim";

SET SQL_SAFE_UPDATES = 1;

