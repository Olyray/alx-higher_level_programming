-- Create a database and user
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the database
USE hbtn_0d_usa;
-- Create a user
CREATE TABLE 
    IF NOT EXISTS states(
        id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL,
        name VARCHAR(256) NOT NULL
        );
