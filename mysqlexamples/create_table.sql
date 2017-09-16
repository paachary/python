CREATE TABLE IF NOT EXISTS examples (
  id int(11) NOT NULL AUTO_INCREMENT,
  description varchar(45),
  PRIMARY KEY (id)
);

INSERT INTO examples(description) VALUES ("Hello World");
INSERT INTO examples(description) VALUES ("MySQL Example");
INSERT INTO examples(description) VALUES ("Flask Example");
