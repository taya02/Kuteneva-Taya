sql-запросы
SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE';
SELECT table_name FROM information_shema.tables WHERE table_schema='p518238_lyc';
SELECT * FROM users;
SELECT * FROM grades;
SELECT * FROM users, grades WHERE users.user_id=grades.users_id;
SELECT * FROM users WHERE fam = 'Кутенева'
