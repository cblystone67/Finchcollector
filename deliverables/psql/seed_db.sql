DROP DATABASE IF EXISTS music;

CREATE DATABASE music;

\c music

CREATE TABLE bands (
    id serial PRIMARY KEY, -- serial is auto-incrementing integer
    name varchar NOT NULL,
    genre varchar
);


INSERT INTO
    bands (name, genre)
VALUES
    ('Rush', 'prog-rock'), -- 1
    ('The Smiths', 'new wave'), -- 2
    ('M83', 'alternative/indie'), -- 3
    ('Sam Smith', 'dance/pop'), -- 4
    ('Majid Jordan', 'R&B'), -- 5
    ('Jason Derulo', 'R&B/hip-hop'), -- 6 
    ('JAY-Z', 'hip-hop/rap'), -- 7
    ('Dua Lipa', 'pop/dance'), -- 8
    ('Daft Punk', 'dance'), -- 9
    ('Kendrick Lamar', 'hip-hop/rap'); --10;

CREATE TABLE musicians (
    id serial PRIMARY KEY,
    name varchar NOT NULL,
    quote text,
    age INTEGER,
    band_id integer NOT NULL REFERENCES bands (id)
);

INSERT INTO
    musicians (name, quote, band_id, age)
VALUES
    ('Geddy Lee', 'I love to write, it''s my first love.', 1, 71),
    ('Neil Peart', 'If you''ve got a problem, take it out on a drum', 1, 67),
    ('Jeff Jones', NULL, 1, 69),
    ('Anthony Gonzalez', NULL, 3, 43),
    ('Shawn Corey Carter', 'Excellence is being able to perform at a high level over and over again.', 7, 53),
    ('Thomas Bangalter', NULL, 9, 48),
    ('Guy-Manuel de Homem-Christo', NULL, 9, 49),
    ('Kendrick Lamar', 'Look at me, I''m a loser, I''m a winner, I''m good, I''m bad. I''m a sinner, I''m a killer. What I''m doing, I''m saying that I''m human.', 10, 35),
    ('Jason Derulo', 'Hello Friday, I''ve been waiting for you.', 6, 33),
    ('Sam Smith', 'Talking about my deepest and darkest secrets to the world makes me feel better. It''s cathartic.', 4, 30);