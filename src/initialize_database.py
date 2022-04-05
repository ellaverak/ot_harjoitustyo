from db_connection import get_db


def drop_tables(db):
    cursor = db.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS users
    """)

    cursor.execute("""
        DROP TABLE IF EXISTS mommo
    """)

    cursor.execute("""
        DROP TABLE IF EXISTS tricks
    """)

    db.commit()


def create_tables(db):
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            role INTEGER
        );
    """)

    cursor.execute("""
        CREATE TABLE mommo (
            id INTEGER PRIMARY KEY,
            user_id INTEGER REFERENCES users ON DELETE CASCADE,
            name TEXT,
            hunger INTEGER,
            thirst INTEGER,
            clenliness INTEGER,
            happiness INTEGER
        );
    """)

    cursor.execute("""
        CREATE TABLE tricks (
            id INTEGER PRIMARY KEY,
            mommo_id INTEGER REFERENCES mommo ON DELETE CASCADE,
            trick INTEGER
        );
    """)

    db.commit()


def initialize_database():
    db = get_db()

    drop_tables(db)
    create_tables(db)


if __name__ == '__main__':
    initialize_database()