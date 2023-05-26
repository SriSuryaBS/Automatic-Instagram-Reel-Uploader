'''DECODER
from cryptography.fernet import Fernet
def load_key():
    file = open("key" + ".key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)
pasd= input("Pass ; ")
print(fer.decrypt(pasd.encode()).decode())

DELETE EVERYTHING FROM TABLE
import sqlite3

conn = sqlite3.connect('Instadata.db')
c = conn.cursor()

# Delete all rows from table
c.execute('DELETE FROM instagramdata;',);

print('We have deleted', c.rowcount, 'records from the table.')

# Commit the changes to db
conn.commit()
# Close the connection
conn.close()'''
import sqlite3
conn = sqlite3.connect('Instadata.db')
c = conn.cursor()


c.execute("SELECT rowid,* FROM instagramdata ")
items = c.fetchall()
for item in items:
    print(item)

print("created")

