import sqlite3
#from config import DATABASE_FILE_PATH

db = sqlite3.connect("/home/korkella/projektit/ot_harjoitustyo/src/base.db")


def get_db():
    return db