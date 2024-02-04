-- Create a new database
CREATE DATABASE IF NOT EXISTS mysql;
USE mysql;

-- Drop the user if it already exists and create a new one
DROP USER IF EXISTS 'dartchain'@'%';
CREATE USER 'dartchain'@'%' IDENTIFIED BY 'bitcoin2008';

-- Grant privileges to the user on the newly created database
GRANT ALL PRIVILEGES ON *.* TO 'dartchain'@'%';

-- Apply the changes
FLUSH PRIVILEGES;
