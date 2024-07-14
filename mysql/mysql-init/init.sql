CREATE DATABASE IF NOT EXISTS db;
USE db;

-- Verifica se o usuário existe antes de tentar criá-lo
CREATE USER IF NOT EXISTS 'root'@'%' IDENTIFIED BY 'pass_root';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
