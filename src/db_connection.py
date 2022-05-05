import sqlite3
from config import DATABASE_FILE_PATH

db_ = sqlite3.connect(DATABASE_FILE_PATH)


def get_db():
    return db_
