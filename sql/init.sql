
CREATE DATABASE  plantwateringdb;
CREATE USER 'dbuser'@'localhost' IDENTIFIED BY 'Welcome$16';
GRANT ALL PRIVILEGES ON plantwateringdb.* TO 'dbuser'@'localhost';
FLUSH PRIVILEGES;
