CREATE DATABASE IF NOT EXISTS inventory;

USE inventory;

CREATE TABLE IF NOT EXISTS customers (
  id INT(11) NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO customers (first_name, last_name, email) VALUES
  ('Jane', 'Doe', 'janedoe@example.com'),
  ('Bob', 'Smith', 'bobsmith@example.com'),
  ('Alice', 'Johnson', 'alicejohnson@example.com');
