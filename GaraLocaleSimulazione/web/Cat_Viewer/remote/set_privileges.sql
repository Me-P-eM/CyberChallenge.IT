REVOKE ALL PRIVILEGES ON imgdb.* FROM 'imguser'@'%';
GRANT SELECT ON imgdb.* TO 'imguser'@'%';
FLUSH PRIVILEGES;
