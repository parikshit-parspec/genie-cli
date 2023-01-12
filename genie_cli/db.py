import sqlite3
from datetime import datetime

import pytz


def store_token(token: str):
    con = sqlite3.connect("genie.db")

    # Drop table "token" if it already exists
    con.execute("DROP TABLE IF EXISTS token;")

    # Create table "token"
    con.execute(
        "CREATE TABLE token(token, valid_from DATETIME DEFAULT CURRENT_TIMESTAMP);"
    )

    # Insert a row with the given token
    con.execute(f"INSERT INTO token(token) VALUES('{token}');")

    con.commit()
    con.close()


def get_token():
    con = sqlite3.connect("genie.db")

    # Check that table "token" exists in db
    cur = con.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='token';"
    )
    row = cur.fetchone()
    if not row:
        return "No token found", None, None

    # Check that token exists in db
    cur = con.execute("SELECT COUNT(*) FROM token LIMIT 1;")
    row = cur.fetchone()
    if row[0] != 1:
        return "No token found", None, None

    cur = con.execute("SELECT * FROM token LIMIT 1;")
    row = cur.fetchone()
    token = row[0]
    valid_from = datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")

    return None, token, pytz.utc.localize(valid_from)
