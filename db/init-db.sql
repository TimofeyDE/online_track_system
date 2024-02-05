-- Create a new database
CREATE DATABASE IF NOT EXISTS mysql;
USE mysql;

CREATE TABLE IF NOT EXISTS ClientStatus (
    ip_address VARCHAR(15) NOT NULL,
    mac_address VARCHAR(20) NOT NULL PRIMARY KEY,
    status VARCHAR(10) NOT NULL,
    last_online DATETIME NOT NULL
);
