import sqlite3

conn = sqlite3.connect('billets.db')
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS billets (
    id_billets TEXT PRIMARY KEY,
    nom TEXT,
    numero TEXT,
    utilise TEXT
    )
"""
)

conn.commit()
conn.close()
