import sqlite3


def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    conn.execute("INSERT INTO store VALUES ('Wine Glass', 8, 10.5)")
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    conn.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    conn.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    conn.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (
        quantity, price, item,))
    conn.commit()
    conn.close()


update(12, 6, "Water Glass")

print(view())
