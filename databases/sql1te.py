import psycopg2
 
def create_table():
    conn=psycopg2.connect(             
             dbname = "pmc",
              user = "posgress",
              password = "Hneilson1",
              host = "localhost",
              port = "5432")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    cur.execute("INSERT INTO store VALUES('Wine Glass',8,10.5)")
    conn.commit()
    conn.close()
 
create_table()  
 
def insert(item,quantity,price):
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()
 
insert ("mug", 20, 3)
 
def view ():
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows
 
def delete (item):
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()
   
 
def update (quantity,price,item):
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price =? WHERE item=?",(quantity,price,item)) 
    conn.commit()
    conn.close()
 
 
# update(11,6,"Water Glass")
 
 
# print (view())
