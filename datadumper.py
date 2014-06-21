import sqlite3 as lol
from datetime import datetime

conn = lol.connect("data.db")
c = conn.cursor();

c.execute("CREATE TABLE IF NOT EXISTS connection (time INTEGER, cin TEXT, cout TEXT)")

def close():
    conn.close()

def insert_connection(ins, outs):
    print("Inserting %s %s" % (ins, outs))

    c.execute("INSERT INTO connection (time, cin, cout) VALUES (?, ?, ?)"
    , (datetime.utcnow().strftime("%s"), ins, outs))

    conn.commit()
