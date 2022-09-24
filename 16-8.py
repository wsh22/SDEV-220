import sqlite3

conn = sqlite3.connect('books.db')
c = conn.cursor()

# create books table
c.execute('''CREATE TABLE books
            (title text, author text, year integer)''')

# insert data into books table
c.execute("INSERT INTO books VALUES ('The Catcher in the Rye', 'J.D. Salinger', 1951)")
c.execute("INSERT INTO books VALUES ('The Great Gatsby', 'F. Scott Fitzgerald', 1925)")
c.execute("INSERT INTO books VALUES ('To Kill a Mockingbird', 'Harper Lee', 1960)")

# commit changes
conn.commit()

# close connection
conn.close()

import sqlite3

conn = sqlite3.connect('books.db')
c = conn.cursor()

# select title column from books table
c.execute('SELECT title FROM books ORDER BY title')

# print titles in alphabetical order
for row in c:
   print(row)

# close connection
conn.close()


import sqlite3

conn = sqlite3.connect('books.db')
c = conn.cursor()

# select all columns from books table
c.execute('SELECT * FROM books ORDER BY year')

# print all columns in order of publication
for row in c:
   print(row)

# close connection
conn.close()

import sqlalchemy

# connect to sqlite database
engine = sqlalchemy.create_engine('sqlite:///books.db', echo=True)

# select title column from books table
result = engine.execute('SELECT title FROM books ORDER BY title')

# print titles in alphabetical order
for row in result:
   print(row)