from db_connection import get_db


def drop_tables(db_):
    """poistaa kaikki taulut tietokannasta,
    """

    cursor = db_.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS users
    """)

    cursor.execute("""
        DROP TABLE IF EXISTS mommo
    """)

    cursor.execute("""
        DROP TABLE IF EXISTS tricks
    """)

    db_.commit()


def create_tables(db_):
    """luo taulut tietokantaan.
    """

    cursor = db_.cursor()

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
            jump INTEGER,
            squish INTEGER,
            play_dead INTEGER
        );
    """)

    db_.commit()


def initialize_database():
    """hakee tietokantayhteyden ja kutsuu tietokannanrakennus-funktioita.
    """

    db_ = get_db()

    drop_tables(db_)
    create_tables(db_)


if __name__ == '__main__':
    initialize_database()
