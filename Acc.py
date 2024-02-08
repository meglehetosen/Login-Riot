#Database related code
import sqlite3

conn = sqlite3.connect("accounts.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS accountTable (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        path TEXT,
        username TEXT,
        password TEXT
    )
''')
conn.commit()

def AccountSave(path, username, password):
    # Insert data
    cursor.execute('INSERT INTO accountTable (path, username, password) VALUES (?, ?, ?)', (str(path), str(username), str(password)))

    conn.commit()

def printData():
    cursor.execute('SELECT * FROM accountTable')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def returnPaths():
    pathList = []

    with sqlite3.connect("accounts.db") as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT path FROM accountTable')
        rows = cursor.fetchall()
        for row in rows:
            pathList.append(row[0])

    return pathList


def returnUsernames():
    usernameList = []

    with sqlite3.connect("accounts.db") as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT username FROM accountTable')
        rows = cursor.fetchall()
        for row in rows:
            usernameList.append(row[0])

    return usernameList

def returnPasswords():
    passList = []

    with sqlite3.connect("accounts.db") as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT password FROM accountTable')
        rows = cursor.fetchall()
        for row in rows:
            passList.append(row[0])

    return passList

def deleteAll():
    # Delete all rows from the table
    cursor.execute('DELETE FROM accountTable')

    conn.commit()

    # Reset the auto-increment counter
    cursor.execute('VACUUM')



def close():
    conn.close()
