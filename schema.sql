CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    role INTEGER
);

CREATE TABLE mommo (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users ON DELETE CASCADE,
    name TEXT,
    hunger INTEGER
    thirst INTEGER,
    clenliness INTEGER
    happiness INTEGER
);

CREATE TABLE tricks (
    id INTEGER PRIMARY KEY,
    mommo_id INTEGER REFERENCES mommo ON DELETE CASCADE,
    trick INTEGER
);
