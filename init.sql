DROP DATABASE chatapp;
DROP USER 'testuser'@'localhost';

CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testuser';
CREATE DATABASE chatapp;
USE chatapp
GRANT ALL PRIVILEGES ON chatapp.* TO 'testuser'@'localhost';

CREATE TABLE users (
    uid varchar(255) PRIMARY KEY,
    user_name varchar(255) UNIQUE NOT NULL,
    email varchar(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL
);

CREATE TABLE channels (
    id serial PRIMARY KEY,
    uid varchar(255) REFERENCES users(uid),
    name varchar(255) UNIQUE NOT NULL,
    abstract varchar(255)
);

CREATE TABLE messages (
    id serial PRIMARY KEY,
    uid varchar(255) REFERENCES users(uid),
    cid integer REFERENCES channels(id) ON DELETE CASCADE,
    message text,
    created_at timestamp not null default current_timestamp
);

CREATE TABLE todolist (
    id serial PRIMARY KEY,
    uid varchar(255) REFERENCES users(uid),
    proity varchar(10),
    tkname varchar(255) UNIQUE NOT NULL,
    expr varchar(50),
    don varchar(10)
);

CREATE TABLE sitagaki (
    id serial PRIMARY KEY,
    uid varchar(255) REFERENCES users(uid),
    cid integer REFERENCES channels(id) ON DELETE CASCADE,
    message text,
    created_at timestamp not null default current_timestamp
);

CREATE TABLE teikeibun (
    id serial PRIMARY KEY,
    uid varchar(255) REFERENCES users(uid),
    message text,
    created_at timestamp not null default current_timestamp
);

CREATE TABLE sured (
    id serial PRIMARY KEY,
    uid varchar(255) REFERENCES users(uid),
    cid integer REFERENCES channels(id) ON DELETE CASCADE,
    message text,
    created_at timestamp not null default current_timestamp
);

CREATE TABLE imag (
    id serial PRIMARY KEY,
    uid varchar(255) REFERENCES users(uid),
    path varchar(255) not null
);

INSERT INTO users(uid, user_name, email, password)VALUES('970af84c-dd40-47ff-af23-282b72b7cca8','テスト','test@gmail.com','37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578');
INSERT INTO channels(id, uid, name, abstract)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8','部屋','テストさんの部屋です');
INSERT INTO messages(id, uid, cid, message)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', '初の投稿です。');
INSERT INTO todolist(id, uid, proity, tkname, expr, don)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8','高い','朝食を食べる','3-4まで','未完了');
INSERT INTO sitagaki(id, uid, cid, message)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', 'ここに下書きは表示されます');
INSERT INTO teikeibun(id, uid, cid, message)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', 'よろしくお願いいたします。');
INSERT INTO sured(id, uid, cid, message)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', 'これはメッセージに対しての返信です。');
INSERT INTO imag(path)VALUES('This is INIT.');