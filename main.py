from product_data import data
import sqlite3



# Connect DB and create cursor
db = sqlite3.connect('products.db')
cursor = db.cursor()


# Create table
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS products(
        isbn INTEGER,
        publisher TEXT,
        publication_date TEXT,
        series TEXT,
        edition_description TEXT,
        pages INTEGER,
        sales_rank INTEGER,
        product_dimensions TEXT
    )
    '''
)


# Insert Data
cursor.executemany(
    'INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?, ?)', data
)


# Commit Insert
db.commit()


# Display inserted data
for row in cursor.execute('SELECT * FROM products'):
    print(row)


# Close db
db.close()